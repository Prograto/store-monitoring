import pytz
from datetime import datetime
from sqlalchemy.orm import Session
from .models import Timezone

def get_store_timezone(db: Session, store_id: int) -> str:
    tz = db.query(Timezone).filter(Timezone.store_id == store_id).first()
    return tz.timezone_str if tz else "America/Chicago"

def utc_to_local(utc_dt: datetime, timezone_str: str):
    tz = pytz.timezone(timezone_str)
    return utc_dt.replace(tzinfo=pytz.utc).astimezone(tz)
