from enum import Enum, auto, Flag


class PowerType(Enum):
    WHEN_PLAYED = auto()
    WHEN_ACTIVATED = auto()
    ONCE_BETWEEN_TURNS = auto()
    ROUND_END = auto()
    GAME_END = auto()


class NestType(Enum):
    PLATFORM = auto()
    BOWL = auto()
    CAVITY = auto()
    GROUND = auto()
    STAR = auto()


class Location(Flag):
    NORTH_AMERICA = auto()
    SOUTH_AMERICA = auto()
    EUROPE = auto()
    ASIA = auto()
    AFRICA = auto()
    OCEANIA = auto()
    ANTARCTICA = auto()
   
   
class Habitat(Flag):
    FOREST = auto()
    GRASSLANDS = auto()
    WETLANDS = auto()


class Food(Enum):
    WILD = auto()
    SEED = auto()
    FISH = auto()
    FRUIT = auto()
    INVERTEBRATE = auto()
    RODENT = auto()
    NECTAR = auto()
