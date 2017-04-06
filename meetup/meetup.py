from datetime import date
import calendar

def meetup_day(year_in, month_in, day_in, date_in):
    daydict = {"Monday": 0, "Tuesday": 1, "Wednesday": 2, "Thursday": 3, "Friday": 4, "Saturday": 5, "Sunday": 6}

    nth_day = 0
    for d  in daydict.keys():
        if day_in == d:
            nth_day = daydict[d[0]]

    cal = calendar.Calendar()
    caliter = cal.monthdayscalendar(year_in, month_in)

    nth_week = 0
    if date_in[0].isdigit():
        nth_week = date_in[0]
    elif date_in.lower() == "first":
        nth_week = 0
    elif date_in.lower() == "last":
        nth_week = len(caliter)

    day_out = 0
    for d in caliter[nth_week]:
        day_out = d[nth_day]

    return date(year_in, month_in, day_out)
