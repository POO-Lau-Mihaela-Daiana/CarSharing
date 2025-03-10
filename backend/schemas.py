from pydantic import BaseModel

class UserCreate(BaseModel):
    name: str
    email: str
    phoneNumber: str
    location: str
    paymentMethod: str
    password: str

class UserOut(BaseModel):
    id: int
    name: str
    email: str
    phoneNumber: str
    location: str
    paymentMethod: str
