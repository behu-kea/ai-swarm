from models.PersonaGenerator import PersonaGenerator
from models.Person import Person
from models.Exporter import Exporter

from generations import generation1

for i in range(generation1.number_of_personas):
    persona_generator = PersonaGenerator(generation1.target_audience)
    print(f"""Generating background for person {str(i + 1)}""")
    person = Person(persona_generator.get_user_background())
    print(f"""Background generated for person {str(i + 1)}""")

    print(f"""Person {str(i + 1)} is performing their task""")
    task_result = person.do_task(generation1.task, generation1.response_format)
    print(f"""Person {str(i + 1)} is done with their task""")

    print(f"""Exporting person {str(i + 1)}'s answer""")
    Exporter.export_to_csv(person.id, task_result, 'exports/task_result.csv')
    print(f"""Done exporting person {str(i + 1)}'s answer""")
