from pydantic import BaseModel

# User schemas
class UserCreate(BaseModel):
    name: str
    email: str
    phoneNumber: str
    location: str
    paymentMethod: str
    password: str

class UserOut(BaseModel):
    userID: int
    name: str
    email: str
    phoneNumber: str
    location: str
    paymentMethod: str

class Car(Base):
    __tablename__ = "cars"
    id = Column(Integer, primary_key=True, index=True)
    vin = Column(String, unique=True)
    location = Column(String)
    available = Column(Boolean, default=True)