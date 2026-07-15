from datetime import datetime, timedelta

def due_date(days=14):
    return datetime.now() + timedelta(days=days)
