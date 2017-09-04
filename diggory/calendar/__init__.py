from .oceania import Australia, NewZealand
from .canada import Canada
from .europe import (
    Belgium, Denmark, Finland, France, Germany, Netherlands, Poland, Spain, Sweden, UnitedKingdom
)
from .usa import UnitedStates


__all__ = (
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


CALENDARS = {getattr(c, 'name', c.__name__): c for c in __all__}
