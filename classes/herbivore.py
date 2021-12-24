from classes.animal import Animal


class Herbivore(Animal):
    def __init__(
        self,
        x,
        y,
        life_points,
        energy,
        age,
        gender,
        vision_radius,
        contact_radius,
    ):
        super().__init__(
                x,
                y,
                life_points,
                energy,
                age,
                gender,
                vision_radius,
                contact_radius,
            )

    def eat_meat(self):
        return False
