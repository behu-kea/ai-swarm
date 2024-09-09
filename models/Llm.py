from abc import abstractmethod

class Llm():
    def __init__(self, system_prompt):
        self.system_prompt = system_prompt

    @abstractmethod
    def get_response(self, prompt):
        pass