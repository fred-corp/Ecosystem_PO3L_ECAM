from classes.animal import Animal


class Herbivore(Animal):
    def __init__(
        self,
        UUID,
        x,
        y,
        age,
        lifespan,
        health_points,
        max_health_points,
        energy_points,
        max_energy_points,
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
                age,
                lifespan,
                health_points,
                max_health_points,
                energy_points,
                max_energy_points,
                gender,
                gets_pregnant,
                vision_radius,
                contact_radius,
                max_move
            )

    def eat_meat(self):
        return False
