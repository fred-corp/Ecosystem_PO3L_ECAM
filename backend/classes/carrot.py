from classes.plant import Plant


class Carrot(Plant):
    def __init__(
        self,
        x,
        y,
        age,
    ):
        super().__init__(
            x,
            y,
            0,
            4,
            age,
            2,
            8,
        )
        self.max_energy = 6
        self.max_age = 7
        self.min_seed_age = 1
