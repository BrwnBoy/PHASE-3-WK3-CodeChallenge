from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class Customer(Base):
    __tablename__ = 'customers'
    id = Column(Integer, primary_key=True)
    first_name = Column(String)
    last_name = Column(String)
    
    # Relationship to Review
    reviews = relationship('Review', back_populates='customer')
    
    def full_name(self):
        return f"{self.first_name} {self.last_name}"