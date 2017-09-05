from workalendar.canada import BritishColumbia, LateFamilyDayMixin, BoxingDayMixin
from .utils import ShiftMixin


class Canada(BritishColumbia, BoxingDayMixin, LateFamilyDayMixin, ShiftMixin):
    FIXED_HOLIDAYS = BritishColumbia.FIXED_HOLIDAYS + (
        (11, 11, "Remembrance Day"),
        (6, 24, "La fête nationale"),
    )

    # Shift day mechanism
    # These days won't be shifted to next MON or previous FRI
    shift_exceptions = (
        (7, 1),
    )

    def get_variable_days(self, year):
        days = super(BritishColumbia, self).get_variable_days(year)
        days.extend([
            (BritishColumbia.get_family_day(self, year)),
            (LateFamilyDayMixin.get_family_day(self, year)),
            (self.get_victoria_day(year)),
            (self.get_civic_holiday(year, "British Columbia Day")),
            (self.get_thanksgiving(year)),
        ])
        days.extend(self.get_boxing_day(year))
        return days

    def get_calendar_holidays(self, year):
        """
        Will return holidays and their shifted days
        """
        days = super(Canada, self).get_calendar_holidays(year)
        days = self.shift(days, year)
        return days
