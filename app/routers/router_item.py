from fastapi import Depends, APIRouter, HTTPException, Security, Response, status
from sqlalchemy.orm import Session

from .. import schemas, crud
from ..core.database import SessionLocal
from ..dependencies import get_current_active_user


router = APIRouter()

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/items/", response_model=list[schemas.Item])
def read_items(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    items = crud.get_items(db, skip=skip, limit=limit)
    return items

@router.post("/users/{user_id}/items/", response_model=schemas.Item)
def create_item_for_user(
    user_id: int, item: schemas.ItemCreate, db: Session = Depends(get_db)
):
    return crud.create_user_item(db=db, item=item, user_id=user_id)

@router.put("/users/{user_id}/items/", response_model=schemas.Item)
def update_item(user_id: int, item_id: int, item: schemas.ItemUpdate, db: Session = Depends(get_db), 
                current_user: schemas.User = Security(get_current_active_user)):
    
    #Only allow editing of own user data.
    if current_user.id != user_id:
        raise HTTPException(status_code=403, detail="Not authorized to access other user's information")
    
    db_user = crud.get_user(db, user_id=user_id)
    if not db_user:
        raise HTTPException(status_code=404, detail="User not found")
    
    return crud.update_item(db=db, item_id=item_id, item=item)

@router.delete("/users/{user_id}/items/", response_model=schemas.Item)
def delete_item(user_id: int, item_id:int, db: Session = Depends(get_db), 
                current_user: schemas.User = Security(get_current_active_user)):
    
    #Only allow editing of own user data.
    if current_user.id != user_id:
        raise HTTPException(status_code=403, detail="Not authorized to access other user's information")

    db_user = crud.get_user(db, user_id=user_id)
    if not db_user:
        raise HTTPException(status_code=404, detail="User not found")
    
    crud.delete_item(db=db, item_id=item_id)
    return Response(status_code=status.HTTP_204_NO_CONTENT)