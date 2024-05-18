from abc import abstractmethod
from enum import Enum
from typing import Any, List

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
        is_starter: bool = False,
        can_upgrade: bool = False,
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
        self.is_starter = is_starter
        self.can_upgrade = can_upgrade

    def print_attributes(self) -> dict[str, Any]:
        properties = vars(self)

        for property_name, property_value in properties.items():
            print(f"{property_name}: {property_value}")

        return properties

    def get_attr_as_string(self) -> str:
        all_info: List[str] = []

        for key, value in vars(self).items():
            item = f"{key}: {value}"
            all_info.append(item)

        merged_info = ", ".join(all_info)
        return merged_info
