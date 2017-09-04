from workalendar.core import WesternCalendar
from workalendar.europe.denmark import Denmark
from workalendar.europe.france import France as WorkalendarFrance
from workalendar.europe.germany import Saxony
from workalendar.europe.netherlands import Netherlands as WorkalendarNetherlands

from .utils import ShiftMixin


__all__ = ('Denmark', 'France', 'Germany', 'Netherlands')


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
