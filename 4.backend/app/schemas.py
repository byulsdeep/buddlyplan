from pydantic import BaseModel, EmailStr
from datetime import datetime

# --- User Schemas ---

# Properties to receive via API on user creation
class UserCreate(BaseModel):
    username: str
    email: EmailStr
    password: str

# Properties to return to a client (never include the password!)
class UserOut(BaseModel):
    id: int
    username: str
    email: EmailStr
    display_name: str | None = None
    profile_picture_url: str | None = None
    created_at: datetime

    class Config:
        # This tells Pydantic to read the data even if it is not a dict,
        # but an ORM model (or any other arbitrary object with attributes).
        # UserOut is the only one that receives a SQLAlchemy ORM object as its input,
        # so it's the only one that needs to be told how to read from it.
        from_attributes = True

# --- Token Schemas ---

class Token(BaseModel):
    access_token: str
    refresh_token: str
    token_type: str

class TokenData(BaseModel):
    id: int | None = None