from models.OpenAiLlm import OpenAiLlm

class PersonaGenerator:
    def __init__(self, target_audience):
        self.target_audience = target_audience
        self.llm = OpenAiLlm(system_prompt="You help generate different personas with different but very unique backgrounds")

    def get_user_background(self):
        get_user_background_prompt =  f"""
              A random background for a person within the following target audience "{self.target_audience}"
              Please be quite specific about details. Make the background realistic. The background should be around 5 lines long. Here is an example:

              Example
              ```
              Your name is Jenny. You are a single 36 years mom and have two kids aged 3 and 7. 
              You lived in a small town but have always been drawn to the city. Your parents were caring but also very busy with work. You were often picked up quite late from the kindergarden
              Growing up you were fond of playing in nature especially forests. 
              You were smart but never saw yourself as such. You graduated as a Chemist but did not really like working as a chemist. Now you work as an accountant for a law firm
              You are sharing the kids but have not found someone since a quite tough divorce
              ```

              Please respond with only the background text of the user
              """

        return self.llm.get_response(get_user_background_prompt)

