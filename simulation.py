import params
import random

from classes.animal import Animal
from classes.plant import Plant
from classes.organic_waste import OrganicWaste
from classes.meat import Meat

from classes.wolf import Wolf
from classes.sheep import Sheep
from classes.carrot import Carrot


def seek(zone, object, ecosystem):
    """find objects in a specified zone"""
    contacts = {"target_prey": [], "food": [], "partners": []}
    for coord in zone:
        find_object = ecosystem.get_object_by_coord(coord[0], coord[1])
        if object.age >= params.gestation_age:
            if type(object) == type(find_object):
                if find_object.age >= params.gestation_age:
                    if object.gender != find_object.gender:
                        contacts["partners"].append(coord)
        if object.eat_meat():
            if isinstance(find_object, Animal):
                if type(object) != type(find_object):
                    contacts["target_prey"].append(coord)
            elif type(object) == Meat:
                contacts["food"].append(coord)
        elif object.eat_meat() is False:
            if isinstance(object, Plant):
                contacts["food"].append(coord)
    return contacts


def organic_waste_in_root_zone(zone, ecosystem):
    """return a list of organic waste inside the root zone"""
    waste = []
    for coord in zone:
        find_object = ecosystem.get_object_by_coord(coord[0], coord[1])
        if type(find_object) == OrganicWaste:
            waste.append(coord)
    return waste


def is_empty(grid, list):
    """check if coordinates are empty"""
    empty = []
    for coord in list:
        if grid[coord[1]][coord[0]] == 0:
            empty.append(coord)
    return empty


def random_move(ecosystem, grid, object):
    """find a random move"""
    possible = []
    for i in range(object.max_move):
        for j in range(object.max_move):
            if object.x+i in range(ecosystem.size_x) and object.y+j in range(ecosystem.size_y):
                possible.append([object.x+i, object.y+j])
            if object.x-i in range(ecosystem.size_x) and object.y-j in range(ecosystem.size_y):
                possible.append([object.x-i, object.y-j])
    filtered_possible = is_empty(grid, possible)
    return random.choice(filtered_possible)


def move(ecosystem, grid, object, list):
    """find a valid move to a target"""
    target = random.choice(list)
    find_target = ecosystem.get_object_by_coord(target[0], target[1])
    target_contact_zone = find_target.get_contact_zone([ecosystem.size_x, ecosystem.size_y])
    if target_contact_zone:
        if is_empty(grid, target_contact_zone):
            target_coord = random.choice(is_empty(grid, target_contact_zone))
            if abs(target_coord[0] - object.x) > object.max_move:
                if (target_coord[0] - object.x) > 0:
                    target_coord[0] = object.x + object.max_move
                else:
                    target_coord[0] = object.x - object.max_move
            if abs(target_coord[1] - object.y) > object.max_move:
                if (target_coord[1] - object.y) > 0:
                    target_coord[1] = object.y + object.max_move
                else:
                    target_coord[1] = object.y - object.max_move
            return target_coord
        else:
            target_coord = random_move(ecosystem, grid, object)
    else:
        target_coord = random_move(ecosystem, grid, object)
    return target_coord


