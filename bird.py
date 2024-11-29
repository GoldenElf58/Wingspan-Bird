from utils import *


class Bird:
    def __init__(self, name: str, *,
                 victory_points: int,
                 max_eggs: int,
                 wingspan: int,
                 habitats: Habitat,
                 nest_type: NestType,
                 power_type: PowerType,
                 power_text: str,
                 food_cost: dict[Food, int],
                 scientific_name: str | None = None,
                 fun_fact: str | None = None,
                 location: Location | None = None):
        self.name: str = name
        self.victory_points: int = victory_points
        self.max_eggs: int = max_eggs
        self.wingspan: int = wingspan
        self.num_eggs: int = 0
        self.habitats: Habitat = habitats
        self.power_type: PowerType = power_type
        self.power_text: str = power_text
        self.nest_type: NestType = nest_type
        self.food_cost: dict[Food, int] = food_cost
        self.scientific_name = scientific_name
        self.fun_fact: str | None = fun_fact
        self.location: Location | None = location
        
