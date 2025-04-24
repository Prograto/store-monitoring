from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from app.database import Base, engine, SessionLocal
from app.report import trigger_report, generate_report
from app.models import ReportStatus
import threading

Base.metadata.create_all(bind=engine)
app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/trigger_report")
def trigger(db: Session = Depends(get_db)):
    report_id = trigger_report(db)
    threading.Thread(target=generate_report, args=(report_id, db)).start()
    return {"report_id": report_id}

@app.get("/get_report")
def get_report(report_id: str, db: Session = Depends(get_db)):
    report = db.query(ReportStatus).filter(ReportStatus.id == report_id).first()
    if not report:
        return {"error": "Invalid report ID"}
    if report.status != "Complete":
        return {"status": "Running"}
    return {
        "status": "Complete",
        "csv": open(report.filepath).read()
    }
