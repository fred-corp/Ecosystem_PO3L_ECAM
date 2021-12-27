class Life:
    def __init__(
        self,
        x,
        y,
        life_points,
        energy,
        age,
    ):
        self.x = x
        self.y = y
        self.life_points = life_points
        self.energy = energy
        self.age = age

    def modify_energy(self, amount):
        self.energy += amount

    def modify_life_points(self, amount):
        self.life_points += amount

    def make_move(self, coord):
        self.x = coord[0]
        self.y = coord[1]

    def increase_age(self):
        self.age += 1

    def __del__(self):
        pass
