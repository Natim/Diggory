from workalendar.core import SUN, MON, SAT
from datetime import date, timedelta


class ShiftMixin(object):
    shift_forward = False

    # Shift day mechanism
    # These days won't be shifted to next MON or previous FRI
    shift_exceptions = ()

    def shift(self, holidays, year):
        new_holidays = []
        holiday_lookup = [x[0] for x in holidays]
        exceptions = [
            date(year, month, day) for month, day in self.shift_exceptions
        ]

        # For each holiday available:
        # * if it falls on SUN, add the observed on MON
        # * if it falls on SAT, add the observed on FRI
        for day, label in holidays:
            # ... except if it's been explicitely excepted.
            if day in exceptions:
                continue
            if day.weekday() == SAT:
                if self.shift_forward:
                    # Next monday
                    new_holidays.append((day + timedelta(days=2),
                                         label + " (Observed)"))
                else:
                    # Previous friday
                    new_holidays.append((day - timedelta(days=1),
                                         label + " (Observed)"))
            elif day.weekday() == SUN:
                new_holidays.append((day + timedelta(days=1),
                                     label + " (Observed)"))

        # If year+1 January the 1st is on SAT, add the FRI before to observed
        if date(year + 1, 1, 1).weekday() == SAT:
            new_holidays.append((date(year, 12, 31,),
                                 "New Years Day (Observed)"))

        # Special rules for XMas and XMas Eve
        christmas = date(year, 12, 25)
        christmas_eve = date(year, 12, 24)
        # Is XMas eve in your calendar?
        if christmas_eve in holiday_lookup:
            # You are observing the THU before, as an extra XMas Eve
            if christmas.weekday() == SAT:
                new_holidays.append((date(year, 12, 23),
                                     "Christmas Eve (Observed)"))
            # You are observing the 26th (TUE) and 27th (WED)
            elif christmas.weekday() == MON:
                new_holidays.append((date(year, 12, 26),
                                     "Christmas Day (Observed)"))
        return holidays + new_holidays
