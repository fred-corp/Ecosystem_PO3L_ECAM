import json
import os
import random

from classes.animal import Animal
from classes.plant import Plant
from classes.meat import Meat

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
            if life[5] > data["lifeDefaults"][life[1]]["gestation"]:
                gestated = True
            else:
                gestated = False
            class_list.append(
                Animal(
                    life[0],
                    data["lifeDefaults"][life[1]],
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
                    gestated,
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


def find_contacts(sort, diet, zone, hierarchy, gender, gestated, specie):
    """return a dict with:
    - for a carnivore: animals to attack, animals to reproduce with
    - for a herbivore: plants to eat, animals to reproduce with
    - for a plant: plants to reproduce with
    """
    contact_list = {"prey": [], "meat": [], "partners": []}
    for coord in zone:
        if ecosystem[coord[0]][coord[1]] != 0:
            if sort == "animal":
                for life in class_list:
                    if life.uid == ecosystem[coord[0]][coord[1]]:
                        # find plants for a herbivore
                        if diet == 0 and type(life) == Plant:
                            contact_list["prey"].append(coord)
                            break
                        # find animals to reproduce with
                        if gestated is True and life.gestated is True:
                            if life.gender != gender and specie == life.specie:
                                contact_list["partners"].append(coord)
                                break
                        # find animals to attack for a carnivore
                        if diet == 1 and type(life) == Animal:
                            if life.hierarchy < hierarchy:
                                contact_list["prey"].append(coord)
                                break
                        # todo: add meat
            elif sort == "plant":
                if gestated is True:
                    for life in class_list:
                        if life.uid == ecosystem[coord[0]][coord[1]]:
                            if life.gender != gender and life.gestated is True:
                                contact_list["partners"].append(coord)
                                break
    return contact_list


def attack(contacts):
    """reduce hp of an animal
    - for a carnivore: attack an animal with a lower hierarchy inside the
    contact zone
    """
    preys = contacts["prey"]

    target = random.choice(preys)

    for life in class_list:
        if life.uid == ecosystem[target[0]][target[1]]:
            # change food drop amount
            class_list.append(Meat(life.uid, 10, 0, life.pos_x, life.pos_y))
            del life


def eat():
    """modify the energy reserve of a life
    - for a carnivore: eat meat inside the contact zoneP
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
            life.gender,
            life.gestated,
            life.specie
            )
        if life.diet == 1:
            attack(contacts)
        # eat()
        # reproduce()
        # drop_organicwaste()
        # move()

    elif type(life) == Plant:
        contacts = find_contacts(
            "plant",
            life.food_type,
            life.get_contact_zone(rows, cols),
            0,
            life.gender,
            life.gestated,
            life.specie
            )