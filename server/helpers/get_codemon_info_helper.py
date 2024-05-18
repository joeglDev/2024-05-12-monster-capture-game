from langchain_community.llms.ollama import Ollama

from classes.gen_ai.large_language_model import LargeLanguageModel
from server.helpers.get_codemon_from_id import get_codemon_from_id


def get_codemon_info_helper(codemon_id: int) -> str:
    codemon = get_codemon_from_id(codemon_id)

    model = LargeLanguageModel(llm=Ollama(model="orca-mini"), codemon=codemon)
    info = model.get_codemon_info()

    return info
