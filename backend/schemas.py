from pydantic import BaseModel

# User schemas
class UserCreate(BaseModel):
    email: str
    password: str

class UserOut(BaseModel):
    id: int
    email: str

# Car schemas
class CarCreate(BaseModel):
    vin: str
    location: str

class CarOut(BaseModel):
    id: int
    vin: str
    location: str
    available: bool

class CarAvailability(BaseModel):
    available: bool
