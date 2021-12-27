class Life:
    def __init__(
        self,
        UUID,
        lifeform,
        x,
        y,
        age,
        health_points,
        energy_points,
        max_energy_points,
        lifespan,
    ):
        self.UUID = UUID
        self.lifeform = lifeform
        self.x = x
        self.y = y
        self.health_points = health_points
        self.energy_points = energy_points
        self.max_energy_points = max_energy_points
        self.age = age
        self.lifespan = lifespan

    def modify_energy(self, amount):
        self.energy_points += amount

    def modify_health_points(self, amount):
        self.health_points += amount

    def make_move(self, coord):
        self.x = coord[0]
        self.y = coord[1]

    def increase_age(self):
        self.age += 1

    def __del__(self):
        pass
