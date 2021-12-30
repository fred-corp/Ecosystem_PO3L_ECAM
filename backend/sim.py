import json
import sys

from ecoSymFunctions import creatGrid, addPopulation, updateGrid, process, exportEcosystemToDict

from classes.ecosystem import Ecosystem

# functions

# Create a new ecosystem
def createEcosystem(x, y):
    ecosystem = Ecosystem(x, y)
    return ecosystem


def simulateNextStep(ecoSymDict) :
    ecosystem = createEcosystem(ecoSymDict["fieldSize"][0], ecoSymDict["fieldSize"][1])
    simGrid = creatGrid(ecosystem.size_x, ecosystem.size_y)
    addPopulation(ecoSymDict, ecosystem)
    for i in range(len(ecosystem.objects)) :
        simGrid = updateGrid(simGrid, ecosystem)
        ecosystem = process(ecoSymDict, ecosystem.objects[i], ecosystem, simGrid)
    newEcoSymDict = exportEcosystemToDict(ecoSymDict, ecosystem)
    return newEcoSymDict


if __name__ == "__main__":
    with open(sys.argv[1]) as json_file:
        data = json.load(json_file)
        newData = simulateNextStep(data)
        with open('private/ecosystem.json', 'w') as outputFile:
            print(newData)
            outputFile.write(json.dumps(newData, indent=2))
