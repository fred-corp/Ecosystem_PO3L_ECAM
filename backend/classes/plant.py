from classes.life import Life


class Plant(Life):
    def __init__(
        self,
        uid,
        life_points,
        energy_reserve,
        age,
        gender,
        contact_zone,
        root_zone,
        seeding_zone,
        food_type,
        pos_x,
        pos_y,
    ):
        super().__init__(
            uid,
            life_points,
            energy_reserve,
            age,
            gender,
            food_type,
            0,
            contact_zone,
            pos_x,
            pos_y,
        )
        self.root_zone = root_zone
        self.seeding_zone = seeding_zone
