from workalendar.core import Calendar
from kinto.core import Service
from .utils import import_submodules

holidays = Service(name='holidays', path='/holidays{year:(/[0-9]{4})?}', description="Holidays")


def get_subclasses(klass, calendars=None):
    if calendars is None:
        calendars = {}
    if hasattr(klass, '__subclasses__'):
        for k in klass.__subclasses__():
            if not k.__name__.endswith('Mixin'):
                calendars[k.__name__] = k
            get_subclasses(k, calendars)
    return calendars


def workalendar_countries():
    import_submodules('workalendar')
    return get_subclasses(Calendar)


@holidays.get()
def get_holidays(request):
    year = request.matchdict['year'].strip('/')
    if year == '':
        year = None
    else:
        year = int(year)
    countries = workalendar_countries()

    holidays = {}

    for CountryKlass in countries.values():
        try:
            cal = CountryKlass()
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
                holidays[date_id]["countries"].append(CountryKlass.__name__)
    return {"data": sorted(holidays.values(), key=lambda t: t["date"])}
