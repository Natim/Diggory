from datetime import date
from diggory.calendar import (
    Australia,
    Canada,
    Belgium,
    Denmark,
    Finland,
    France,
    Germany,
    Netherlands,
    NewZealand,
    Poland,
    Spain,
    Sweden,
    UnitedKingdom,
    UnitedStates,
)


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


def test_denmark_year_2017():
    cal = Denmark()
    holidays = cal.holidays_set(2017)
    assert holidays == {
        date(2017, 1, 1),   # New Year
        date(2017, 4, 9),   # Palm Sunday
        date(2017, 4, 13),  # Maundy Thursday
        date(2017, 4, 14),  # Good Friday
        date(2017, 4, 16),  # Easter
        date(2017, 4, 17),  # Easter Monday
        date(2017, 5, 25),  # Ascension
        date(2017, 6, 4),   # Pentcost Sunday
        date(2017, 6, 5),   # Whit Monday
        date(2017, 5, 12),  # Great Prayer Day
        date(2017, 12, 24),  # XMas Eve
        date(2017, 12, 25),  # XMas Eve (Observed)
        date(2017, 12, 26),  # XMas Day (Boxing)
        date(2017, 12, 31),  # New Year Eve's
    }, "{}".format(cal.holidays(2017))


def test_france_year_2017():
    cal = France()
    holidays = cal.holidays_set(2017)
    assert holidays == {
        date(2017, 1, 1),   # New Year
        date(2017, 1, 2),   # New Year (Observed)
        date(2017, 4, 17),  # Easter Monday
        date(2017, 5, 1),   # Fete du travail
        date(2017, 5, 8),   # 8 mai 1945
        date(2017, 5, 25),  # Ascension
        date(2017, 7, 14),  # Fête Nationale
        date(2017, 8, 15),  # Assumption
        date(2017, 11, 1),  # La Toussaint
        date(2017, 11, 10),  # Armistice 39 Observed
        date(2017, 11, 11),  # Armistice 39
        date(2017, 12, 25),  # XMas Day
    }, "{}".format(cal.holidays(2017))


def test_germany_year_2017():
    cal = Germany()
    holidays = cal.holidays_set(2017)
    assert holidays == {
        date(2017, 1, 1),   # New Year
        date(2017, 1, 2),   # New Year (Observed)
        date(2017, 1, 6),   # Epiphany
        date(2017, 4, 14),  # Good Friday
        date(2017, 4, 17),  # Easter Monday
        date(2017, 5, 1),   # May Day
        date(2017, 5, 25),  # Ascension
        date(2017, 6, 5),   # Whit Monday
        date(2017, 6, 15),  # Corpus Christi
        date(2017, 8, 15),  # Assumption
        date(2017, 10, 3),  # Day of German Unity
        date(2017, 10, 31),  # Reformation Day (500 anniversary in 2017)
        date(2017, 11, 1),   # All Saints
        date(2017, 11, 22),  # Day of Prayer & Repentance
        date(2017, 12, 25),  # XMas Day
        date(2017, 12, 26),  # XMas Day (Boxing)
    }, "{}".format(cal.holidays(2017))


def test_netherlands_year_2017():
    cal = Netherlands()
    holidays = cal.holidays_set(2017)
    assert holidays == {
        date(2017, 1, 1),   # New Year
        date(2017, 4, 14),  # Good Friday
        date(2017, 4, 16),  # Easter
        date(2017, 4, 17),  # Easter Monday
        date(2017, 4, 27),  # King Birthday
        date(2017, 5, 25),  # Ascension
        date(2017, 6, 4),   # Whitsundays
        date(2017, 6, 5),   # Whit Monday
        date(2017, 12, 25),  # XMas Day
        date(2017, 12, 26),  # XMas Day (Boxing)
    }, "{}".format(cal.holidays(2017))


def test_new_zealand_year_2017():
    cal = NewZealand()
    holidays = cal.holidays_set(2017)
    assert holidays == {
        date(2017, 1, 1),   # New Year
        date(2017, 1, 2),   # New Year (observed)
        date(2017, 2, 6),   # Waitangi Day
        date(2017, 4, 14),  # Good Friday
        date(2017, 4, 17),  # Easter Monday
        date(2017, 4, 25),  # Anzac
        date(2017, 6, 5),   # Queens Birthday
        date(2017, 10, 23),  # Labour Day
        date(2017, 12, 25),  # XMas Day
        date(2017, 12, 26),  # XMas Day (Boxing)
    }, "{}".format(cal.holidays(2017))


