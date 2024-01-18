import calendar
import pprint

# cal = calendar.month(2024, 1)

# print(cal)
# print(type(cal))

cal = calendar.month(2024, 1, w=5, l=5)
print(cal)

cal_month = calendar.prmonth(2023, 1)
print(cal_month)

cal_out = calendar.calendar(2024, c=5, m=2)
print(cal_out)

calendar.setfirstweekday(calendar.SATURDAY)

print(calendar.month(2024, 1))

ltc_fr = calendar.LocaleTextCalendar(locale='fr_FR')

print(ltc_fr.formatmonth(2024, 1))

html_cal = calendar.HTMLCalendar()
print(html_cal.formatmonth(2024, 1, withyear=False))

print(html_cal.formatyear(2024, width=5))

print(html_cal.cssclasses)
html_cal.cssclasses = ['manic_monday', 'ruby_tuesday', 'wed', 'thu', 'fri', 'sat', 'sun']
print(html_cal.cssclasses)

html_cal_day = calendar.HTMLCalendar(firstweekday=5)
print(html_cal_day.formatmonth(2024, 1))

pprint.pprint(calendar.monthcalendar(2023,1))
calendar.setfirstweekday(5)
pprint.pprint(calendar.monthcalendar(2023,1))

caldr = calendar.Calendar(firstweekday=5)
pprint.pprint(caldr.monthdayscalendar(2024, 1))

pprint.pprint(caldr.yeardayscalendar(2024), depth=3)
pprint.pprint(caldr.yeardayscalendar(2024, width=5,), depth=5)

pprint.pprint(caldr.monthdays2calendar(2024, 1))
pprint.pprint(caldr.monthdatescalendar(2024, 1))