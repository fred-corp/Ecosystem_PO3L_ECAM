import json
import time
import sys

from simulation import process_ecosystem
from ecoSymFunctions import addPopulation

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
    addPopulation(ecoSymDict, ecosystem)
    newEcoSymDict = {}
    return newEcoSymDict


if __name__ == "__main__":
    with open(sys.argv[1]) as json_file:
        data = json.load(json_file)
        simulateNextStep(data)
