from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import mysql.connector
from threading import Thread
import jwt
import datetime
import uuid


# Database Connection
def get_db_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="carsharing_db"
    )


# JWT Setup
SECRET_KEY = "supersecretkey"

def create_jwt(user_id: str):
    payload = {"user_id": user_id, "exp": datetime.datetime.utcnow() + datetime.timedelta(hours=1)}
    return jwt.encode(payload, SECRET_KEY, algorithm="HS256")


# FastAPI App
app = FastAPI()


class RegisterModel(BaseModel):
    name: str
    email: str
    phoneNumber: str
    password: str


def register_user_thread(user):
    db = get_db_connection()
    cursor = db.cursor()
    cursor.execute("SELECT email FROM Client WHERE email = %s", (user.email,))
    if cursor.fetchone():
        cursor.close()
        db.close()
        return  # Exit if email already exists

    user_id = str(uuid.uuid4())
    cursor.execute("INSERT INTO Client (userID, name, email, phoneNumber, passwordHash) VALUES (%s, %s, %s, %s, %s)",
                   (user_id, user.name, user.email, user.phoneNumber, user.password))
    db.commit()
    cursor.close()
    db.close()


@app.post("/register")
def register(user: RegisterModel):
    thread = Thread(target=register_user_thread, args=(user,))
    thread.start()
    return {"message": "User registration is being processed"}


class LoginModel(BaseModel):
    email: str
    password: str


def login_user_thread(user, response_dict):
    db = get_db_connection()
    cursor = db.cursor()
    cursor.execute("SELECT userID, passwordHash FROM Client WHERE email = %s", (user.email,))
    result = cursor.fetchone()
    cursor.close()
    db.close()

    if result:
        stored_password = result[1]
        if stored_password == user.password:  # Ensure passwords match
            response_dict["token"] = create_jwt(result[0])
        else:
            response_dict["error"] = "Invalid credentials"
    else:
        response_dict["error"] = "User not found"



@app.post("/login")
def login(user: LoginModel):
    response_dict = {}
    thread = Thread(target=login_user_thread, args=(user, response_dict))
    thread.start()
    thread.join()  # Wait for thread to complete before returning response

    # Check if login was successful
    if "error" in response_dict:
        raise HTTPException(status_code=401, detail=response_dict["error"])

    if "token" not in response_dict:
        raise HTTPException(status_code=500, detail="Internal server error: Token generation failed")

    return {"token": response_dict["token"]}



@app.get("/cars")
def get_available_cars():
    def fetch_cars(response_dict):
        db = get_db_connection()
        cursor = db.cursor(dictionary=True)
        cursor.execute("SELECT * FROM Car WHERE status = 'available'")
        response_dict["cars"] = cursor.fetchall()
        cursor.close()
        db.close()

    response_dict = {}
    thread = Thread(target=fetch_cars, args=(response_dict,))
    thread.start()
    thread.join()

    return response_dict["cars"]
