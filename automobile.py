
from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Automobile(Base):
    __tablename__ = "automobiles"

    id = Column(Integer, primary_key=True, index=True)
    brand = Column(String, index=True)
    model = Column(String, index=True)
    year = Column(Integer)
    color = Column(String)
    mileage = Column(Integer)
    price = Column(Float)
    fuel_type = Column(String)
    transmission = Column(String)
    engine_size = Column(Float)
    num_doors = Column(Integer)
    plate = Column(String, unique=True, index=True)

    def __repr__(self):
        return f"<Automobile(brand='{self.brand}', model='{self.model}', year={self.year})>"


