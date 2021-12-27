import json
import sys
import time

from ecoSymFunctions import *

from classes.animal import Animal
from classes.organic_waste import OrganicWaste
from classes.plant import Plant
from classes.meat import Meat
from classes.carnivore import Carnivore
from classes.herbivore import Herbivore
from classes.ecosystem import Ecosystem

# functions

# Create a new ecosystem
def createEcosystem(x, y):
    ecosystem = Ecosystem(x, y)
    return ecosystem

# Main application
def main():
    ecosystem = create_ecosystem(100, 50)
    screen = create_screen(ecosystem)

    # main application loop:
    while True:

        length = len(ecosystem.objects)
        # Simulation logic:
        for i in range(length):
            ecosystem = process_ecosystem(ecosystem.objects[i], ecosystem, grid)

def simulateNextStep(ecoSymDict) :
    ecosystem = createEcosystem(ecoSymDict["fieldSize"][0], ecoSymDict["fieldSize"][1])
    simGrid = creatGrid(ecosystem.size_x, ecosystem.size_y)
    addPopulation(ecoSymDict, ecosystem)
    for i in range(len(ecosystem.objects)) :
        ecosystem = process(ecoSymDict, ecosystem.objects[i], ecosystem, simGrid)
    newEcoSymDict = exportEcosystemToDict(ecoSymDict, ecosystem)
    return newEcoSymDict


if __name__ == "__main__":
    with open(sys.argv[1]) as json_file:
        data = json.load(json_file)
        print(simulateNextStep(data))
