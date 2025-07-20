from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from .. import database, schemas
from .auth import get_current_user # <-- Import our bouncer!

router = APIRouter(
    prefix="/users",
    tags=['Users']
)

@router.get("/me", response_model=schemas.UserOut)
def get_me(current_user: schemas.UserOut = Depends(get_current_user)):
    """
    Get the profile information for the currently authenticated user.
    """
    # The get_current_user dependency has already done all the work.
    # It validated the token and fetched the user object from the DB.
    # We can just return it directly.
    return current_user