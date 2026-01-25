import pandas as pd
from sqlalchemy import create_engine

df = pd.read_parquet("green_tripdata_2025-11.parquet")

engine = create_engine(
    "postgresql://postgres:postgres@localhost:5433/ny_taxi"
)

df.to_sql(
    "green_tripdata_2025_11",
    engine,
    if_exists="replace",
    index=False
)

print("Row Count:", len(df))