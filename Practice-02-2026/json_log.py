import logging
import json

logging.basicConfig(filename="log-files/structured.log", level=logging.INFO)

def log_event(event_type, user_id, status):
    log_data = {
        "event": event_type,
        "user_id": user_id,
        "status": status
    }
    logging.info(json.dumps(log_data))

log_event("ORDER_PLACED", 101, "SUCCESS")