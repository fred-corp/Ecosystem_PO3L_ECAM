import json
import sys

from classes.animal import Animal

class_list = []

with open (sys.path[4] + "\Ecosystem_PO3L_ECAM\ecosystemExampleFiles\example1.json") as file:
    data = json.load(file)
    rounds = data["rounds"]
    for life in rounds[0]:
        life_data = data["lifeDefaults"][life[1]]
        if life_data["species"] == "animal":
            class_list.append(
                Animal(
                    life[6],
                    life[7],
                    life[5],
                    life[2],
                    data["visionRadius"],
                    data["contactRadius"],
                    life_data["hierarchy"],
                    life_data["diet"]
                )
            )
        elif life_data["species"] == "plant":
            pass