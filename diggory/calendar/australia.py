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
