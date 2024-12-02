from enum import Enum, auto, Flag


class NestType(Enum):
    """Enumeration of the different types of nests birds can have."""
    PLATFORM = auto()
    BOWL = auto()
    CAVITY = auto()
    GROUND = auto()
    STAR = auto()


class Location(Flag):
    """Flag enumeration of the various geographic locations."""
    NORTH_AMERICA = auto()
    SOUTH_AMERICA = auto()
    EUROPE = auto()
    ASIA = auto()
    AFRICA = auto()
    OCEANIA = auto()
    ANTARCTICA = auto()
   
   
class Habitat(Flag):
    """Flag enumeration of the different types of habitats."""
    FOREST = auto()
    GRASSLANDS = auto()
    WETLANDS = auto()


class Food(Enum):
    """Enumeration of the different types of food a bird can eat."""
    WILD = auto()
    SEED = auto()
    FISH = auto()
    FRUIT = auto()
    INVERTEBRATE = auto()
    RODENT = auto()
    NECTAR = auto()