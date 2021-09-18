import datetime

def get_before_day(before:int, format:str) -> str:
    return ( datetime.datetime.now() - datetime.timedelta(before) ).strftime(format)