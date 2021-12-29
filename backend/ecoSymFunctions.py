import random
import uuid

from classes.carnivore import Carnivore
from classes.herbivore import Herbivore
from classes.animal import Animal
from classes.plant import Plant
from classes.life import Life
from classes.meat import Meat
from classes.organic_waste import OrganicWaste


def addPopulation (ecoSymDict, ecosystem) :
    for item in ecoSymDict["rounds"][-1] :
        lifeformDefault = ecoSymDict["lifeFormDefaults"][item["lifeform"]]
        if lifeformDefault["type"] == 0 :
            ecosystem.add_object(Carnivore(
                    item["UUID"],
                    item["lifeform"],
                    item["posX"],
                    item["posY"],
                    item["age"],
                    lifeformDefault["lifespan"],
                    item["HP"],
                    ecoSymDict["defaultHP"],
                    item["FP"],
                    ecoSymDict["defaultFP"],
                    item["gender"],
                    item["isPregnant"],
                    item["gestationCooldown"],
                    lifeformDefault["adultAt"],
                    lifeformDefault["visionRadius"],
                    lifeformDefault["contactRadius"],
                    lifeformDefault["maxMove"],
                    ))
        elif lifeformDefault["type"] == 1 :
            ecosystem.add_object(Herbivore(
                    item["UUID"],
                    item["lifeform"],
                    item["posX"],
                    item["posY"],
                    item["age"],
                    lifeformDefault["lifespan"],
                    item["HP"],
                    ecoSymDict["defaultHP"],
                    item["FP"],
                    ecoSymDict["defaultFP"],
                    item["gender"],
                    item["isPregnant"],
                    item["gestationCooldown"],
                    lifeformDefault["adultAt"],
                    lifeformDefault["visionRadius"],
                    lifeformDefault["contactRadius"],
                    lifeformDefault["maxMove"],
                    ))
        elif lifeformDefault["type"] == 2 :
            ecosystem.add_object(Plant(
                    item["UUID"],
                    item["lifeform"],
                    item["posX"],
                    item["posY"],
                    item["age"],
                    lifeformDefault["lifespan"],
                    item["HP"],
                    ecoSymDict["defaultHP"],
                    item["FP"],
                    ecoSymDict["defaultFP"],
                    lifeformDefault["adultAt"],
                    lifeformDefault["rootRadius"],
                    lifeformDefault["seedRadius"],
            ))
        elif lifeformDefault["type"] == 3 :
            ecosystem.add_object(Meat(
                    item["UUID"],
                    item["lifeform"],
                    item["posX"],
                    item["posY"],
                    lifeformDefault["FP"],
                    item["age"],
                    ecoSymDict["meatCompostAfter"],
            ))
            pass
        elif lifeformDefault["type"] == 4 :
            ecosystem.add_object(OrganicWaste(
                    item["UUID"],
                    item["lifeform"],
                    item["posX"],
                    item["posY"],
                    item["FP"]
                ))
        else :
            print("{} Not implemented yet !".format(ecoSymDict["types"][lifeformDefault["type"]]))

def exportEcosystemToDict(oldEcoSymDict, ecosystem) :
    newEcoSymDist = oldEcoSymDict
    newRound = []
    for item in ecosystem.objects :
        itemDict = {}
        itemDict["UUID"] = item.UUID
        itemDict["lifeform"] = item.lifeform
        itemDict["posX"] = item.x
        itemDict["posY"] = item.y
        itemDict["FP"] = item.energy_points
        if isinstance(item, Life) or isinstance(item, Meat) :
            itemDict["age"] = item.age
            if isinstance(item, Life): 
                itemDict["HP"] = item.health_points
                if isinstance(item, Animal) :
                    itemDict["gender"] = item.gender
                    # TODO
                    # * store if pregnant
                    # * store cooldown
                    itemDict["isPregnant"] = item.isPregnant
                    itemDict["gestationCooldown"] = item.gestationCooldown
        newRound.append(itemDict)

    if (len(newEcoSymDist["rounds"]) == 1) or (oldEcoSymDict["keepHistory"]):
        newEcoSymDist["rounds"].append(newRound)
    else :
        newEcoSymDist["rounds"][1] = newRound
        
    return newEcoSymDist

def creatGrid(x, y):
    grid = []
    for row in range(y):
        grid.append([])
        for column in range(x):
            grid[row].append(0)
    return grid

# Process each object in the ecosystem: feed, reproduce, move, ...
def process(ecoSymDict, object, ecosystem, grid):
    if isinstance(object, Animal):
        return animalProcess(ecoSymDict, object, ecosystem, grid)

    elif isinstance(object, Plant):
        return plantProcess(ecoSymDict, object, ecosystem, grid)

    elif type(object) == Meat:
        return meatProcess(ecoSymDict, object, ecosystem, grid)
    
    elif type(object) == OrganicWaste:
        return organicwasteProcess(ecoSymDict, object, ecosystem, grid)

    return ecosystem



