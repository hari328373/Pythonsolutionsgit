import calendar
month, day, year = map(int, input().split())
k=calendar.day_name[calendar.weekday(year, month, day)].upper()
print(k)

