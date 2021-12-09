from abc import ABC, abstractclassmethod


class Energy(ABC):
    def __init__(self, amount):
        self.amount = amount
