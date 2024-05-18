from dataclasses import dataclass

from classes.monsters.statistics.element import Element
from classes.monsters.statistics.species import Species
from server.helpers.get_codemon_from_id import get_codemon_from_id


@dataclass
class CodemonStatsResponse:
    name: str
    element: Element
    health: int
    strength: int
    armour: int
    intelligence: int
    speed: int
    is_starter: bool
    can_upgrade: bool
    species: Species
    codemon_id: int


def get_codemon_stats_helper(codemon_id: int) -> CodemonStatsResponse:
    codemon = get_codemon_from_id(codemon_id)
    res = CodemonStatsResponse(
        name=codemon.name,
        element=codemon.element,
        health=codemon.health,
        strength=codemon.strength,
        armour=codemon.armour,
        intelligence=codemon.intelligence,
        speed=codemon.speed,
        species=codemon.own_species,
        is_starter=codemon.is_starter,
        can_upgrade=codemon.can_upgrade,
        codemon_id=codemon_id,
    )

    return res
