import random
import params

from classes.wolf import Wolf
from classes.carrot import Carrot
from classes.sheep import Sheep

def generate(ecosystem):
    "generate an initial population"
    ecosystem.add_object(Wolf(
                            random.randint(0, ecosystem.size_x-1),
                            random.randint(0, ecosystem.size_y-1),
                            0,
                            random.choice(params.genders)
                            ))
    ecosystem.add_object(Wolf(
                            random.randint(0, ecosystem.size_x-1),
                            random.randint(0, ecosystem.size_y-1),
                            0,
                            random.choice(params.genders)
                            ))
    ecosystem.add_object(Wolf(
                            random.randint(0, ecosystem.size_x-1),
                            random.randint(0, ecosystem.size_y-1),
                            0,
                            random.choice(params.genders)
                            ))
    ecosystem.add_object(Wolf(
                            random.randint(0, ecosystem.size_x-1),
                            random.randint(0, ecosystem.size_y-1),
                            0,
                            random.choice(params.genders)
                            ))
    ecosystem.add_object(Wolf(
                            random.randint(0, ecosystem.size_x-1),
                            random.randint(0, ecosystem.size_y-1),
                            0,
                            random.choice(params.genders)
                            ))
    ecosystem.add_object(Wolf(
                            random.randint(0, ecosystem.size_x-1),
                            random.randint(0, ecosystem.size_y-1),
                            0,
                            random.choice(params.genders)
                            ))

    ecosystem.add_object(Carrot(
                            random.randint(0, ecosystem.size_x-1),
                            random.randint(0, ecosystem.size_y-1),
                            0,
                            ))
    ecosystem.add_object(Carrot(
                            random.randint(0, ecosystem.size_x-1),
                            random.randint(0, ecosystem.size_y-1),
                            0,
                            ))
    ecosystem.add_object(Carrot(
                            random.randint(0, ecosystem.size_x-1),
                            random.randint(0, ecosystem.size_y-1),
                            0,
                            ))
    ecosystem.add_object(Carrot(
                            random.randint(0, ecosystem.size_x-1),
                            random.randint(0, ecosystem.size_y-1),
                            0,
                            ))                        
    ecosystem.add_object(Sheep(
                            random.randint(0, ecosystem.size_x-1),
                            random.randint(0, ecosystem.size_y-1),
                            0,
                            random.choice(params.genders)
                            ))
    ecosystem.add_object(Sheep(
                            random.randint(0, ecosystem.size_x-1),
                            random.randint(0, ecosystem.size_y-1),
                            0,
                            random.choice(params.genders)
                            ))
    ecosystem.add_object(Sheep(
                            random.randint(0, ecosystem.size_x-1),
                            random.randint(0, ecosystem.size_y-1),
                            0,
                            random.choice(params.genders)
                            ))
    ecosystem.add_object(Sheep(
                            random.randint(0, ecosystem.size_x-1),
                            random.randint(0, ecosystem.size_y-1),
                            0,
                            random.choice(params.genders)
                            ))
    ecosystem.add_object(Sheep(
                            random.randint(0, ecosystem.size_x-1),
                            random.randint(0, ecosystem.size_y-1),
                            0,
                            random.choice(params.genders)
                            ))
    ecosystem.add_object(Sheep(
                            random.randint(0, ecosystem.size_x-1),
                            random.randint(0, ecosystem.size_y-1),
                            0,
                            random.choice(params.genders)
                            ))
    return ecosystem