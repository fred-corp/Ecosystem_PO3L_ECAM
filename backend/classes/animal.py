from abc import ABC, abstractmethod
from classes.life import Life


class Animal(Life, ABC):
    def __init__(
        self,
        UUID,
        lifeform,
        x,
        y,
        age,
        lifespan,
        health_points,
        max_health_points,
        energy_points,
        max_energy_points,
        gender,
        gets_pregnant,
        adultAt,
        vision_radius,
        contact_radius,
        max_move
    ):
        super().__init__(
            UUID,
            lifeform,
            x,
            y,
            health_points,
            energy_points,
            max_energy_points,
            age,
            lifespan,
        )
        self.gender = gender
        self.gets_pregnant = gets_pregnant
        self.adultAt = adultAt
        self.vision_radius = vision_radius
        self.contact_radius = contact_radius
        self.max_move = max_move

    def get_contact_zone(self, size):
        zone = []
        for i in range(1, self.contact_radius):
            for j in range(1, self.contact_radius):
                if self.x+i in range(size[0]) and self.y+j in range(size[1]):
                    zone.append([self.x+i, self.y+j])
                if self.x-i in range(size[0]) and self.y-j in range(size[1]):
                    zone.append([self.x-i, self.y-j])
        return zone

    def get_vision_zone(self, size):
        zone = []
        for i in range(1, self.vision_radius):
            for j in range(1, self.vision_radius):
                if self.x+i in range(size[0]) and self.y+j in range(size[1]):
                    zone.append([self.x+i, self.y+j])
                if self.x-i in range(size[0]) and self.y-j in range(size[1]):
                    zone.append([self.x-i, self.y-j])
        return zone

    # TODO :
    # • Verify which gender gets pregnant
    # • Add cooldown to reproduction
    def gestated(self, min_age):
        if self.age > min_age:
            return True
        else:
            return False

    @abstractmethod
    def eat_meat(self):
        pass
