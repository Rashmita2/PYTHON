import calendar
print(calendar.weekheader(3))
print()
print(calendar.firstweekday())
print()
print(calendar.month(2019,4))
print()
print(calendar.calendar(2021))

day_week = calendar.weekday(2021,3,9)
print(day_week)
print()
is_leap = calendar.isleap(2020)
print(is_leap)