from langchain_community.llms import Ollama
from langchain_core.prompts import PromptTemplate

from classes.monsters.codemon import Codemon
from classes.monsters.thunderwyrm import ThunderWyrm

CODEMON_INFO_PROMPT = """
You are an encyclopedia on fantasy monsters called Codemon. They exist in the digital realm and come about though the stray thoughts of advanced computer systems.
Please discuss the biology and ecology of the following Codemon:
{codemon}
"""


class LargeLanguageModel:
    def __init__(self, llm: Ollama, codemon: Codemon):
        self.llm = llm
        self.codemon = codemon

    def get_codemon_info(self):
        prompt_template = PromptTemplate.from_template(CODEMON_INFO_PROMPT)
        prompt_with_context = prompt_template.format(
            codemon=self.codemon.get_attr_as_string()
        )

        completion: str = self.llm.invoke(prompt_with_context)
        return completion
