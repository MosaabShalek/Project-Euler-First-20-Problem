import datetime as dt

# - Test for 2019 which has two sundays as the first days of the month, in december & September
for month in range(1, 13):
    day = dt.date(2019, month, 1)
    if day.weekday() == 6: print("^_^")

# - Actual solution to problem 19
counter = 0
for year in range(1901, 2001) :
    for month in range(1, 13):
        day = dt.date(year, month, 1)
        if day.weekday() == 6:
            counter += 1
print(counter)
