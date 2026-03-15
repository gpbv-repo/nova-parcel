import os
import pytest

# Set database URL from environment with no fallback to SQLite.
# For local Postgres, set it before running tests:
#   setx DATABASE_URL "postgresql://postgres:admin@localhost:5432/mydatabase"
#   OR (PowerShell temporary) $env:DATABASE_URL = "postgresql://postgres:admin@localhost:5432/mydatabase"
# For Unix: export DATABASE_URL="postgresql://postgres:admin@localhost:5432/mydatabase"
if not os.getenv("DATABASE_URL"):
    raise RuntimeError(
        "DATABASE_URL must be set to a Postgres connection for tests, e.g. postgres://postgres:admin@localhost:5432/nova_parcel"
    )

from fastapi.testclient import TestClient
from app.database import engine
from app import models
from app.main import app

@pytest.fixture(scope="module", autouse=True)
def setup_db():
    # migrate/drop and create tables on the configured engine
    models.Base.metadata.drop_all(bind=engine)
    models.Base.metadata.create_all(bind=engine)
    yield
    models.Base.metadata.drop_all(bind=engine)

client = TestClient(app)

@pytest.mark.parametrize("path", [
    "/customers","/deliveries","/planets","/products","/vehicle-types",
    "/parcels-summaries","/parcels-summaries-monthly"
])
def test_read_empty_collections(path):
    r = client.get(path)
    assert r.status_code == 200
    assert r.json() == []