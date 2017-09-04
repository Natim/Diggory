from workalendar.core import WesternCalendar
from workalendar.europe.belgium import Belgium as WorkalendarBelgium
from workalendar.europe.denmark import Denmark
from workalendar.europe.france import France as WorkalendarFrance
from workalendar.europe.germany import Saxony
from workalendar.europe.netherlands import Netherlands as WorkalendarNetherlands
from workalendar.europe.poland import Poland as WorkalendarPoland
from workalendar.europe.spain import Spain as WorkalendarSpain
from workalendar.europe.sweden import Sweden as WorkalendarSweden
from workalendar.europe.united_kingdom import UnitedKingdom

from .utils import ShiftMixin


__all__ = (
    'Belgium', 'Denmark', 'France', 'Germany', 'Netherlands', 'Poland',
    'Spain', 'Sweden', 'UnitedKingdom'
)


class France(WorkalendarFrance, ShiftMixin):
    include_whit_monday = False   # Mozilla Solidarity day

    def get_calendar_holidays(self, year):
        """
        Will return holidays and their shifted days
        """
        days = super(France, self).get_calendar_holidays(year)
        days = self.shift(days, year)
        return days


class Germany(Saxony, ShiftMixin):
    include_epiphany = True
    include_corpus_christi = True
    include_all_saints = True
    include_assumption = True
    include_reformation_day = True

    def get_calendar_holidays(self, year):
        """
        Will return holidays and their shifted days
        """
        days = super(Germany, self).get_calendar_holidays(year)
        days = self.shift(days, year)
        return days


class Netherlands(WorkalendarNetherlands):
    FIXED_HOLIDAYS = WesternCalendar.FIXED_HOLIDAYS


class Poland(WorkalendarPoland):
    FIXED_HOLIDAYS = WesternCalendar.FIXED_HOLIDAYS + (
        # (1, 6, 'Trzech Kroli'),  # Not a Mozilla Holiday
        (5, 1, 'Labour Day'),
        (5, 3, 'Constitution Day'),
        (11, 11, 'Independence Day'),
    )


class Belgium(WorkalendarBelgium, ShiftMixin):
    shift_new_years_day = True
    shift_forward = True

    def get_calendar_holidays(self, year):
        """
        Will return holidays and their shifted days
        """
        days = super(Belgium, self).get_calendar_holidays(year)
        days = self.shift(days, year)
        return days


class Sweden(WorkalendarSweden):
    shift_new_years_day = True


class Spain(WorkalendarSpain):
    include_holy_thursday = True
    shift_new_years_day = True
