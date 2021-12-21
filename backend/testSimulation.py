import json
import os

from classes.animal import Animal
from classes.plant import Plant

class_list = []

path = os.path.dirname(os.path.abspath(__file__)).removesuffix("backend")

ecosystem_path = os.path.join(path, "ecosystemExampleFiles", "example1.json")

with open(ecosystem_path) as file:
    data = json.load(file)
    rounds = data["rounds"]

    rows, cols = data["fieldSize"][0], data["fieldSize"][1]
    ecosystem = [([0]*cols) for i in range(rows)]

    for life in rounds[0]:
        life_data = data["lifeDefaults"][life[1]]
        if life_data["species"] == "animal":
            class_list.append(
                Animal(
                    life[0],
                    life[6],
                    life[7],
                    life[5],
                    life[2],
                    life_data["diet"],
                    data["visionRadius"],
                    data["contactRadius"],
                    life_data["hierarchy"],
                    life[8],
                    life[9],
                )
            )
            ecosystem[life[8]][life[9]] = life[0]
        elif life_data["species"] == "plant":
            class_list.append(
                Plant(
                    life[0],
                    life[6],
                    life[7],
                    life[5],
                    life[2],
                    data["contactRadius"],
                    data["rootRadius"],
                    data["seedRadius"],
                    "organicwaste",
                    life[8],
                    life[9],
                )
            )

# print(ecosystem)


def seek():
    """return a list of predators, preys or food inside the vision zone
    of an animal
    """
    pass


def find_contacts(sort, diet, zone, hierarchy, gender):
    """return a dict with:
    - for a carnivore: animals to attack, animals to reproduce with
    - for a herbivore: plants to eat, animals to reproduce with
    - for a plant: plants to reproduce with
    """
    contact_list = {"food": [], "partners": []}
    for coord in zone:
        if ecosystem[coord[0]][coord[1]] != 0:
            if sort == "animal":
                for life in class_list:
                    if life.uid == ecosystem[coord[0]][coord[1]]:
                        # find plants for a herbivore
                        if diet == 0 and type(life) == Plant:
                            contact_list["food"].append(coord)
                            break
                        # find animals to reproduce with
                        # todo: check age, race and break
                        if life.gender != gender:
                            pass
                        # find animals to attack for a carnivore
                        if diet == 1 and type(life) == Animal:
                            if life.hierarchy < hierarchy:
                                contact_list["food"].append(coord)
                                break
            elif sort == "plant":
                pass
    return contact_list


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
    """"move an animal (to food or to reproduce or random)"""
    pass


def lower_energy_reserve():
    """decrease energy reserve each round"""
    pass


def convert_life_point():
    """convert health points to energy reserve if energy reserve is empty"""
    pass


def die():
    """die if health points are 0
    - animal: destroy class and create meat
    - plant: destroy class and create organic waste
    - meat: destroy class and create organic waste
    """
    pass


for life in class_list:
    if type(life) == Animal:
        contacts = find_contacts(
            "animal",
            life.food_type,
            life.get_contact_zone(rows, cols),
            life.hierarchy,
            life.gender
            )
        print(contacts)

    elif type(life) == Plant:
        contacts = find_contacts(
            "plant",
            life.food_type,
            life.get_contact_zone(rows, cols),
            0,
            life.gender
            )
    # simulation order:
    # - seek
    # - attack
    # - eat
    # - reproduce
    # - drop organic waste
    # - move
