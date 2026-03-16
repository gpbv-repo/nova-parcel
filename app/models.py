from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class Customer(Base):
    __tablename__ = "customer"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    email = Column(String)
    country_id = Column(Integer)
    premium_customer = Column(String)


class Delivery(Base):
    __tablename__ = "delivery"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    description = Column(String)
    product_id = Column(Integer)
    customer_id = Column(Integer)
    delivery_date = Column(String)


class Planet(Base):
    __tablename__ = "planet"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    region = Column(String)

class Product(Base):
    __tablename__ = "product"

    id = Column(Integer, primary_key=True)
    reference = Column(String)
    name = Column(String)
    vehicle_type_id = Column(Integer)
    price = Column(String)

class VehicleType(Base):
    __tablename__ = "vehicle_type"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    cost = Column(Float)

class ParcelsSummary(Base):
    __tablename__ = "parcels_summary"

    delivery_id = Column(Integer, primary_key=True)
    delivery_date = Column(String)
    product_id = Column(Integer)
    customer_id = Column(Integer)
    country_id = Column(Integer)
    product_name = Column(String)
    product_price = Column(Float)
    vehicle_type_id = Column(Integer)
    vehicle_cost = Column(Float)
    region = Column(String)
    load_date = Column(String)
    process_name = Column(String)
    user_id = Column(String)

class ParcelsSummaryMonthly(Base):
    __tablename__ = "parcels_summary_monthly"

    yyyymm = Column(String)
    product_name = Column(String)
    parcel_count = Column(Integer)
    region = Column(String)
    profit = Column(Float)
