from sqlalchemy import Column, Integer, String, ForeignKey, Date
from . import Base

class Booking(Base):
    __tablename__ = "Bookings"
    id = Column(Integer, primary_key=True, index=True)
    vehicle_id = Column(Integer, ForeignKey("Vehicles.id"))
    customer_name = Column(String, nullable=False)
    start_date = Column(Date)
    end_date = Column(Date)
