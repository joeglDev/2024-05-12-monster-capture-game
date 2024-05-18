from classes.monsters.codemon import Codemon
from classes.monsters.statistics.id_codemon_map import id_codemon_map


def get_codemon_from_id(codemon_id) -> Codemon:
    # Check if the ID exists in the
    if codemon_id in id_codemon_map:
        codemon = id_codemon_map[codemon_id]()
    else:
        raise ValueError(f"ID {codemon_id} not found.")

    return codemon
