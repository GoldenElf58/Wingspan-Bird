from bird import Bird
from power import *
from utils import *


def main() -> None:
    power = Power(power_color=PowerColor.BROWN, condition=PowerCondition.ALWAYS, result=PowerResult.EGGS,
                  power_text="Test Power Text")
    bird = Bird("Test Bird", victory_points=1, max_eggs=1, wingspan=1, habitats=Habitat.FOREST,
                nest_type=NestType.BOWL, power=power, food_cost={Food.SEED: 1}, scientific_name="Test Bird",
                fun_fact="Test Fun Fact", location="Test")
    bird.power.activate(bird)


if __name__ == '__main__':
    main()
