from classes.food import Food


class OrganicWaste(Food):
    def __init__(
        self,
        x,
        y,
    ):
        super().__init__(x, y, 5)
