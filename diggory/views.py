from kinto.core import Service
from .calendar import CALENDARS

holidays = Service(name='holidays', path='/holidays{year:(/[0-9]{4})?}', description="Holidays")


@holidays.get()
def get_holidays(request):
    year = request.matchdict['year'].strip('/')
    if year == '':
        year = None
    else:
        year = int(year)

    holidays = {}

    for name, klass in CALENDARS.items():
        try:
            cal = klass()
            country_holidays = cal.holidays(year)
        except Exception as e:
            print("{}".format(e))
            continue
        else:
            for date, title in country_holidays:
                date_id = date.strftime('%Y-%m-%d')
                holidays.setdefault(date_id, {
                    "date": date_id,
                    "title": title,
                    "countries": []
                })
                holidays[date_id]["countries"].append(name)
    return {"data": sorted(holidays.values(), key=lambda t: t["date"])}
