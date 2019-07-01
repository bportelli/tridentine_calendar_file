"""The movable feasts of the liturgical calendar.

These feasts are represented as objects with a `name` and a `date`.  The `name` attribute links the
feast to the other data in `movable_feasts_ferias_et_al.json`.

NOTE: The `tridentine_calendar` module will introspect this module to find all the movable feasts in
the calendar.  Any `MovableFeast` objects added to this module will therefore be added to the
calendor generated by `tridentine_calendar`.

"""

from abc import ABCMeta
from abc import abstractmethod


class MovableFeast(metaclass=ABCMeta):
    """An abstract class for a movable feast.

    A movable feast must have two attributes:

    1. A name.
    2. A date.

    The name must correspond to the feast data in `movable_feasts_ferias_et_al.json`.

    """

    def __init__(self, year):
        # TODO: Determine how the date is saved.
        pass

    @property
    @abstractemethod
    def name(self):
        raise NotImplementedError
    
    @abstractmethod
    def date(self, year):
        # TODO: Determine what the signature of this function should be.
        pass
