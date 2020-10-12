import calendar
from datetime import datetime

current_month = datetime.now().month
current_year = datetime.now().year

print(calendar.month(current_year,current_month))
