class Life:
    def __init__(
        self,
        UUID,
        lifeform,
        x,
        y,
        life_points,
        energy,
        max_energy,
        age,
        max_age,
    ):
        self.UUID = UUID
        self.lifeform = lifeform
        self.x = x
        self.y = y
        self.life_points = life_points
        self.energy_points = energy
        self.max_energy = max_energy
        self.age = age
        self.max_age = max_age

    def modify_energy(self, amount):
        self.energy_points += amount

    def modify_life_points(self, amount):
        self.life_points += amount

    def make_move(self, coord):
        self.x = coord[0]
        self.y = coord[1]

    def increase_age(self):
        self.age += 1

    def __del__(self):
        pass
