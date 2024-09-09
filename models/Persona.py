from models.OpenAiLlm import OpenAiLlm

class Persona:
    def __init__(self, background):
        self.background = background
        self.llm = OpenAiLlm(background)

    def do_task(self, task):
        return self.llm.get_response(task)
