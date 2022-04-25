from khayyam import algorithms_pure as a
from datetime import datetime, timedelta

cc = datetime(622,3,22)
while True:
  jd = a.get_julian_day_from_gregorian_date(cc.year, cc.month, cc.day)
  year, month, day = a.get_jalali_date_from_julian_day(jd)
  if year == 3178:
    break
  print(f'{cc.year}-{cc.month}-{cc.day},{year}-{month}-{int(day)}')
  cc += timedelta(days=1)
