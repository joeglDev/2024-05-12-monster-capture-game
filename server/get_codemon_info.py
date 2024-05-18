from langchain_community.llms.ollama import Ollama

from classes.gen_ai.large_language_model import LargeLanguageModel
from classes.monsters.codemon import Codemon
from classes.monsters.statistics.id_codemon_map import id_codemon_map


def get_codemon_info_helper(codemon_id: int) -> str:
    # Check if the ID exists in the
    codemon: Codemon | None = None
    if codemon_id in id_codemon_map:
        codemon = id_codemon_map[codemon_id]()
    else:
        raise ValueError(f"ID {codemon_id} not found.")

    model = LargeLanguageModel(llm=Ollama(model="orca-mini"), codemon=codemon)
    info = model.get_codemon_info()

    return info
