# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
from openai import OpenAI
from dotenv import load_dotenv
import os
import json
import prompts
import constants

# openai.api_key = os.getenv('OPENAI_API_KEY')
# Load environment variables
load_dotenv()

client = OpenAI(
    api_key=os.getenv('OPENAI_API_KEY'),
)


def get_personas():
    generate_swarm_prompt = prompts.get_swarm_prompt(constants.NUMBER_OF_PERSONAS, constants.TARGET_AUDIENCE)

    completion = client.chat.completions.create(
        model="gpt-4-1106-preview",
        response_format={"type": "json_object"},
        messages=[
            {"role": "system",
             "content": "You help generate different personas with different but very unique backgrounds"},
            {"role": "user", "content": generate_swarm_prompt}
        ]
    )

    return completion.choices[0].message.content


personas_json_string = get_personas()

personas = json.loads(personas_json_string)
print("personas", personas)
feedback_complete = ""
counter = 0
for persona in personas['personas']:
    task_prompt = prompts.get_task_prompt(persona)

    completion = client.chat.completions.create(
        model="gpt-4-1106-preview",
        messages=[
            {"role": "user", "content": task_prompt}
        ]
    )

    feedback = completion.choices[0].message.content
    print("feedback", feedback)
    feedback_complete += f"Student {(counter + 1)} feedback: ```{feedback}```\n"
    counter += 1

print("feedback_complete", feedback_complete)

completion = client.chat.completions.create(
    model="gpt-4-1106-preview",
    messages=[
        {"role": "user", "content": f"""
        Act like a professional and feedback oriented lecturer. The students were asked to write what went well and what can be improved.   
        Please write a clear and concise summary of the feedback given here. Dont go through each student, but just write the conclusion of the feedback: ```{feedback_complete}```
        """}
    ]
)

print("Feedback summary: ", completion.choices[0].message.content)
