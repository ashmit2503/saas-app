import datetime

def timestamp_as_datetime(timestamp):
    if timestamp is None:
        return None
    return datetime.datetime.fromtimestamp(timestamp, tz=datetime.timezone.utc)