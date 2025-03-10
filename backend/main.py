from fastapi import FastAPI, HTTPException, Depends
from schemas import UserCreate, UserOut
from crud import create_user, get_user_by_email
from database import SessionLocal
from sqlalchemy.orm import Session
import jwt
import bcrypt
from datetime import datetime, timedelta

app = FastAPI()

SECRET_KEY = "your_secret_key"
ALGORITHM = "HS256"

# Database Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Register User
@app.post("/register", response_model=UserOut)
def register_user(user: UserCreate, db: Session = Depends(get_db)):
    existing_user = get_user_by_email(db, user.email)
    if existing_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    return create_user(db, user.email, user.password)

# Login User
@app.post("/login")
def login_user(user: UserCreate, db: Session = Depends(get_db)):
    db_user = get_user_by_email(db, user.email)
    if not db_user or not bcrypt.checkpw(user.password.encode(), db_user.password_hash.encode()):
        raise HTTPException(status_code=401, detail="Invalid email or password")

    token_data = {
        "sub": db_user.email,
        "exp": datetime.utcnow() + timedelta(hours=2)  # Token expires in 2 hours
    }
    token = jwt.encode(token_data, SECRET_KEY, algorithm=ALGORITHM)
    
    return {"token": token}
