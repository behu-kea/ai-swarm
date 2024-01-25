import constants


def get_swarm_prompt(number_of_personas, target_audience):
    return f"""
      Generate {number_of_personas} different and random backgrounds for people within the following target audience "{target_audience}"
      Please be quite specific about details. Make the backgrounds realistic. The background should be around 5 lines long. Here is an example:

      Example
      ```
      Your name is Jenny. You are a single 36 years mom and have two kids aged 3 and 7. 
      You lived in a small town but have always been drawn to the city. Your parents were caring but also very busy with work. You were often picked up quite late from the kindergarden
      Growing up you were fond of playing in nature especially forests. 
      You were smart but never saw yourself as such. You graduated as a Chemist but did not really like working as a chemist. Now you work as an accountant for a law firm
      You are sharing the kids but have not found someone since a quite tough divorce
      ```

      Please respond with json with an array of strings in the following format. 
      ```
      {{
        personas: [PERSONA_DESCRIPTION_1, PERSONA_DESCRIPTION_2, ...]
      }}
      ```
      """


def get_task_prompt(persona):
    return f"""
        Act like the following persona:
        {persona}
        You have done the following exercises in a programming class.
        Please write 5 things that worked well and 5 things that can be improved. Keep it relatively short and concise and please answer in english!
        Exercises:
        ```
        {constants.EXERCISES}
        ```
        """