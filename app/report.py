import pandas as pd
import uuid
from datetime import datetime, timedelta
from sqlalchemy.orm import Session
from .models import StoreStatus, MenuHours, ReportStatus
from .utils import utc_to_local, get_store_timezone

def trigger_report(db: Session) -> str:
    report_id = str(uuid.uuid4())
    report = ReportStatus(id=report_id, status="Running")
    db.add(report)
    db.commit()
    return report_id

def generate_report(report_id: str, db: Session):
    now = db.query(StoreStatus).order_by(StoreStatus.timestamp_utc.desc()).first().timestamp_utc
    start = now - timedelta(weeks=1)

    statuses = pd.read_sql(db.query(StoreStatus).filter(StoreStatus.timestamp_utc >= start).statement, db.bind)
    hours = pd.read_sql(db.query(MenuHours).statement, db.bind)
    tzs = pd.read_sql(db.query(Timezone).statement, db.bind)

    report_df = pd.DataFrame({
        "store_id": [1],
        "uptime_last_hour": [30],
        "uptime_last_day": [12],
        "update_last_week": [80],
        "downtime_last_hour": [30],
        "downtime_last_day": [12],
        "downtime_last_week": [88],
    })

    filepath = f"report_{report_id}.csv"
    report_df.to_csv(filepath, index=False)

    db.query(ReportStatus).filter(ReportStatus.id == report_id).update({
        "status": "Complete",
        "filepath": filepath
    })
    db.commit()
