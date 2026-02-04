from typing import Iterator
from sqlalchemy import create_engine, Engine

__POSTGRES_URL = (
    f"postgresql+psycopg://"
    f"developer:secretpassword"
    f"@localhost:5432"
    f"/ecommerce_db"
)

engine = create_engine(__POSTGRES_URL, echo=True)



