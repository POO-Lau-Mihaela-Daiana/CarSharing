import bcrypt
from database import get_db_connection

# Function to create a new user
def create_user(email: str, password: str):
    connection = get_db_connection()
    cursor = connection.cursor(dictionary=True)

    # Hash password
    hashed_password = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()

    query = "INSERT INTO users (email, password_hash) VALUES (%s, %s)"
    cursor.execute(query, (email, hashed_password))
    connection.commit()

    user_id = cursor.lastrowid
    cursor.close()
    connection.close()

    return {"id": user_id, "email": email}

# Function to get user by email
def get_user_by_email(email: str):
    connection = get_db_connection()
    cursor = connection.cursor(dictionary=True)

    query = "SELECT id, email FROM users WHERE email = %s"
    cursor.execute(query, (email,))
    user = cursor.fetchone()

    cursor.close()
    connection.close()

    return user

# Function to create a car
def create_car(vin: str, location: str):
    connection = get_db_connection()
    cursor = connection.cursor(dictionary=True)

    query = "INSERT INTO cars (vin, location, available) VALUES (%s, %s, %s)"
    cursor.execute(query, (vin, location, True))
    connection.commit()

    car_id = cursor.lastrowid
    cursor.close()
    connection.close()

    return {"id": car_id, "vin": vin, "location": location, "available": True}

# Function to get car by VIN
def get_car_by_vin(vin: str):
    connection = get_db_connection()
    cursor = connection.cursor(dictionary=True)

    query = "SELECT * FROM cars WHERE vin = %s"
    cursor.execute(query, (vin,))
    car = cursor.fetchone()

    cursor.close()
    connection.close()

    return car

# Function to get available cars by location
def get_available_cars(location: str):
    connection = get_db_connection()
    cursor = connection.cursor(dictionary=True)

    query = "SELECT * FROM cars WHERE location = %s AND available = TRUE"
    cursor.execute(query, (location,))
    cars = cursor.fetchall()

    cursor.close()
    connection.close()

    return cars

# Function to update car availability
def update_car_availability(car_id: int, available: bool):
    connection = get_db_connection()
    cursor = connection.cursor(dictionary=True)

    query = "UPDATE cars SET available = %s WHERE id = %s"
    cursor.execute(query, (available, car_id))
    connection.commit()

    cursor.close()
    connection.close()

    return {"id": car_id, "available": available}
