from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from .database import Base, engine, get_db
from .models import VehicleType, Vehicle, Booking

# Create tables if they don't exist
Base.metadata.create_all(bind=engine)

app = FastAPI(title="Vehicle Rental API")

# ------------------ VEHICLE TYPES ------------------
@app.get("/vehicle-types")
def get_vehicle_types(db: Session = Depends(get_db)):
    types = db.query(VehicleType).all()
    return types

@app.get("/vehicle-types/{type_id}")
def get_vehicle_type(type_id: int, db: Session = Depends(get_db)):
    vtype = db.query(VehicleType).filter(VehicleType.id == type_id).first()
    if not vtype:
        raise HTTPException(status_code=404, detail="Vehicle type not found")
    return vtype

# ------------------ VEHICLES ------------------
@app.get("/vehicles")
def get_vehicles(db: Session = Depends(get_db)):
    vehicles = db.query(Vehicle).all()
    return vehicles

@app.get("/vehicles/{vehicle_id}")
def get_vehicle(vehicle_id: int, db: Session = Depends(get_db)):
    vehicle = db.query(Vehicle).filter(Vehicle.id == vehicle_id).first()
    if not vehicle:
        raise HTTPException(status_code=404, detail="Vehicle not found")
    return vehicle

# ------------------ BOOKINGS ------------------
@app.get("/bookings")
def get_bookings(db: Session = Depends(get_db)):
    bookings = db.query(Booking).all()
    return bookings

@app.get("/bookings/{booking_id}")
def get_booking(booking_id: int, db: Session = Depends(get_db)):
    booking = db.query(Booking).filter(Booking.id == booking_id).first()
    if not booking:
        raise HTTPException(status_code=404, detail="Booking not found")
    return booking

# Root endpoint
@app.get("/")
def root():
    return {"message": "Vehicle Rental API is running"}
