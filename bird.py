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
    
    def __repr__(self):
        res = f'=== {self.name} ===\n'
        res += f'Victory Points: {self.victory_points}\n'
        res += f'Max Eggs: {self.max_eggs}\n'
        res += f'Wingspan: {self.wingspan}\n'
        res += f'Nest Type: {self.nest_type}\n'
        res += f'Power Type: {self.power_type}\n'
        res += f'Power Text: {self.power_text}\n'
        res += f'Food Cost: {self.food_cost}\n'
        if self.scientific_name is not None:
            res += f'Scientific Name: {self.scientific_name}\n'
        if self.fun_fact is not None:
            res += f'Fun Fact: {self.fun_fact}\n'
        if self.location is not None:
            res += f'Location: {self.location}\n'
        return res
    
    def __str__(self):
        return self.__repr__()
