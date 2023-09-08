from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from sqlalchemy.orm import sessionmaker
from restaurant import Restaurant
from customer import Customer
from review import Review

engine = create_engine('sqlite:///restaurant.db')
Session = sessionmaker(bind=engine)
session = Session()

def setup_module(module):
    Base.metadata.create_all(engine)
    restaurant = Restaurant(name='Test Restaurant', price=50)
    customer = Customer(first_name='Test', last_name='Customer')
    review = Review(star_rating=5, restaurant=restaurant, customer=customer)
    session.add(restaurant)
    session.add(customer)
    session.add(review)
    session.commit()
    
def test_full_name():
    customer = session.query(Customer).first()
    assert customer.full_name() == 'Test Customer'
    
def teardown_module(module):
    Base.metadata.drop_all(engine)