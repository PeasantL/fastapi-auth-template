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

@router.get("/users/me/items", response_model=list[schemas.Item])
def read_items(db: Session = Depends(get_db),
               current_user: schemas.User = Security(get_current_active_user)):
    
    db_user = crud.get_user(db, user_id=current_user.id)
    if not db_user:
        raise HTTPException(status_code=404, detail="User not found")

    items = crud.get_user_items(db, current_user.id)
    return items

@router.post("/users/me/items/", response_model=schemas.Item)
def create_item_for_user(item: schemas.ItemCreate, db: Session = Depends(get_db),
                current_user: schemas.User = Security(get_current_active_user)):
    
    db_user = crud.get_user(db, user_id=current_user.id)
    if not db_user:
        raise HTTPException(status_code=404, detail="User not found")
    
    return crud.create_user_item(db=db, item=item, user_id=current_user.id)

@router.put("/users/me/items/{item_id}", response_model=schemas.Item)
def update_item(item_id: int, item: schemas.ItemUpdate, db: Session = Depends(get_db), 
                current_user: schemas.User = Security(get_current_active_user)):
    
    db_user = crud.get_user(db, user_id=current_user.id)
    if not db_user:
        raise HTTPException(status_code=404, detail="User not found")
    
    db_item = crud.get_item(db, item_id)
    if not db_item:
        raise HTTPException(status_code=404, detail="Item not found")
    if db_item.owner_id != current_user.id:
        raise HTTPException(status_code=403, detail="Not authorized to access other user's items")  
    
    return crud.update_item(db=db, item_id=item_id, item=item)

@router.delete("/users/me/items/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_item(item_id:int, db: Session = Depends(get_db), 
                current_user: schemas.User = Security(get_current_active_user)):
    
    db_user = crud.get_user(db, user_id=current_user.id)
    if not db_user:
        raise HTTPException(status_code=404, detail="User not found")
    
    db_item = crud.get_item(db, item_id)
    if not db_item:
        raise HTTPException(status_code=404, detail="Item not found")
    if db_item.owner_id != current_user.id:
        raise HTTPException(status_code=403, detail="Not authorized to access other user's items")  
    
    crud.delete_item(db=db, item_id=item_id)
    return Response(status_code=status.HTTP_204_NO_CONTENT)