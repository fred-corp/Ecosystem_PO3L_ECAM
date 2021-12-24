from abc import ABC, abstractmethod
from classes.life import Life


class Animal(Life, ABC):
    def __init__(
        self,
        x,
        y,
        life_points,
        energy,
        age,
        gender,
        vision_radius,
        contact_radius,
    ):
        super().__init__(
            x,
            y,
            life_points,
            energy,
            age,
        )
        self.gender = gender
        self.vision_radius = vision_radius
        self.contact_radius = contact_radius

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

    def gestated(self, min_age):
        if self.age > min_age:
            return True
        else:
            return False

    @abstractmethod
    def eat_meat(self):
        pass
