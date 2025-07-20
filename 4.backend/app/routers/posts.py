from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.orm import Session
from .. import database, schemas, models
from .auth import get_current_user
from typing import List

router = APIRouter(
    prefix="/posts",
    tags=['Posts']
)

@router.post("/", status_code=status.HTTP_201_CREATED, response_model=schemas.PostOut)
def create_post(post: schemas.PostCreate, db: Session = Depends(database.get_db), current_user: models.User = Depends(get_current_user)):
    """
    Create a new post or a private note.
    """
    # Create the new post object, linking it to the current user
    new_post = models.Post(author_id=current_user.id, **post.model_dump())
    
    db.add(new_post)
    db.commit()
    db.refresh(new_post)
    
    return new_post

@router.get("/", response_model=List[schemas.PostOut])
def get_posts(db: Session = Depends(database.get_db), current_user: models.User = Depends(get_current_user)):
    """
    Get the feed of posts. For now, it gets all public posts.
    We will add friend logic later.
    """
    # For now, let's just get all public posts to test
    posts = db.query(models.Post).filter(models.Post.is_private == False).order_by(models.Post.created_at.desc()).all()
    return posts

@router.get("/notes", response_model=List[schemas.PostOut])
def get_my_notes(db: Session = Depends(database.get_db), current_user: models.User = Depends(get_current_user)):
    """
    Get all private notes for the currently authenticated user.
    """
    notes = db.query(models.Post).filter(models.Post.author_id == current_user.id, models.Post.is_private == True).order_by(models.Post.created_at.desc()).all()
    return notes

@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_post(id: int, db: Session = Depends(database.get_db), current_user: models.User = Depends(get_current_user)):
    """
    Delete a post.
    """
    post_query = db.query(models.Post).filter(models.Post.id == id)
    post = post_query.first()

    if post is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Post with id: {id} does not exist")

    # Check if the user trying to delete the post is the author
    if post.author_id != current_user.id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Not authorized to perform requested action")
    
    post_query.delete(synchronize_session=False)
    db.commit()
    
    return # No response body for 204