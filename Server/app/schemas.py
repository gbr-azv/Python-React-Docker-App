from uuid import UUID
from datetime import datetime
from typing import Optional, List
from pydantic import BaseModel, EmailStr

'''This file defines a series of models using Pydantic, which are used to validate 
and document the data entering and leaving the FastAPI application'''

############################## ORDER ##############################

class OrderSend(BaseModel):
    Products: dict[int, int]

class MenuResponse(BaseModel):
    name: str
    description: str
    price: float
    product_id: int

class OrderDetails(BaseModel):
    name: str
    quantity: int
    subtotal: float
    
class OrderResponse(BaseModel):
    purchase_id: UUID
    purchase_date: datetime
    status: str
    items: List[OrderDetails]
    
############################## USER ##############################
    
class UserCreate(BaseModel):
    name: str
    email: EmailStr
    password: str
    phone: str
    address: str
    
class UserUpdate(BaseModel):
    name: str
    email: EmailStr
    phone: str
    address: str

class UserResponse(BaseModel):
    customer_id: UUID
    email: str
    created_at: datetime

class UserDetails(BaseModel):
    customer_id: UUID
    name: str
    email: str
    phone: str
    address: str
    created_at: datetime
    
class UserLogin(BaseModel):
    email: EmailStr # Checks if it is really an email
    password: str

############################## TOKEN ##############################

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    id: Optional[str] = None