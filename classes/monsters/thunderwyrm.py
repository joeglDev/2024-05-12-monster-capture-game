from classes.monsters.codemon import Codemon
from classes.monsters.statistics.element import Element
from classes.monsters.statistics.species import Species


class ThunderWyrm(Codemon):
    def __init__(
        self,
        own_species: str = Species.ElectricStarter1.value,
        name: str = "Thunderwyrm",
        element: str = Element.Electric.value,
        health: int = 25,
        strength: int = 3,
        armour: int = 3,
        intelligence: int = 7,
        speed: int = 7,
        is_starter: bool = True,
        can_upgrade: bool = True,
    ):
        super().__init__(
            own_species,
            name,
            element,
            health,
            strength,
            armour,
            intelligence,
            speed,
            is_starter,
            can_upgrade,
        )
