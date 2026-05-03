from sqlalchemy import Column, Integer, String, ForeignKey
from api.dependencies.database import Base

class Review(Base):
    __tablename__ = "review"

    reviewID = Column(Integer, primary_key=True, index=True)
    reviewText = Column(String)
    reviewScore = Column(Integer, nullable=False)
    customerID = Column(Integer, ForeignKey("customer.customerID"))