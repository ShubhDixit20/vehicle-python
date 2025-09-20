from sqlalchemy import Column, Integer, String, ForeignKey
from . import Base

class Vehicle(Base):
    __tablename__ = "vehicles"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    vehicle_type_id = Column(Integer, ForeignKey("VehicleTypes.id"))
