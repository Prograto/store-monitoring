import pandas as pd
from sqlalchemy import create_engine
from app.database import Base, engine
from app.models import StoreStatus, MenuHours, Timezone

Base.metadata.create_all(bind=engine)

conn = create_engine("sqlite:///./stores.db")

pd.read_csv("data/store_status.csv").to_sql("store_status", conn, if_exists="replace", index=False)
pd.read_csv("data/menu_hours.csv").to_sql("menu_hours", conn, if_exists="replace", index=False)
pd.read_csv("data/timezones.csv").to_sql("timezones", conn, if_exists="replace", index=False)

print("✅ Data loaded successfully!")
