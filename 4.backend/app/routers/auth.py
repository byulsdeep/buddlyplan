from fastapi import APIRouter, Depends, status, HTTPException
from fastapi.security import OAuth2PasswordRequestForm, OAuth2PasswordBearer
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from .. import database, schemas, models, config
from ..utils import security # We will create this file next
from datetime import timedelta

# This tells FastAPI what URL to check for the token (our login endpoint)
# This doesn't create the endpoint, it's just metadata for the docs.
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/api/v1/auth/token")

router = APIRouter(
    prefix="/auth",
    tags=['Authentication']
)

@router.post("/register", status_code=status.HTTP_201_CREATED, response_model=schemas.UserOut)
def register_user(user: schemas.UserCreate, db: Session = Depends(database.get_db)): # This is FastAPI's Dependency Injection system
    
    # Hash the incoming plain-text password
    hashed_password = security.hash_password(user.password)
    user_data = user.model_dump(exclude={"password"})
    new_user = models.User(**user_data)
    new_user.hashed_password = hashed_password

    # Add to the database and handle potential conflicts
    try:
        db.add(new_user)
        db.commit()
        db.refresh(new_user)
    except IntegrityError:
        db.rollback() # Good practice to rollback the failed transaction
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="Account already exists with this email or username."
        )
    return new_user

# === ADD THIS NEW LOGIN ENDPOINT ===

@router.post("/token", response_model=schemas.Token)
def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(database.get_db)): # OAuth2PasswordRequestForm application/x-www-form-urlencoded
    # 1. Find the user by their username (email in our case)
    user = db.query(models.User).filter(models.User.email == form_data.username).first()

    # 2. Check if user exists and password is correct
    if not user or not security.verify_password(form_data.password, user.hashed_password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect email or password",
            headers={"WWW-Authenticate": "Bearer"},
        )

    # 3. Create access token
    access_token_expires = timedelta(minutes=config.settings.ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = security.create_access_token(
        data={"sub": str(user.id)}, expires_delta=access_token_expires
    )

    # 4. Create refresh token
    refresh_token = security.create_refresh_token(data={"sub": str(user.id)})

    return {"access_token": access_token, "refresh_token": refresh_token, "token_type": "bearer"}

def get_current_user(token: str = Depends(oauth2_scheme), db: Session = Depends(database.get_db)):
    
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    
    # Verify the token to get the user ID
    token_data = security.verify_token(token, credentials_exception)
    
    # Fetch the user from the database
    user = db.query(models.User).filter(models.User.id == token_data.id).first()
    
    if user is None:
        raise credentials_exception
        
    return user