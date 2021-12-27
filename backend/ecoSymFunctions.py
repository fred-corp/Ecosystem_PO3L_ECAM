from classes.carnivore import Carnivore
from classes.herbivore import Herbivore
from classes.plant import Plant
from classes.meat import Meat
from classes.organic_waste import OrganicWaste


def addPopulation (ecoSymDict, ecosystem) :
    for item in ecoSymDict["rounds"][-1] :
        lifeformDefault = ecoSymDict["lifeFormDefaults"][item["lifeform"]]
        if lifeformDefault["type"] == 0 :
            ecosystem.add_object(Carnivore(
                    item["UUID"],
                    item["posX"],
                    item["posY"],
                    item["age"],
                    lifeformDefault["lifespan"],
                    item["HP"],
                    ecoSymDict["defaultHP"],
                    item["FP"],
                    ecoSymDict["defaultHP"],
                    item["gender"],
                    lifeformDefault["getsPregnant"],
                    lifeformDefault["visionRadius"],
                    lifeformDefault["contactRadius"],
                    lifeformDefault["maxMove"],
                    ))
        elif lifeformDefault["type"] == 1 :
            ecosystem.add_object(Herbivore(
                    item["UUID"],
                    item["posX"],
                    item["posY"],
                    item["age"],
                    lifeformDefault["lifespan"],
                    item["HP"],
                    ecoSymDict["defaultHP"],
                    item["FP"],
                    ecoSymDict["defaultHP"],
                    item["gender"],
                    lifeformDefault["getsPregnant"],
                    lifeformDefault["visionRadius"],
                    lifeformDefault["contactRadius"],
                    lifeformDefault["maxMove"],
                    ))
        else :
            print("{} Not implemented yet !".format(ecoSymDict["types"][lifeformDefault["type"]]))
    print(ecosystem)
