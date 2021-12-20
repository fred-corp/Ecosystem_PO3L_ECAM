from classes.ecosystem import Ecosystem


class Life(Ecosystem):
    def __init__(
        self,
        uid,
        life_points,
        energy_reserve,
        age,
        gender,
        food_type,
        contact_zone,
        pos_x,
        pos_y,
    ):
        self.uid = id
        self.life_points = life_points
        self.energy_reserve = energy_reserve
        self.age = age
        self.gender = gender
        self.food_type = food_type
        self.contact_zone = contact_zone
        self.pos_x = pos_x
        self.pos_y = pos_y

    def modify_energy(self, amount):
        self.energy_reserve += amount

    def modify_life_points(self, amount):
        self.life_points += amount

    def get_contact_zone(self, rows, cols):
        zone = []
        for i in range(self.contact_zone):
            for j in range(self.contact_zone):
                if self.pos_x+i in range(rows) and self.pos_y+j in range(cols):
                    zone.append([self.pos_x+i, self.pos_y+j])
                if self.pos_x-i in range(rows) and self.pos_y-j in range(cols):
                    zone.append([self.pos_x-i, self.pos_y-j])
        return zone

    def __del__(self):
        pass
