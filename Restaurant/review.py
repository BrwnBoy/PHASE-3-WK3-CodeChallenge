from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import declarative_base

engine = create_engine('sqlite:///restaurant.db')
Session = sessionmaker(bind=engine)
session = Session()

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