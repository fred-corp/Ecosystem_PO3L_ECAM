from classes.food import Food


class Meat(Food):
    def __init__(
        self,
        x,
        y,
        age,
    ):
        super().__init__(x, y, 9)
        self.age = age
        self.meat_rot_age = 8

    def increase_age(self):
        self.age += 1
