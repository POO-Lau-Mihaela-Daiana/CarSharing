from fastapi import FastAPI, HTTPException, Depends
from schemas import UserCreate, UserOut
from crud import create_user, get_user_by_email
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Allow requests from frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allow all HTTP methods (GET, POST, etc.)
    allow_headers=["*"],  # Allow all headers
)


@app.post("/register", response_model=UserOut)
def register_user(user: UserCreate):
    existing_user = get_user_by_email(user.email)
    if existing_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    
    return create_user(user.name, user.email, user.phoneNumber, user.location, user.paymentMethod, user.password)


# Login User
@app.post("/login")
def login_user(user: UserCreate):
    db_user = get_user_by_email(user.email)
    if not db_user or not bcrypt.checkpw(user.password.encode(), db_user["password_hash"].encode()):
        raise HTTPException(status_code=401, detail="Invalid email or password")

    token_data = {
        "sub": db_user["email"],
        "exp": datetime.utcnow() + timedelta(hours=2)  # Token expires in 2 hours
    }
    token = jwt.encode(token_data, SECRET_KEY, algorithm=ALGORITHM)

    return {"token": token, "userID": db_user["userID"], "name": db_user["name"], "email": db_user["email"]}
