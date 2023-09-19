from config import selected_stock
import pandas as pd
import datetime

data = None #data would be data of selected stock
df = pd.read_csv(data)


def string_to_datetime(s):
    split = s.split('-')
    year, month, day = int(split[0]), int(split[1]), int(split[2])
    return datetime.datetime(year=year, month=month, day=day)

#testting

datetime_object = None..

#https://www.youtube.com/watch?v=CbTU92pbDKw   3:45