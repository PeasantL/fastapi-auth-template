from sqlalchemy.orm import Session

from .. import models, schemas


def get_item(db: Session, item_id):
    return db.query(models.Item).filter(models.Item.id == item_id).first()

def get_items_all(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Item).offset(skip).limit(limit).all()

def get_user_items(db: Session, owner_id: int):
    return db.query(models.Item).filter(models.Item.owner_id == owner_id).all()

def create_user_item(db: Session, item: schemas.ItemCreate, user_id: int):
    db_item = models.Item(**item.dict(), owner_id=user_id)
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item

def update_item(db: Session, item_id: int, item: schemas.ItemUpdate):
    db_item = get_item(item_id)
    if db_item:
        if item.title is not None:
            db_item.title = item.title
        if item.description is not None:
            db_item.description = item.description
        if item.owner_id is not None:
            db_item.owner_id = item.owner_id
    db.commit()
    return db_item

def delete_item(db: Session, item_id: int):
    db_item = get_item(item_id)
    if db_item:
        db.delete(db_item)
        db.commit()  


"""
#Redundant, handled through SQLAlchemy cascading deletes

def delete_all_user_items(db: Session, owner_id: int):
    db.query(models.Item).filter(models.Item.owner_id == owner_id).delete()
    db.commit()
"""   