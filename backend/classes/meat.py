from classes.energy import Energy


class Meat(Energy):
    def __init__(self, uid, amount, age, pos_x, pos_y):
        super().__init__(uid, amount, pos_x, pos_y)
        self.age = age
