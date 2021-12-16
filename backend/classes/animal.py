from classes.life import Life


class Animal(Life):
    def __init__(
        self,
        life_points,
        energy_reserve,
        age,
        gender,
        food_type,
        vision_zone,
        contact_zone,
        hierarchy,
    ):
        super().__init__(
            life_points,
            energy_reserve,
            age,
            gender,
            food_type,
            vision_zone,
            contact_zone,
        )
        self.hierarchy = hierarchy

    def modify_hierarchy(self, amount):
        self.hierarchy += amount
