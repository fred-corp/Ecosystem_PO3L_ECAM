from life import Life


class Plant(Life):
    def __init__(self, life_points, energy_reserve, age, gender, contact_zone, root_zone, seeding_zone, food_type):
        super().__init__(life_points, energy_reserve, age, gender, food_type)
        self.contact_zone = contact_zone
        self.root_zone = root_zone
        self.seeding_zone = seeding_zone
