from datetime import datetime

cur_date = datetime.now()

def datetime_from_string(date: str) -> datetime:
    return datetime.strptime(date, '%Y-%m-%d')

def check_valid_date(date: str) -> bool:
    return datetime_from_string(date) >= cur_date
