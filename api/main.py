from fastapi import FastAPI
from supabase import create_client
import os
from dotenv import load_dotenv

load_dotenv(dotenv_path=os.path.join(os.path.dirname(__file__), ".env"))

SUPABASE_URL = os.environ.get("SUPABASE_URL")
SUPABASE_ANON_KEY = os.environ.get("SUPABASE_ANON_KEY")

print("Supabase URL:", SUPABASE_URL)
print("Supabase Anon Key:", SUPABASE_ANON_KEY)

supabase = create_client(SUPABASE_URL, SUPABASE_ANON_KEY)

app = FastAPI(title="Vehicle Rental API")

@app.get("/")
def root():
    return {"message": "API is running"}

@app.get("/vehicle-types")
def get_vehicle_types():
    data = supabase.table("VehicleTypes").select("*").execute()
    return data.data

@app.get("/vehicles")
def get_vehicles():
    data = supabase.table("Vehicles").select("*").execute()
    return data.data

@app.get("/bookings")
def get_bookings():
    data = supabase.table("Bookings").select("*").execute()
    return data.data
