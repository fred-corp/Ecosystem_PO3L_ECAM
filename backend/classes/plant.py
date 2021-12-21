from classes.life import Life


class Plant(Life):
    def __init__(
        self,
        uid,
        specie,
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
        gestated,
    ):
        super().__init__(
            uid,
            specie,
            life_points,
            energy_reserve,
            age,
            gender,
            food_type,
            0,
            contact_zone,
            pos_x,
            pos_y,
            gestated,
        )
        self.root_zone = root_zone
        self.seeding_zone = seeding_zone
