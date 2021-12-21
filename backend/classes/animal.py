from classes.life import Life


class Animal(Life):
    def __init__(
        self,
        uid,
        specie,
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
            contact_zone,
            pos_x,
            pos_y,
            gestated,
        )
        self.vision_zone = vision_zone
        self.hierarchy = hierarchy

    def modify_hierarchy(self, amount):
        self.hierarchy += amount

    def get_vision_zone(self):
        pass
