from sqlalchemy import Column, Integer, String, DateTime, Enum, Time
from .database import Base

class StoreStatus(Base):
    __tablename__ = "store_status"
    id = Column(Integer, primary_key=True, index=True)
    store_id = Column(Integer, index=True)
    timestamp_utc = Column(DateTime)
    status = Column(String)

class MenuHours(Base):
    __tablename__ = "menu_hours"
    id = Column(Integer, primary_key=True, index=True)
    store_id = Column(Integer)
    day_of_week = Column(Integer)
    start_time_local = Column(Time)
    end_time_local = Column(Time)

class Timezone(Base):
    __tablename__ = "timezones"
    id = Column(Integer, primary_key=True, index=True)
    store_id = Column(Integer)
    timezone_str = Column(String)

class ReportStatus(Base):
    __tablename__ = "report_status"
    id = Column(String, primary_key=True)
    status = Column(String)
    filepath = Column(String, nullable=True)
