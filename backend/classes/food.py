class Food:
    def __init__(
        self,
        x,
        y,
        energy,
    ):
        self.x = x
        self.y = y
        self.energy = energy

    def modify_energy(self, amount):
        self.energy += amount

    def __del__(self):
        pass
