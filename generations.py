from models.Generation import Generation
from pydantic import BaseModel

class ResponseFormat1(BaseModel):
    question1: str
    question2: str
    question3: str
    question4: str
    question5: str
    question6: str
    question7: str
    question8: str

generation1 = Generation(
    number_of_personas=1,
    target_audience="Students at it-architecture at KEA. Living close to copenhagen. Between 18 and 24. Some have programming from before some dont. ",
    task = f"""Du skal svare på det følgende spørgeskema:
                1. Hvorfor har du søgt ind på IT-arkitektur?
                2. Hvilke færdigheder og kompetencer kan du bidrage med på studiet? (fagligt, social, andet)
                3. Hvad var dit yndlingsfag i din ungdomsuddannelse?
                4. Er der noget vi skal vide om dine forudsætninger?
                5. Hvad motiverer dig til at lære?
                6. Hvad interesserer du dig for?
                7. Har du tidligere programmeringserfaring? Hvis ja hvor meget?
                8. Har du nogle spørgsmål til underviserne?
                """,
    response_format=ResponseFormat1
)