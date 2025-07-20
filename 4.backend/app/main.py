from fastapi import FastAPI, Depends, HTTPException # <--- ADD HTTPException
from sqlalchemy import text  # <--- ADD THIS IMPORT
from sqlalchemy.orm import Session
from .database import get_db, engine, Base # Import Depends, Session, and our new get_db

# This line is important. It tells SQLAlchemy to create all the tables defined
# in your ORM models (we will create those models soon). For now, it won't do much.
# Base.metadata.create_all(bind=engine) 

# Create the FastAPI app instance
app = FastAPI(title="Event Horizon API")


# Define a root endpoint for health checks
@app.get("/")
def read_root():
    """A simple health check endpoint to confirm the API is running."""
    return {"status": "ok", "message": "Welcome to the Event Horizon API!"}

# In a real app, you would import and include your routers here
# from .routers import users, posts, etc.
# app.include_router(users.router)
# app.include_router(posts.router)

# === ADD THIS NEW ENDPOINT ===
@app.get("/db-check")
def database_check(db: Session = Depends(get_db)):
    """
    Performs a simple query to verify the database connection.
    """
    try:
        # Execute a simple, harmless query
        db.execute(text("SELECT 1"))
        # If the above line succeeds, this is returned with a default 200 OK
        return {"status": "ok", "message": "Database connection successful!"}
    except Exception as e:
        # If any exception occurs during the db connection/query
        print(f"Database connection failed: {e}")
        # Raise an HTTPException, which FastAPI will convert into
        # a proper HTTP response with the correct status code.
        raise HTTPException(
            status_code=503, # 503 Service Unavailable is a perfect code for this
            detail="Database connection failed.",
        )