import time

from simulation import process_ecosystem
from generation import generate

from classes.animal import Animal
from classes.organic_waste import OrganicWaste
from classes.plant import Plant
from classes.meat import Meat
from classes.carnivore import Carnivore
from classes.herbivore import Herbivore
from classes.ecosystem import Ecosystem

# functions

# Create a new ecosystem
def create_ecosystem(x, y):
    ecosystem = Ecosystem(x, y)
    generate(ecosystem)
    return ecosystem


# Create a grid to display in pygame
def create_grid(x, y):

    grid = []
    for row in range(y):
        grid.append([])
        for column in range(x):
            grid[row].append(0)
    return grid


<<<<<<< HEAD
=======
# Add objects to grid
def update_grid(ecosystem, grid):
    for object in ecosystem.objects:
        if isinstance(object, Wolf):
            grid[object.y][object.x] = 1
        elif isinstance(object, Carrot):
            grid[object.y][object.x] = 2
        elif type(object) == Meat:
            grid[object.y][object.x] = 3
        elif type(object) == OrganicWaste:
            grid[object.y][object.x] = 4
        elif isinstance(object, Sheep):
            grid[object.y][object.x] = 5
    return grid

>>>>>>> e1e2086abf2e46de48215749ae6b3a6d0d8163c1

# Main application
def main():
    ecosystem = create_ecosystem(100, 50)
    screen = create_screen(ecosystem)

    # generate grid
    grid = create_grid(ecosystem.size_x, ecosystem.size_y)
    grid = update_grid(ecosystem, grid)

    # main application loop:
    while True:

        length = len(ecosystem.objects)
        # Simulation logic:
        for i in range(length):
            ecosystem = process_ecosystem(ecosystem.objects[i], ecosystem, grid)


if __name__ == "__main__":
    main()
