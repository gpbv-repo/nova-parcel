from typing import Optional
from pydantic import BaseModel


class CustomerRead(BaseModel):
    id: int
    name: str 
    email: str
    country_id: int
    premium_customer: str

    class Config:
        orm_mode = True

class DeliveryRead(BaseModel):
    id: int
    name: str 
    description: str 
    product_id: int
    customer_id: int
    delivery_date: str

    class Config:
        orm_mode = True


class PlanetRead(BaseModel):
    id: int
    name: str 
    region: str

    class Config:
        orm_mode = True

class ProductRead(BaseModel):
    id: int
    reference: str 
    name: str 
    vehicle_type_id: int
    price: str

    class Config:
        orm_mode = True

class VehicleTypeRead(BaseModel):
    id: int
    name: str 
    cost: float

    class Config:
        orm_mode = True

class ParcelsSummaryRead(BaseModel):
    delivery_id: int
    delivery_date: str
    product_id: int
    customer_id: int
    country_id: int
    product_name: str
    product_price: float
    vehicle_type_id: int
    vehicle_cost: float
    region: str
    load_date: str
    process_name: str
    user_id: str

    class Config:
        orm_mode = True


class ParcelsSummaryMonthlyRead(BaseModel):
    yyyymm: str
    product_name: str
    parcel_count: int
    region: str
    profit: float

    class Config:
        orm_mode = True


