from classes.life import Life


class Animal(Life):
    def __init__(
        self,
        uid,
        life_points,
        energy_reserve,
        age,
        gender,
        food_type,
        vision_zone,
        contact_zone,
        hierarchy,
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
            contact_zone,
            pos_x,
            pos_y,
        )
        self.vision_zone = vision_zone
        self.hierarchy = hierarchy

    def modify_hierarchy(self, amount):
        self.hierarchy += amount

    def get_vision_zone(self):
        pass
