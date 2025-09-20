from sqlalchemy import Column, Integer, String
from . import Base

class VehicleType(Base):
    __tablename__ = "VehicleTypes"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
