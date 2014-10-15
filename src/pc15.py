import datetime

# 1996 is leap year, and -20 is end with 6 and also leap year
year = [y for y in range(1996,1005,-20) if y % 4 == 0 and datetime.date(y,1,26).weekday() == 0][1]

print '%d-1-27' % year
