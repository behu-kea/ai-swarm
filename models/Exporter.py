import csv
import json
import os

class Exporter:
    @staticmethod
    def export_to_csv(person_id, task_result, filename: str):
        file_exists = os.path.isfile(filename)

        # Open the file in append mode ('a')
        with open(filename, mode='a', newline='', encoding='utf-8') as file:
            attributes = vars(task_result)
            # Create a new dictionary with 'id' as the first key
            ordered_attributes = {'id': person_id}
            # Add the rest of the attributes
            ordered_attributes.update(attributes)

            # Initialize the writer
            writer = csv.DictWriter(file, fieldnames=ordered_attributes.keys(), delimiter=';', quotechar='"',
                                    quoting=csv.QUOTE_ALL)

            # Write the header only if the file is new
            if not file_exists:
                writer.writeheader()

            # Write the data (the attribute values)
            writer.writerow(ordered_attributes)

    @staticmethod
    def export_to_json(task_result, filename: str):
        with open(filename, 'w', encoding='utf-8') as file:
            json.dump({'answers': task_result.answers}, file, ensure_ascii=False, indent=4)


# Usage
# task_result = person.do_task(generation.task, generation.response_format)
# Exporter.export_to_csv(task_result, 'task_result.csv')
# Exporter.export_to_json(task_result, 'task_result.json')
