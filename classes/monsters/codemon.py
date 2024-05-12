from abc import abstractmethod
from enum import Enum

from classes.monsters.statistics.species import Species
from classes.monsters.statistics.element import Element


class Codemon:
    def __init__(
        self,
        own_species: Species | None = None,
        name: str = "Codemon",
        element: Element | None = None,
        health: int = 100,
        strength: int = 100,
        armour: int = 100,
        intelligence: int = 100,
        speed: int = 100,
    ):
        self.own_species = own_species
        self.name = name
        self.element = element
        self.health = health
        self.strength = strength
        self.armour = armour
        self.intelligence = intelligence
        self.speed = speed
        self.current_health = health

    def print_attributes(self):
        properties = vars(self)
        for property_name, property_value in properties.items():
            print(f"{property_name}: {property_value}")
