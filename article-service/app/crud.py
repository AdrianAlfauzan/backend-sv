from sqlalchemy.orm import Session
from app import models, schemas
from fastapi import HTTPException, status

def create_post(db: Session, post: schemas.PostCreate):
    db_post = models.Post(
        Title=post.title,
        Content=post.content,
        Category=post.category,
        Status=post.status.value if hasattr(post.status, 'value') else post.status
    )
    db.add(db_post)
    db.commit()
    db.refresh(db_post)
    return db_post

def get_posts(db: Session, limit: int = 10, offset: int = 0):
    return db.query(models.Post).offset(offset).limit(limit).all()

def get_post(db: Session, post_id: int):
    db_post = db.query(models.Post).filter(models.Post.id == post_id).first()
    if not db_post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Post not found")
    return db_post

def update_post(db: Session, post_id: int, post_update: schemas.PostUpdate):
    db_post = get_post(db, post_id)
    update_data = post_update.model_dump(exclude_unset=True)
    
    if "title" in update_data:
        db_post.Title = update_data["title"]
    if "content" in update_data:
        db_post.Content = update_data["content"]
    if "category" in update_data:
        db_post.Category = update_data["category"]
    if "status" in update_data:
        db_post.Status = update_data["status"].value if hasattr(update_data["status"], 'value') else update_data["status"]
    
    db.commit()
    db.refresh(db_post)
    return db_post

def delete_post(db: Session, post_id: int):
    db_post = get_post(db, post_id)
    db.delete(db_post)
    db.commit()
    return {"message": f"Artikel dengan ID {post_id} berhasil dihapus"}