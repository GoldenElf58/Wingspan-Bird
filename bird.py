from utils import *
from power import Power


class Bird:
    """
    A Bird object represents a specific type of bird card in Wingspan.
    
    :param name: The name of the bird species.
    :param victory_points: The number of victory points awarded for this bird.
    :param max_eggs: The number of eggs that can be laid in this bird's nest.
    :param wingspan: The wingspan of the bird in centimeters.
    :param habitats: The habitats in which this bird can be played.
    :param nest_type: The type of nest that this bird builds.
    :param power_type: The type of this bird's power (e.g. when played, when activated, etc).
    :param power_func: The function that implements this bird's power.
    :param power_text: A string that describes the power.
    :param food_cost: A dictionary with each food required as a key and the quantity required as the value.
    :param scientific_name: The scientific name of the bird species, or None.
    :param fun_fact: A fun fact about the bird species, or None.
    :param location: The location where the bird species can be found, or None.
    """
    
    def __init__(self, name: str, *,
                 victory_points: int,
                 max_eggs: int,
                 wingspan: int,
                 habitats: Habitat,
                 nest_type: NestType,
                 power: Power,
                 food_cost: dict[Food, int],
                 scientific_name: str | None = None,
                 fun_fact: str | None = None,
                 location: Location | None = None):
        """
        A Bird object represents a specific type of bird card in Wingspan.
        
        :param name: The name of the bird species.
        :param victory_points: The number of victory points awarded for this bird.
        :param max_eggs: The number of eggs that can be laid in this bird's nest.
        :param wingspan: The wingspan of the bird in centimeters.
        :param habitats: The habitats in which this bird can be played.
        :param nest_type: The type of nest that this bird builds.
        :param power_type: The type of this bird's power (e.g. when played, when activated, etc).
        :param power_func: The function that implements this bird's power.
        :param power_text: A string that describes the power.
        :param food_cost: A dictionary with each food required as a key and the quantity required as the value.
        :param scientific_name: The scientific name of the bird species, or None.
        :param fun_fact: A fun fact about the bird species, or None.
        :param location: The location where the bird species can be found, or None.
        """
        self.name: str = name
        self.victory_points: int = victory_points
        self.max_eggs: int = max_eggs
        self.wingspan: int = wingspan
        self.num_eggs: int = 0
        self.habitats: Habitat = habitats
        self.power: Power = power
        self.nest_type: NestType = nest_type
        self.food_cost: dict[Food, int] = food_cost
        self.scientific_name: str | None = scientific_name
        self.fun_fact: str | None = fun_fact
        self.location: Location | None = location
    
    def can_add_eggs(self, num_eggs: int = 1) -> bool:
        """
        Check if the bird can add eggs.
        
        :param num_eggs: The number of eggs to add. Defaults to 1.
        :return: True if the bird can add eggs, False otherwise.
        """
        return self.num_eggs + num_eggs <= self.max_eggs
    
    def add_eggs(self, num_eggs: int = 1) -> None:
        """
        Add eggs to the bird's nest.
        
        :param num_eggs: The number of eggs to add. Defaults to 1.
        :raises ValueError: If the number of eggs to add would exceed the maximum number of eggs.
        """
        if not self.can_add_eggs(num_eggs):
            raise ValueError(
                f'Cannot add {num_eggs} eggs to {self.name}. Max eggs: {self.max_eggs} Current eggs: {self.num_eggs}')
        self.num_eggs += num_eggs
    
    def __repr__(self):
        """
        Return a string representation of the Bird object.
    
        :return: A string containing the bird's name, victory points, max eggs,
                 wingspan, nest type, power type, power text, food cost, and
                 optionally the scientific name, fun fact, and location if they
                 are not None.
        """
        res = f'=== {self.name} ===\n'
        res += f'Victory Points: {self.victory_points}\n'
        res += f'Max Eggs: {self.max_eggs}\n'
        res += f'Wingspan: {self.wingspan}\n'
        res += f'Nest Type: {self.nest_type}\n'
        res += f'Power: {self.power}\n'
        res += f'Food Cost: {self.food_cost}\n'
        if self.scientific_name is not None:
            res += f'Scientific Name: {self.scientific_name}\n'
        if self.fun_fact is not None:
            res += f'Fun Fact: {self.fun_fact}\n'
        if self.location is not None:
            res += f'Location: {self.location}\n'
        return res
    
    def __str__(self):
        """
        Return a string representation of the Bird object.
        
        :return:  A string containing the bird's name, victory points, max eggs,
                  wingspan, nest type, power type, power text, food cost, and
                  optionally the scientific name, fun fact, and location if they
                  are not None.
        """
        return self.__repr__()