def animalProcess(ecoSymDict, object, ecosystem, grid):
    # check if the animal is too old
    if object.age > object.lifespan:
        ecosystem.add_object(Meat(object.UUID, "meat", object.x, object.y, ecoSymDict["lifeFormDefaults"]["meat"]["FP"], 0, ecoSymDict["meatCompostAfter"]))
        ecosystem.remove_object(object)
        del object
        return ecosystem
    # check if the animal still has energy
    if object.energy_points <= 0:
        if object.health_points > 0:
            object.modify_health_points(-1)
            object.modify_energy(ecoSymDict["HPFPEquivalence"])
        else:
            ecosystem.add_object(Meat(object.UUID, "meat", object.x, object.y, ecoSymDict["lifeFormDefaults"]["meat"]["FP"], 0, ecoSymDict["meatCompostAfter"]))
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
            find_prey.modify_health_points(-1)
            object.modify_energy(-2)
    # eat
    if contacts["food"]:
        hunger = object.max_energy_points - object.energy_points
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
        elif not object.eat_meat():
            plant = random.choice(contacts["food"])
            find_plant = ecosystem.get_object_by_coord(plant[0], plant[1])
            food_energy = find_plant.energy
            if food_energy >= hunger:
                object.modify_energy(hunger)
                find_plant.modify_energy(-hunger)
            else:
                object.modify_energy(food_energy)
                find_plant.modify_energy(-food_energy)
    
    #reproduction
    if contacts["partners"]:
        # mate
        partner = random.choice(contacts["partners"])
        find_partner = ecosystem.get_object_by_coord(partner[0], partner[1])
        object.modify_energy(-2)
        find_partner.modify_energy(-2)
        whichGetsPregnant = object if (object.gender == ecoSymDict["lifeFormDefaults"][object.lifeform]["getsPregnant"]) else find_partner
        whichGetsPregnant.isPregnant = 1
        whichGetsPregnant.gestationCooldown = ecoSymDict["lifeFormDefaults"][whichGetsPregnant.lifeform]["reproduceCooldown"]
        
    # give birth if pregnant
    if(object.isPregnant == 1) :
        if(object.gestationCooldown == 0) :
            birthCoords = random.choice(is_empty(grid, contact_zone))
            ecosystem.add_object(type(object)(
                    str(uuid.uuid4()), 
                    object.lifeform, 
                    birthCoords[0], 
                    birthCoords[1], 
                    0,
                    ecoSymDict["lifeFormDefaults"][object.lifeform]["lifespan"], 
                    20, 
                    ecoSymDict["defaultHP"], 
                    20, 
                    ecoSymDict["defaultFP"], 
                    random.choice([0, 1]), 
                    0,
                    0,
                    ecoSymDict["lifeFormDefaults"][object.lifeform]["adultAt"], 
                    ecoSymDict["lifeFormDefaults"][object.lifeform]["visionRadius"], 
                    ecoSymDict["lifeFormDefaults"][object.lifeform]["contactRadius"], 
                    ecoSymDict["lifeFormDefaults"][object.lifeform]["maxMove"]))
            object.isPregnant = 0
        else :
            object.gestationCooldown -= 1
    
    # drop organic waste
    if is_empty(grid, contact_zone):
        drop = random.choice(is_empty(grid, contact_zone))
        if (random.randint(0, 100) <= ecoSymDict["organicwasteDropChance"]):
            ecosystem.add_object(OrganicWaste(str(uuid.uuid4()), "organicwaste", drop[0], drop[1], ecoSymDict["lifeFormDefaults"]["organicwaste"]["FP"]))
    
    # move
    seeked = seek(vision_zone, object, ecosystem)
    if seeked["partners"]:
        print("{} seeked partner !".format(object.UUID))
        new_pos = move(ecosystem, grid, object, seeked["partners"])
        object.make_move(new_pos)
        object.modify_energy(-2)
    elif seeked["food"]:
        print("{} seeked food !".format(object.UUID))
        new_pos = move(ecosystem, grid, object, seeked["food"])
        object.make_move(new_pos)
        object.modify_energy(-2)
    elif seeked["target_prey"]:
        print("{} seeked prey !".format(object.UUID))
        new_pos = move(ecosystem, grid, object, seeked["target_prey"])
        object.make_move(new_pos)
        object.modify_energy(-2)
    else:
        # random move
        print("{} moved randomly !".format(object.UUID))
        new_pos = random_move(ecosystem, grid, object)
        object.make_move(new_pos)
        object.modify_energy(-2)
    
    # increase age
    object.increase_age()
    
    # decrease energy with time
    object.modify_energy(-1)
    return ecosystem


