from classes.life import Life


class Plant(Life):
    def __init__(
        self,
        x,
        y,
        life_points,
        energy,
        age,
        root_radius,
        seed_radius,
    ):
        super().__init__(
            x,
            y,
            life_points,
            energy,
            age,
        )
        self.root_radius = root_radius
        self.seed_radius = seed_radius

    def get_root_zone(self, size):
        zone = []
        for i in range(self.root_radius):
            for j in range(self.root_radius):
                if self.x+i in range(size[0]) and self.y+j in range(size[1]):
                    zone.append([self.x+i, self.y+j])
                if self.x-i in range(size[0]) and self.y-j in range(size[1]):
                    zone.append([self.x-i, self.y-j])
        return zone

    def get_seed_zone(self, size):
        zone = []
        for i in range(self.seed_radius):
            for j in range(self.seed_radius):
                if self.x+i in range(size[0]) and self.y+j in range(size[1]):
                    zone.append([self.x+i, self.y+j])
                if self.x-i in range(size[0]) and self.y-j in range(size[1]):
                    zone.append([self.x-i, self.y-j])
        return zone
