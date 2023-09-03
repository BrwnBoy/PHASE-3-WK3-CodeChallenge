from sqlachemy import create_engine
from sqlachemy.orm import Session

engine = create_engine('sqlite:///restaurant.db')
session = sessionmaker(bind=engine)
session = Session(engine)

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
    
def teardowm_module(module):
    Base.metadata.drop_all(engine)