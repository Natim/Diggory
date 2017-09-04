from workalendar.europe.denmark import Denmark
from workalendar.europe.france import France as WorkalendarFrance
from .utils import ShiftMixin


__all__ = ('Denmark', 'France')


class France(WorkalendarFrance, ShiftMixin):
    include_whit_monday = False   # Mozilla Solidarity day

    def get_calendar_holidays(self, year):
        """
        Will return holidays and their shifted days
        """
        days = super(France, self).get_calendar_holidays(year)
        days = self.shift(days, year)
        return days
