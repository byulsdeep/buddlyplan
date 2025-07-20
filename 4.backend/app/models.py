from sqlalchemy import Column, Integer, String, Boolean, text, ForeignKey
from sqlalchemy.orm import relationship # <-- Import relationship
from sqlalchemy.sql.sqltypes import TIMESTAMP
from .database import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    username = Column(String(50), nullable=False, unique=True)
    email = Column(String(255), nullable=False, unique=True)
    hashed_password = Column(String(255), nullable=False)
    display_name = Column(String(100), nullable=True)
    profile_picture_url = Column(String(255), nullable=True)
    is_ai = Column(Boolean, server_default='false', nullable=False)
    created_at = Column(TIMESTAMP(timezone=True), nullable=False, server_default=text('now()'))

    # Define the one-to-many relationship from the User side
    posts = relationship("Post", back_populates="author")

# === ADD THIS NEW MODEL ===
class Post(Base):
    __tablename__ = "posts"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)

    content = Column(String, nullable=False) # Changed to String for now
    is_private = Column(Boolean, server_default='false', nullable=False)

    created_at = Column(TIMESTAMP(timezone=True), nullable=False, server_default=text('now()'))
    # ADD THIS
    updated_at = Column(TIMESTAMP(timezone=True), nullable=True, onupdate=text('now()'))
    
    # Define the foreign key relationship
    author_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"), nullable=False)

    # Define the relationship from the Post side
    author = relationship("User", back_populates="posts")

    # We will add the parent_post_id for comments later