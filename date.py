import calendar
from datetime import datetime

current_month = datetime.now().month
current_year = datetime.now().year

html_cal= calendar.HTMLCalendar(calendar.MONDAY)
str = html_cal.formatmonth(current_year,current_month)
print(str)
