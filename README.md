# AI Swarm

## Entities

- `PersonasGenerator` - Creates the random background for a `Person`
  - Takes a `target_audience` - `String`
- `Persona`
  - `background` - `String` - Has a background generated from `PersonaGenerator`
  - `do_task` - Function that returns the result of doing a task
- `Llm` - Baseclass defines an abstract function `get_response`. Reason for this is so we can easily change models with fx anthropic or llama
- `OpenAiLlm` - Extends `Llm` and is an llm implemented using OpenAi api.
- `Generation` - Represents a full generation. Meaning
  - `number_of_personas` - `Number`
  - `target_audience` - `String`
  - `task` - `String`

## Todo
- Personageneratoren skal have many shot eksempler på hvordan den skal generere realistiske personer. Den skal have måske 10 forskellige eksempler på en målgruppe og hvilke realistiske baggrunde kunne komme ud af det.
- Personageneratoren kan også have en helt anden approach til at lave en realistisk person. Kunne man tage inspiration i personlighedstests? Måske hver persona skal have ønsker, mål, svagheder, personlighedstyper, etc. 

## Forbedringer
- Personerne er meget stereotypiske. Fx når der bliver lavet It-arkitektur studerende er de alle så "professionelle". Alle deres interesser er om netværk og softwareudvikling. Sådan er det ikke i virkeligheden. Hvordan kan vi forbedre det?
- 