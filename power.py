from enum import Enum, auto


class PowerColor(Enum):
    """Enumeration of the different types of powers a bird can have."""
    WHITE = auto()  # when played
    BROWN = auto()  # when activated
    PINK = auto()  # once per turn
    YELLOW = auto()  # round end
    BLUE = auto()  # game end


class PowerCondition(Enum):
    """Enumeration of the different types of conditions a power can have."""
    ALWAYS = auto()
    FOOD = auto()
    EGGS = auto()
    WINGSPAN = auto()
    HABITAT = auto()
    NEST = auto()
    DICE = auto()
    TUCK = auto()


class PowerResult(Enum):
    """Enumeration of the different types of results a power can have."""
    EGGS = auto()
    FOOD = auto()
    CARDS = auto()
    TUCK = auto()


class Power:
    def __init__(self, *, power_color: PowerColor, condition: PowerCondition, result: PowerResult, power_text: str):
        self.text: str = power_text
        self.color: PowerColor = power_color
        self.condition: PowerCondition = condition
        self.result: PowerResult = result
    
    def activate(self, bird):
        if self.check_condition(bird):
            if self.user_approved():
                self.run_result(bird)
    
    def user_approved(self) -> bool:
        print(f'Power:\n{self.text}')
        return input("Do you want to activate the above power? (Y/N) ").lower() == 'y'
    
    def check_condition(self, bird) -> bool:
        if self.condition == PowerCondition.ALWAYS:
            return True
        else:
            pass
    
    def run_result(self, bird) -> None:
        print("Power activated")
