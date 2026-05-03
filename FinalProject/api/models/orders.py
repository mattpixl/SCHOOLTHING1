from sqlalchemy import Column, Integer, String, Float, Date, ForeignKey
from api.dependencies.database import Base

class Orders(Base):
    __tablename__ = "orders"

    orderID = Column(Integer, primary_key=True, index=True)
    orderDate = Column(Date, nullable=False)
    trackingNumber = Column(Integer, unique=True, nullable=False)
    orderStatus = Column(String(15), nullable=False)
    orderPrice = Column(Float, nullable=False)
    orderCustomerID = Column(Integer, ForeignKey("customer.customerID"))