from abc import ABC


class Energy(ABC):
    def __init__(self, amount):
        self.amount = amount
