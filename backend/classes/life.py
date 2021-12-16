from classes.ecosystem import Ecosystem


class Life(Ecosystem):
    def __init__(
            self,
            life_points,
            energy_reserve,
            age,
            gender,
            food_type,
            vision_zone,
            contact_zone
            ):
        self.life_points = life_points
        self.energy_reserve = energy_reserve
        self.age = age
        self.gender = gender
        self.food_type = food_type
        self.vision_zone = vision_zone
        self.contact_zone = contact_zone

    def modify_energy(self, amount):
        self.energy_reserve += amount

    def modify_life_points(self, amount):
        self.life_points += amount
