import os
from sqlalchemy import create_engine

url = os.getenv('DATABASE_URL') or 'postgresql://postgres:admin@localhost:5432/nova_parcel'
print('DATABASE_URL:', url)

engine = create_engine(url)
import sqlalchemy
print('SQLAlchemy version', sqlalchemy.__version__)

with engine.connect() as conn:
    version = conn.execute('SELECT version()').fetchone()[0]
    print('Postgres version:', version)
    cust = conn.execute("SELECT to_regclass('public.customer')").fetchone()[0]
    print('customer table exists:', cust)
