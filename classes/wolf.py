from classes.carnivore import Carnivore


class Wolf(Carnivore):
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
                7,
                age,
                gender,
                15,
                3,
            )
        self.max_energy = 7
        self.max_move = 5
        self.max_age = 10
