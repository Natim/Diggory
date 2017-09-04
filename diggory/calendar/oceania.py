from workalendar.core import WesternCalendar, MON
from workalendar.oceania import (
    Australia as WAustralia,
    AustraliaCapitalTerritory
)


class Australia(WAustralia):
    include_queens_birthday = True
    include_labour_day_october = True

    def get_variable_days(self, year):
        cal = AustraliaCapitalTerritory()
        days = super().get_variable_days(year)
        days.extend([
            cal.get_family_community_day(year),
        ])
        return days


class NewZealand(WAustralia):
    "New Zealand"
    include_queens_birthday = True
    include_labour_day_october = True

    FIXED_HOLIDAYS = WesternCalendar.FIXED_HOLIDAYS + (
        (2, 6, "Waitangi Day"),
    )

    def get_queens_birthday(self, year):
        return (
            Australia.get_nth_weekday_in_month(year, 6, MON),
            "Queen's Birthday"
        )

    def get_labour_day_october(self, year):
        return (
            NewZealand.get_nth_weekday_in_month(year, 10, MON, 4),
            'Labour Day'
        )
