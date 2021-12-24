from classes.herbivore import Herbivore


class Sheep(Herbivore):
    def __init__(
        self,
        x,
        y,
        age,
        gender,
    ):
        super().__init__(
                x,
                y,
                3,
                6,
                age,
                gender,
                5,
                2,
            )
        self.max_energy = 6
        self.max_move = 3
        self.max_age = 10
