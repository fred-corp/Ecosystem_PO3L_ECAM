from classes.energy import Energy


class Meat(Energy):
    def __init__(self, amount, age):
        super().__init__(amount)
        self.age = age
