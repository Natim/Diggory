from datetime import date
from diggory.calendar import Australia, Canada, UnitedStates


def test_usa_year_2017():
    cal = UnitedStates()
    holidays = cal.holidays_set(2017)
    assert holidays == {
        date(2017, 1, 1),   # New Year
        date(2017, 1, 2),   # New Year Days
        date(2017, 1, 16),  # Martin Luther King, Jr. Day
        date(2017, 2, 20),  # President's day
        date(2017, 5, 29),  # Memorial Day
        date(2017, 7, 4),   # Independance day
        date(2017, 9, 4),   # Labour day
        date(2017, 11, 23),  # Thanskgiving
        date(2017, 11, 24),  # Day after Thanskgiving
        date(2017, 12, 24),  # XMas Eve
        date(2017, 12, 25),  # XMas Eve (Observed)
        date(2017, 12, 26),  # XMas Day (Boxing)
    }, "{}".format(cal.holidays(2017))


def test_australia_year_2017():
    cal = Australia()
    holidays = cal.holidays_set(2017)
    assert holidays == {
        date(2017, 1, 1),   # New Year
        date(2017, 1, 2),   # New Year Days
        date(2017, 1, 26),  # Australia Day
        date(2017, 4, 14),  # Good Friday
        date(2017, 4, 17),  # Easter monday
        date(2017, 4, 25),  # Anzac
        date(2017, 6, 12),  # Queens Birthday
        date(2017, 9, 25),  # Family & Community Day
        date(2017, 10, 2),  # Labour Day
        date(2017, 12, 25),  # XMas Eve (Observed)
        date(2017, 12, 26),  # XMas Day (Boxing)
    }, "{}".format(cal.holidays(2017))


def test_canada_year_2017():
    cal = Canada()
    holidays = cal.holidays_set(2017)
    assert holidays == {
        date(2017, 1, 1),   # New Year
        date(2017, 1, 2),   # New Year Days
        date(2017, 2, 13),  # Family Day British Columbia
        date(2017, 2, 20),  # Family Day Alberta, Ontario, Saskatchewan ou Louis Riel Day Manitoba
        date(2017, 4, 14),  # Good Friday
        date(2017, 5, 22),  # Victory Day or National Patriots' Day
        date(2017, 6, 23),  # La fête nationale Quebec (Observed)
        date(2017, 6, 24),  # La fête nationale Quebec
        date(2017, 7, 1),   # Canada Day
        date(2017, 7, 3),   # Canada Day (Observed)
        date(2017, 8, 7),   # Civic Holiday or British Columbia Day
        date(2017, 9, 4),   # Labour Day
        date(2017, 10, 9),   # Thanskgiving
        date(2017, 11, 10),  # Remembrance Day (Observed)
        date(2017, 11, 11),  # Remembrance Day
        date(2017, 12, 25),  # XMas Eve (Observed)
        date(2017, 12, 26),  # XMas Day (Boxing)
    }, "{}".format(cal.holidays(2017))
