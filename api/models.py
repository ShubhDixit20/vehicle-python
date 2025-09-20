from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from .database import Base

class VehicleType(Base):
    __tablename__ = "vehicle_types"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, nullable=False)
    vehicles = relationship("Vehicle", back_populates="vehicle_type")

class Vehicle(Base):
    __tablename__ = "vehicles"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    vehicle_type_id = Column(Integer, ForeignKey("vehicle_types.id"))
    vehicle_type = relationship("VehicleType", back_populates="vehicles")
    bookings = relationship("Booking", back_populates="vehicle")

class Booking(Base):
    __tablename__ = "bookings"

    id = Column(Integer, primary_key=True, index=True)
    vehicle_id = Column(Integer, ForeignKey("vehicles.id"))
    customer_name = Column(String, nullable=False)
    start_time = Column(DateTime)
    end_time = Column(DateTime)

    vehicle = relationship("Vehicle", back_populates="bookings")
