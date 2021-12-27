class Food:
    def __init__(
        self,
        UUID,
        lifeform,
        x,
        y,
        energy_points,
    ):
        self.UUID = UUID
        self.lifeform = lifeform
        self.x = x
        self.y = y
        self.energy_points = energy_points

    def modify_energy(self, amount):
        self.energy_points += amount

    def __del__(self):
        pass
