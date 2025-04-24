# Store Uptime Monitoring API

This project provides a backend API for tracking restaurant store uptime and downtime during business hours. It allows restaurant owners to generate reports on their store's operational status, with uptime and downtime data extrapolated from periodic polling.

# Problem Overview

Loop monitors several restaurants in the US to check if the stores are online during business hours. The goal is to provide a report on the store's uptime and downtime over the past hour, day, and week.

### Data Sources
1. store_status.csv: Contains hourly polling data for store status (`store_id`, `timestamp_utc`, `status`).
2. menu_hours.csv: Defines the business hours for each store (`store_id`, `dayOfWeek`, `start_time_local`, `end_time_local`).
3. timezones.csv: Specifies the timezone for each store (`store_id`, `timezone_str`).


# API Endpoints

# 1. Trigger Report Generation
- POST /trigger_report
    - Triggers the report generation process.
    - Response: Returns a `report_id` to track the report status.
    - Example:
      ```json
      {
        "report_id": "e4a35c6e-8c54-4e9e-bd65-a374df5c1b5a"
      }
      ```

# 2. Get Report Status
- GET /get_report?report_id=<id>
    - Checks the status of the report generation and provides the generated CSV when complete.
    - Response (Running):
      ```json
      {
        "status": "Running"
      }
      ```
    - Response (Complete):
      ```json
      {
        "status": "Complete",
        "csv": "store_id,uptime_last_hour,..."
      }
      ```

---

# Setup

# 1. Clone the repository
```bash
git clone https://github.com/yourusername/store-uptime-monitoring.git
cd store-uptime-monitoring
