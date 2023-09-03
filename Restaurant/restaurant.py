class Restaurant(Base):
    __tablename__ = 'restaurants'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    price = Column(Integer)
    
    # Relationship to Review
    reviews = relationship('Review', back_populates='restaurant')