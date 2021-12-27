import random

# generate an initial population
def generate(ecosystem):
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