def test_poland_year_2017():
    cal = Poland()
    holidays = cal.holidays_set(2017)
    assert holidays == {
        date(2017, 1, 1),   # New Year
        date(2017, 4, 16),  # Easter
        date(2017, 4, 17),  # Easter Monday
        date(2017, 5, 1),   # Labour Day
        date(2017, 5, 3),   # Constitution Day
        date(2017, 8, 15),  # Assumption
        date(2017, 6, 4),   # Whitsunday
        date(2017, 6, 15),  # Corpus Christi
        date(2017, 11, 1),  # All Saints
        date(2017, 11, 11),  # Independance Day
        date(2017, 12, 25),  # XMas Day
        date(2017, 12, 26),  # XMas Day (Boxing)
    }, "{}".format(cal.holidays(2017))


def test_spain_year_2017():
    cal = Spain()
    holidays = cal.holidays_set(2017)
    assert holidays == {
        date(2017, 1, 1),   # New Year
        date(2017, 1, 2),   # New Year (observed)
        date(2017, 1, 6),   # Epiphany
        date(2017, 4, 13),  # Maundy Thursday
        date(2017, 4, 14),  # Good Friday
        date(2017, 5, 1),   # Labour Day
        date(2017, 8, 15),  # Assumption
        date(2017, 10, 12),  # Fiesta Nacional de Espana
        date(2017, 11, 1),   # All saints
        date(2017, 12, 6),   # Constitution Day
        date(2017, 12, 8),   # Immaculate Conception
        date(2017, 12, 25),  # XMas Day
    }, "{}".format(cal.holidays(2017))


def test_sweden_year_2017():
    cal = Sweden()
    holidays = cal.holidays_set(2017)
    assert holidays == {
        date(2017, 1, 1),   # New Year
        date(2017, 1, 2),   # New Year (observed)
        date(2017, 1, 6),   # Epiphany
        date(2017, 4, 14),  # Good Friday
        date(2017, 4, 16),  # Easter
        date(2017, 4, 17),  # Easter Monday
        date(2017, 5, 1),   # Labour Day
        date(2017, 5, 25),  # Ascension
        date(2017, 6, 4),   # Pentcost Sunday
        date(2017, 6, 6),   # National Day
        date(2017, 6, 23),  # Midsummer's Eve
        date(2017, 6, 24),  # Midsummer's Day
        date(2017, 11, 4),  # All saints
        date(2017, 12, 24),  # XMas Eve
        date(2017, 12, 25),  # XMas Day
        date(2017, 12, 26),  # XMas Day (Boxing)
        date(2017, 12, 31),  # New Year Eve's
    }, "{}".format(cal.holidays(2017))


def test_united_kingdom_year_2017():
    cal = UnitedKingdom()
    holidays = cal.holidays_set(2017)
    assert holidays == {
        date(2017, 1, 1),   # New Year
        date(2017, 1, 2),   # New Year (observed)
        date(2017, 4, 14),  # Good Friday
        date(2017, 4, 16),  # Easter
        date(2017, 4, 17),  # Easter Monday
        date(2017, 5, 1),   # Early May Bank Holiday
        date(2017, 5, 29),  # Spring Bank Holiday
        date(2017, 8, 28),  # Summer Bank Holiday
        date(2017, 12, 25),  # XMas Day
        date(2017, 12, 26),  # XMas Day (Boxing)
    }, "{}".format(cal.holidays(2017))


def test_belgium_year_2017():
    cal = Belgium()
    holidays = cal.holidays_set(2017)
    assert holidays == {
        date(2017, 1, 1),   # New Year
        date(2017, 1, 2),   # New Year (observed)
        date(2017, 4, 17),  # Easter Monday
        date(2017, 5, 1),   # Early May Bank Holiday
        date(2017, 5, 25),  # Ascension
        date(2017, 6, 5),   # Whit Monday
        date(2017, 7, 21),  # Belgium National Holiday
        date(2017, 8, 15),  # Assumption
        date(2017, 11, 1),  # All saints
        date(2017, 11, 11),  # Armistice Day
        date(2017, 11, 13),  # Armistice Day (Observed)
        date(2017, 12, 25),  # XMas Day
    }, "{}".format(cal.holidays(2017))


def test_finland_year_2017():
    cal = Finland()
    holidays = cal.holidays_set(2017)
    assert holidays == {
        date(2017, 1, 1),   # New Year
        date(2017, 1, 6),   # Epiphany
        date(2017, 4, 14),  # Good Friday
        date(2017, 4, 16),  # Easter
        date(2017, 4, 17),  # Easter Monday
        date(2017, 5, 1),   # Early May Bank Holiday
        date(2017, 5, 25),  # Ascension
        date(2017, 6, 4),   # Pentcost Sunday
        date(2017, 6, 23),  # Midsummer's Eve
        date(2017, 6, 24),  # Midsummer's Day
        date(2017, 11, 4),  # All saints
        date(2017, 12, 6),  # Independance Day
        date(2017, 12, 24),  # XMas Eve
        date(2017, 12, 25),  # XMas Day
        date(2017, 12, 26),  # St. Stephen's Day
    }, "{}".format(cal.holidays(2017))
