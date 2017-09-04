from workalendar.usa.core import UnitedStates as WorkalendarUSA


class UnitedStates(WorkalendarUSA):
    """USA Mozilla observance"""
    name = "United States"
    include_thanksgiving_friday = True
    include_christmas_eve = True
    include_veterans_day = False
    include_cesar_chavez_day = False
    include_columbus_day = False
