class Customer(Base):
    __tablename__ = 'customers'
    id = Column(Integer, primary_key=True)
    first_name = Column(String)
    last_name = Column(String)
    
    # Relationship to Review
    reviews = relationship('Review', back_populates='customer')