# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
from models.PersonaGenerator import PersonaGenerator
from models.Persona import Persona

import constants

# openai.api_key = os.getenv('OPENAI_API_KEY')
# Load environment variables


number_of_personas = 1
for i in range(number_of_personas):
    target_audience = "Students at it-architecture at KEA. Living close to copenhagen. Between 18 and 24. "
    persona_generator = PersonaGenerator(target_audience)
    persona_background = persona_generator.get_user_background()
    person = Persona(persona_background)
    print(person.background)

    task_result = person.do_task(f"""You are on your 2. semester and have done the following exercises in a kotlin programming class.
                Please write 5 things that worked well and 5 things that can be improved. Keep it relatively short and concise and please answer in english!
                Exercises:
                ```
                {constants.EXERCISES}
                ```
                """)

    print(task_result)

# completion = client.chat.completions.create(
#     model="gpt-4-1106-preview",
#     messages=[
#         {"role": "user", "content": f"""
#         Act like a professional and feedback oriented lecturer. The students were asked to write what went well and what can be improved.
#         Please write a clear and concise summary of the feedback given here. Dont go through each student, but just write the conclusion of the feedback: ```{feedback_complete}```
#         """}
#     ]
# )
#
# print("Feedback summary: ", completion.choices[0].message.content)
