from sqlalchemy import column, integer, string, ForeignKey
from sqlachemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Review(Base):
    __tablename__ = 'reviews'
    id = Column(Integer, primary_key=True)
    star_rating = Column(Integer)
    restaurant_id = Column(Integer, ForeignKey('restaurants.id'))
    customer_id = Column(Integer, ForeignKey('customers.id'))
    
    # Relationship to Restaurant
    restaurant = relationship('Restaurant', back_populates='reviews')
    
    # Relationship to Customer
    customer = relationship('Customer', back_populates='reviews')