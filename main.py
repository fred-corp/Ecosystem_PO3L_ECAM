import pygame
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

from classes.wolf import Wolf
from classes.carrot import Carrot
from classes.sheep import Sheep


# pygame parameters
BROWN = (100, 40, 0)
GREEN = (0, 255, 0)
WIDTH = 15
HEIGHT = 15

# initialise pygame
pygame.init()
pygame.display.set_caption("Ecosystem")
clock = pygame.time.Clock()


# functions
def create_ecosystem(x, y):
    """create a new ecosystem"""
    ecosystem = Ecosystem(x, y)
    generate(ecosystem)
    return ecosystem


def create_grid(x, y):
    """create a grid to display in pygame"""
    grid = []
    for row in range(y):
        grid.append([])
        for column in range(x):
            grid[row].append(0)
    return grid


def update_grid(ecosystem, grid):
    """add objects to grid"""
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


def create_screen(ecosystem):
    """create pygame screen"""
    WINDOW_SIZE = [ecosystem.size_x*WIDTH, ecosystem.size_y*HEIGHT]
    screen = pygame.display.set_mode(WINDOW_SIZE)
    screen.fill(GREEN)
    return screen


def main():
    """main application"""
    ecosystem = create_ecosystem(100, 50)
    screen = create_screen(ecosystem)

    # import images 
    wolf_image = pygame.image.load('./ressources/wolf.png').convert_alpha()
    wolf_image = pygame.transform.scale(wolf_image, (15, 15))
    meat_image = pygame.image.load('./ressources/meat.png').convert_alpha()
    meat_image = pygame.transform.scale(meat_image, (15, 15))
    carrot_image = pygame.image.load('./ressources/carrot.png').convert_alpha()
    carrot_image = pygame.transform.scale(carrot_image, (15, 15))
    sheep_image = pygame.image.load('./ressources/sheep.png').convert_alpha()
    sheep_image = pygame.transform.scale(sheep_image, (15, 15))

    # main application loop:
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

        # generate grid
        grid = create_grid(ecosystem.size_x, ecosystem.size_y)
        grid = update_grid(ecosystem, grid)

        length = len(ecosystem.objects)
        # Simulation logic:
        for i in range(length):
            ecosystem = process_ecosystem(ecosystem.objects[i], ecosystem, grid)
            # update grid
            grid = create_grid(ecosystem.size_x, ecosystem.size_y)
            grid = update_grid(ecosystem, grid)
            # Draw the grid
            for row in range(ecosystem.size_y):
                for column in range(ecosystem.size_x):
                    if grid[row][column] == 1:
                        rect = wolf_image.get_rect()
                        rect.center = (WIDTH * column+7, HEIGHT * row+7)
                        screen.blit(wolf_image, rect)
                    elif grid[row][column] == 2:
                        rect = carrot_image.get_rect()
                        rect.center = (WIDTH * column+7, HEIGHT * row+7)
                        screen.blit(carrot_image, rect)
                    elif grid[row][column] == 3:
                        rect = meat_image.get_rect()
                        rect.center = (WIDTH * column+7, HEIGHT * row+7)
                        screen.blit(meat_image, rect)
                    elif grid[row][column] == 4:
                        pygame.draw.rect(screen,
                                        BROWN,
                                        [WIDTH * column,
                                        HEIGHT * row,
                                        WIDTH,
                                        HEIGHT])
                    elif grid[row][column] == 5:
                        rect = meat_image.get_rect()
                        rect.center = (WIDTH * column+7, HEIGHT * row+7)
                        screen.blit(sheep_image, rect)
                    else:
                        pygame.draw.rect(screen,
                                        GREEN,
                                        [WIDTH * column,
                                        HEIGHT * row,
                                        WIDTH,
                                        HEIGHT])
            time.sleep(0.1)
            pygame.display.update()
        # Limit to 60 frames per second
        clock.tick(60)
        pygame.display.flip()


if __name__ == "__main__":
    main()
