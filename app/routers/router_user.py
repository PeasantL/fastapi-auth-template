from fastapi import Depends, APIRouter, HTTPException, Security, Response, status
from sqlalchemy.orm import Session

from .. import crud, schemas
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

@router.post("/users/", response_model=schemas.User)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    db_user = crud.get_user_by_username(db, username=user.username)
    if db_user:
        raise HTTPException(status_code=400, detail="Username already registered")
    return crud.create_user(db=db, user=user)

@router.get("/users", response_model=list[schemas.User])
def read_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    users = crud.get_users(db, skip=skip, limit=limit)
    return users

"""
# Unnecessary Endpoint
@router.get("/users/{user_id}", response_model=schemas.User)
def read_user(user_id: int, db: Session = Depends(get_db)):
    db_user = crud.get_user(db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user
"""

@router.put("/users/me", response_model=schemas.User)
def update_user(user: schemas.UserUpdate, db: Session = Depends(get_db), 
                current_user: schemas.User = Security(get_current_active_user)):
    
    db_user = crud.get_user(db, user_id=current_user.id)
    if not db_user:
        raise HTTPException(status_code=404, detail="User not found")
    
    return crud.update_user(db=db, user_id=current_user.id, user=user)

@router.delete("/users/me", status_code=status.HTTP_204_NO_CONTENT)
def delete_user(db: Session = Depends(get_db), 
                current_user: schemas.User = Security(get_current_active_user)):
    
    db_user = crud.get_user(db, user_id=current_user.id)
    if not db_user:
        raise HTTPException(status_code=404, detail="User not found")
    
    # Handling of the items associated with user on termination are done through 
    # cascading deletesfrom SQLAlchemy
    crud.delete_user(db=db, user_id=current_user.id)
    return Response(status_code=status.HTTP_204_NO_CONTENT)
