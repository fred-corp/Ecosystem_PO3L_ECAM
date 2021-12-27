from classes.food import Food


class OrganicWaste(Food):
    def __init__(
        self,
        UUID,
        lifeform,
        x,
        y,
    ):
        super().__init__(UUID, lifeform, x, y, 5)