def plantProcess(ecoSymDict, object, ecosystem, grid):
    # check if the plant is too old
    if object.age > object.lifespan:
        ecosystem.add_object(OrganicWaste(object.UUID, "organicwaste", object.x, object.y))
        ecosystem.remove_object(object)
        del object
        return ecosystem
    # check if the plant still has energy
    if object.energy_points <= 0:
        if object.health_points > 0:
            object.modify_health_points(-1)
            object.modify_energy(ecoSymDict["HPFPEquivalence"])
        else:
            ecosystem.add_object(OrganicWaste(object.UUID, "organicwaste", object.x, object.y))
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
        food_energy = find_organic_waste.energy_points
        hunger = object.max_energy_points - object.energy_points
        if food_energy >= hunger:
            object.modify_energy(hunger)
            find_organic_waste.modify_energy(-hunger)
            if(find_organic_waste.energy_points <= 0) :
                ecosystem.remove_object(find_organic_waste)
                del find_organic_waste
        else:
            object.modify_energy(food_energy)
            find_organic_waste.modify_energy(-food_energy)
            if(find_organic_waste.energy_points <= 0) :
                ecosystem.remove_object(find_organic_waste)
                del find_organic_waste

    # seed
    if object.age >= object.adultAt:
        if is_empty(grid, seed_zone):
            seed = random.choice(is_empty(grid, seed_zone))
            ecosystem.add_object(type(object)(
                    str(uuid.uuid4()),
                    object.lifeform,
                    seed[0],
                    seed[1],
                    0,
                    object.lifespan,
                    object.health_points,
                    object.max_health_points,
                    object.energy_points,
                    object.max_energy_points,
                    object.adultAt,
                    object.root_radius,
                    object.seed_radius))
    # increase age
    object.increase_age()
    # decrease energy with time
    object.modify_energy(-1)
    return ecosystem


def meatProcess(ecoSymDict, object, ecosystem, grid):
    # check if meat is rot
    if object.age >= object.rotsAt:
        ecosystem.add_object(OrganicWaste(object.UUID, "organicwaste", object.x, object.y))
        ecosystem.remove_object(object)
        del object
        return ecosystem
    # check if meat still has energy
    if object.energy_points == 0:
        if object.health_points > 0:
            object.modify_health_points(-1)
            object.modify_energy(ecoSymDict["HPFPEquivalence"])
        else:
            ecosystem.add_object(OrganicWaste(object.UUID, "organicwaste", object.x, object.y))
            ecosystem.remove_object(object)
            del object
            return ecosystem
    # decrease energy with time
    object.modify_energy(-1)
    # increase age
    object.increase_age()
    return ecosystem


def organicwasteProcess(ecoSymDict, object, ecosystem, grid):
    if(object.energy_points <= 0):
        ecosystem.remove_object(object)
        del object
        return ecosystem
    object.modify_energy(-1)
    return ecosystem

# Find objects in a specified zone
def seek(zone, object, ecosystem):
    contacts = {"target_prey": [], "food": [], "partners": []}
    for coord in zone:
        find_object = ecosystem.get_object_by_coord(coord[0], coord[1])
        if object.age >= object.adultAt:
            if (type(object) == type(find_object)) and (object.lifeform == find_object.lifeform) and (find_object.age >= object.adultAt) and (object.gender != find_object.gender) and (find_object.isPregnant == 0):
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


# Return a list of organic waste inside the root zone
def organic_waste_in_root_zone(zone, ecosystem):
    waste = []
    for coord in zone:
        find_object = ecosystem.get_object_by_coord(coord[0], coord[1])
        if type(find_object) == OrganicWaste:
            waste.append(coord)
    return waste


# Check if coordinates are empty""
def is_empty(grid, list):
    empty = []
    for coord in list:
        if grid[coord[1]][coord[0]] == 0:
            empty.append(coord)
    return empty


# Find a random move
def random_move(ecosystem, grid, object):
    possible = []
    for i in range(object.max_move):
        for j in range(object.max_move):
            if object.x+i in range(ecosystem.size_x) and object.y+j in range(ecosystem.size_y):
                possible.append([object.x+i, object.y+j])
            if object.x-i in range(ecosystem.size_x) and object.y-j in range(ecosystem.size_y):
                possible.append([object.x-i, object.y-j])
    filtered_possible = is_empty(grid, possible)
    if filtered_possible != possible :
        print(object.UUID)
        print(possible)
        print(filtered_possible)
    return random.choice(filtered_possible)


# find a valid move to a target
def move(ecosystem, grid, object, list):
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
