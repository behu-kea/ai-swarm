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

    def get_response(self, prompt, response_format=None):
        # Only add response
        completion = None
        if response_format:
         completion = client.beta.chat.completions.parse(
            model= "gpt-4o-2024-08-06",
            messages = [
                {"role": "system", "content": self.system_prompt},
                {"role": "user", "content": prompt}
            ],
            response_format = response_format
        )
        else:
            completion = client.beta.chat.completions.parse(
                model="gpt-4o-2024-08-06",
                messages=[
                    {"role": "system", "content": self.system_prompt},
                    {"role": "user", "content": prompt}
                ],
            )

        return completion.choices[0].message.parsed if response_format else completion.choices[0].message.content


