from life import Life


class Animal(Life):
    def __init__(self, life_points, energy_reserve, age, gender, vision_zone, contact_zone, hierarchy, food_type):
        super().__init__(life_points, energy_reserve, age, gender, food_type)
        self.vision_zone = vision_zone
        self.contact_zone = contact_zone
        self.hierarchy = hierarchy

    def modify_hierarchy(self, amount):
        self.hierarchy += amount
