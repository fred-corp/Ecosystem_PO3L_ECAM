from classes.animal import Animal


class Herbivore(Animal):
    def __init__(
        self,
        UUID,
        x,
        y,
        life_points,
        energy,
        max_energy,
        age,
        max_age,
        gender,
        gets_pregnant,
        vision_radius,
        contact_radius,
        max_move
    ):
        super().__init__(
                UUID,
                x,
                y,
                life_points,
                energy,
                max_energy,
                age,
                max_age,
                gender,
                gets_pregnant,
                vision_radius,
                contact_radius,
                max_move
            )

    def eat_meat(self):
        return False