def process_ecosystem(object, ecosystem, grid):
    """process each object in the ecosystem: feed, reproduce, move, ..."""
    if isinstance(object, Animal):
        # check if the animal is too old
        if object.age > object.max_age:
            ecosystem.add_object(Meat(object.x, object.y, 0))
            ecosystem.remove_object(object)
            del object
            return ecosystem
        # check if the animal still has energy
        if object.energy == 0:
            if object.life_points > 0:
                object.modify_life_points(-1)
                object.modify_energy(params.life_points_to_energy)
            else:
                ecosystem.add_object(Meat(object.x, object.y, 0))
                ecosystem.remove_object(object)
                del object
                return ecosystem
        # get available food, partners, preys
        contact_zone = object.get_contact_zone([ecosystem.size_x, ecosystem.size_y])
        vision_zone = object.get_vision_zone([ecosystem.size_x, ecosystem.size_y])
        contacts = seek(contact_zone, object, ecosystem)
        # attack
        if object.eat_meat():
            if contacts["target_prey"]:
                prey = random.choice(contacts["target_prey"])
                find_prey = ecosystem.get_object_by_coord(prey[0], prey[1])
                find_prey.modify_life_points(-1)
                object.modify_energy(-2)
        # eat
        if contacts["food"]:
            hunger = object.max_energy - object.energy
            if object.eat_meat():
                meat = random.choice(contacts["food"])
                find_meat = ecosystem.get_object_by_coord(meat[0], meat[1])
                food_energy = find_meat.energy
                if food_energy >= hunger:
                    object.modify_energy(hunger)
                    find_meat.modify_energy(-hunger)
                else:
                    object.modify_energy(food_energy)
                    find_meat.modify_energy(-food_energy)
            elif object.eat_meat() is False:
                plant = random.choice(contacts["food"])
                find_plant = ecosystem.get_object_by_coord(plant[0], plant[1])
                food_energy = find_plant.energy
                if food_energy >= hunger:
                    object.modify_energy(hunger)
                    find_plant.modify_energy(-hunger)
                else:
                    object.modify_energy(food_energy)
                    find_plant.modify_energy(-food_energy)
        # reproduce
        if contacts["partners"]:
            partner = random.choice(contacts["partners"])
            find_partner = ecosystem.get_object_by_coord(partner[0], partner[1])
            object.modify_energy(-2)
            find_partner.modify_energy(-2)
            birth = random.choice(is_empty(grid, contact_zone))
            ecosystem.add_object(type(object)(birth[0], birth[1], 0, random.choice(["male", "female"])))

        # drop organic waste
        if is_empty(grid, contact_zone):
            drop = random.choice(is_empty(grid, contact_zone))
            ecosystem.add_object(OrganicWaste(drop[0], drop[1]))
        # move
        seeked = seek(vision_zone, object, ecosystem)
        if seeked["partners"]:
            new_pos = move(ecosystem, grid, object, seeked["partners"])
            object.make_move(new_pos)
            object.modify_energy(-2)
        elif seeked["food"]:
            new_pos = move(ecosystem, grid, object, seeked["food"])
            object.make_move(new_pos)
            object.modify_energy(-2)
        elif seeked["target_prey"]:
            new_pos = move(ecosystem, grid, object, seeked["target_prey"])
            object.make_move(new_pos)
            object.modify_energy(-2)
        else:
            # random move
            new_pos = random_move(ecosystem, grid, object)
            object.make_move(new_pos)
            object.modify_energy(-2)
        # increase age
        object.increase_age()
        # decrease energy with time
        object.modify_energy(-1)

    elif isinstance(object, Plant):
        # check if the animal is too old
        if object.age > object.max_age:
            ecosystem.add_object(OrganicWaste(object.x, object.y))
            ecosystem.remove_object(object)
            del object
            return ecosystem
        # check if the plant still has energy
        if object.energy == 0:
            if object.life_points > 0:
                object.modify_life_points(-1)
                object.modify_energy(params.life_points_to_energy)
            else:
                ecosystem.add_object(OrganicWaste(object.x, object.y))
                ecosystem.remove_object(object)
                del object
                return ecosystem
        root_zone = object.get_root_zone([ecosystem.size_x, ecosystem.size_y])
        seed_zone = object.get_seed_zone([ecosystem.size_x, ecosystem.size_y])
        # eat
        food_list = organic_waste_in_root_zone(root_zone, ecosystem)
        if food_list:
            organic_waste = random.choice(food_list)
            find_organic_waste = ecosystem.get_object_by_coord(organic_waste[0], organic_waste[1])
            food_energy = find_organic_waste.energy
            hunger = object.max_energy - object.energy
            if food_energy >= hunger:
                object.modify_energy(hunger)
                find_organic_waste.modify_energy(-hunger)
            else:
                object.modify_energy(food_energy)
                find_organic_waste.modify_energy(-food_energy)
        # seed
        if object.age >= object.min_seed_age:
            if is_empty(grid, seed_zone):
                seed = random.choice(is_empty(grid, seed_zone))
                ecosystem.add_object(type(object)(seed[0], seed[1], 0))
        # increase age
        object.increase_age()
        # decrease energy with time
        object.modify_energy(-1)

    elif type(object) == Meat:
        # check if meat is rot
        if object.age >= object.meat_rot_age:
            ecosystem.add_object(OrganicWaste(object.x, object.y))
            ecosystem.remove_object(object)
            del object
            return ecosystem
        # check if meat still has energy
        if object.energy == 0:
            if object.life_points > 0:
                object.modify_life_points(-1)
                object.modify_energy(params.life_points_to_energy)
            else:
                ecosystem.add_object(OrganicWaste(object.x, object.y))
                ecosystem.remove_object(object)
                del object
                return ecosystem
        # decrease energy with time
        object.modify_energy(-1)
        # increase age
        object.increase_age()

    return ecosystem
