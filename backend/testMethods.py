import json
import os

from classes.animal import Animal

class_list = []

path = os.path.dirname(os.path.abspath(__file__)).removesuffix("backend")

ecosystem_path = os.path.join(path, "ecosystemExampleFiles", "example1.json")

with open(ecosystem_path) as file:
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
                    life_data["diet"],
                )
            )
        elif life_data["species"] == "plant":
            pass

print(class_list)
