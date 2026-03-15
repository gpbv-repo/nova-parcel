from fastapi import FastAPI, Depends
from typing import List
from sqlalchemy.orm import Session
from .database import SessionLocal
from . import models, schemas

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# READ operations for Customer
@app.get("/customers", response_model=List[schemas.CustomerRead], status_code=200)
def read_customers(db: Session = Depends(get_db)):
    return db.query(models.Customer).all()

# READ operations for Deliveries
@app.get("/deliveries", response_model=List[schemas.DeliveryRead], status_code=200)
def read_deliveries(db: Session = Depends(get_db)):
    return db.query(models.Delivery).all()

# READ operations for Planet
@app.get("/planets", response_model=List[schemas.PlanetRead], status_code=200)
def read_planets(db: Session = Depends(get_db)):
    return db.query(models.Planet).all()

# READ operations for Product
@app.get("/products", response_model=List[schemas.ProductRead], status_code=200)
def read_products(db: Session = Depends(get_db)):
    return db.query(models.Product).all()

# READ operations for VehicleType
@app.get("/vehicle-types", response_model=List[schemas.VehicleTypeRead], status_code=200)
def read_vehicle_types(db: Session = Depends(get_db)):
    return db.query(models.VehicleType).all()

# READ operations for ParcelsSummary
@app.get("/parcels-summaries", response_model=List[schemas.ParcelsSummaryRead], status_code=200)
def read_parcels_summaries(db: Session = Depends(get_db)):
    return db.query(models.ParcelsSummary).all()

# READ operations for ParcelsSummaryMonthly - Read only
@app.get("/parcels-summaries-monthly", response_model=List[schemas.ParcelsSummaryMonthlyRead], status_code=200)
def read_parcels_summaries_monthlys(db: Session = Depends(get_db)):
    return db.query(models.ParcelsSummaryMonthly).all()

