from pydantic import BaseModel

class CustomerBase(BaseModel):
    customerName: str
    customerEmail: str
    customerPhone: str
    customerAddress: str

class CustomerCreate(CustomerBase):
    pass

class Customer(CustomerBase):
    customerID: int

    class Config:
        orm_mode = True