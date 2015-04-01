__author__ = 'root'
from datetime import datetime

date = datetime(2016, 3, 20)
today = datetime(2015, 3, 21)
date3 = datetime(1394, 1, 1)
days = (date-today).days
day = 1
month = 1
year = 1394

while days > 0:
    day += 1
    if month <= 6 and day == 32:
        day = 1
        month += 1

    if 6 < month < 12 and day == 31:
        day = 1
        month += 1

    if day == 30 and month == 12:
        if year % 1391 == 0:
            day += 1
        else:
            day = 1
            month = 1
            year += 1

    if day == 31 and month == 12 and year % 1391 ==0:
        day = 1
        month = 1
        year += 1

    days -= 1


date3 = datetime(year, month, day)
print(date3)