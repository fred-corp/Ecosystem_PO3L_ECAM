import json
import os

from classes.animal import Animal

class_list = []

path = os.path.dirname(os.path.abspath(__file__)).removesuffix("backend")

ecosystem_path = os.path.join(path, "ecosystemExampleFiles", "example1.json")

with open(ecosystem_path) as file:
    data = json.load(file)
    rounds = data["rounds"]

    # a transformer en classe?
    rows, cols = data["fieldSize"][0], data["fieldSize"][1]
    ecosystem = [([0]*cols) for i in range(rows)]

    for life in rounds[0]:
        life_data = data["lifeDefaults"][life[1]]
        if life_data["species"] == "animal":
            class_list.append(
                Animal(
                    life[6],
                    life[7],
                    life[5],
                    life[2],
                    life_data["diet"],
                    data["visionRadius"],
                    data["contactRadius"],
                    life_data["hierarchy"],
                )
            )
            ecosystem[life[8]][life[9]] = life[0]
        elif life_data["species"] == "plant":
            pass

print(ecosystem)


def seek_zone():
    """return a list of predators, preys or food inside the vision zone
    of an animal
    """
    pass


def contact_zone():
    """return a list of:
    - for a carnivore: animals to attack, animals to reproduce with, predators
    - for a herbivore: plants to eat, animals to reproduce with, predators
    - for a plant: plants to reproduce with
    """
    pass


def attack():
    """reduce hp of an animal
    - for a carnivore: attack an animal with a lower hierarchy inside the
    contact zone
    """
    pass


def eat():
    """modify the energy reserve of a life
    - for a carnivore: eat meat inside the contact zone
    - for a herbivore: eat plants inside the contact zone
    - for a plant: eat organic waste inside the root zone
    """
    pass


def reproduce():
    """create a new life and
    - for an animal: reproduce with an animal of the other gender inside
    the contact zone and if both animals are aged enough, lower energy reserve
    - for a plant: create plants inside the seeding zone
    """
    pass


def drop_organicwaste():
    """drop organic waste for an animal"""
    pass


def move():
    """"move an animal"""
    pass


def lower_energy_reserve():
    """decrease energy reserve each round"""
    pass


def convert_life_point():
    """convert health points to energy reserve if energy reserve is empty"""
    pass


def decease():
    """decease if health points are 0
    - animal: destroy class and create meat
    - plant: destroy class and create organic waste
    """
    pass
