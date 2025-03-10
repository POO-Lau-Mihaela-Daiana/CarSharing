import bcrypt
from database import get_db_connection

def create_user(name: str, email: str, phoneNumber: str, location: str, paymentMethod: str, password: str):
    connection = get_db_connection()
    cursor = connection.cursor(dictionary=True)

    hashed_password = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()

    query = """
    INSERT INTO users (name, email, phoneNumber, location, paymentMethod, password_hash) 
    VALUES (%s, %s, %s, %s, %s, %s)
    """
    cursor.execute(query, (name, email, phoneNumber, location, paymentMethod, hashed_password))
    connection.commit()

    user_id = cursor.lastrowid
    cursor.close()
    connection.close()

    return {"id": user_id, "name": name, "email": email, "phoneNumber": phoneNumber, "location": location, "paymentMethod": paymentMethod}


# Get user by email
def get_user_by_email(email: str):
    connection = get_db_connection()
    cursor = connection.cursor(dictionary=True)

    query = "SELECT * FROM users WHERE email = %s"
    cursor.execute(query, (email,))
    user = cursor.fetchone()

    cursor.close()
    connection.close()
    
    return user
