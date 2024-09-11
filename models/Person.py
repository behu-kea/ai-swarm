from models.OpenAiLlm import OpenAiLlm
import secrets

class Person:
    def __init__(self, background):
        self.background = background
        self.llm = OpenAiLlm(background)
        self.id = secrets.token_urlsafe(8)

    def do_task(self, task, response_format):
        return self.llm.get_response(task, response_format)
