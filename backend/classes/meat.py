from classes.food import Food


class Meat(Food):
    def __init__(
        self,
        UUID,
        lifeform,
        x,
        y,
        energy_points,
        age,
        rotsAt
    ):
        super().__init__(UUID, lifeform, x, y, energy_points)
        self.age = age
        self.rotsAt = rotsAt

    def increase_age(self):
        self.age += 1
