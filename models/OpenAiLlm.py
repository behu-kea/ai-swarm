from openai import OpenAI
import os
from models.Llm import Llm

from dotenv import load_dotenv
load_dotenv()

client = OpenAI(
    api_key=os.getenv('OPENAI_API_KEY'),
)

class OpenAiLlm(Llm):
    def __init__(self, system_prompt):
        super().__init__(system_prompt)
        self.system_prompt = system_prompt

    def get_response(self, prompt):
        completion = client.chat.completions.create(
            model="gpt-4o",
            messages=[
                {"role": "system",
                 "content": self.system_prompt},
                {"role": "user", "content": prompt}
            ]
        )

        return completion.choices[0].message.content

