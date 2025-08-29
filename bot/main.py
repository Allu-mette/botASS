from google import genai
from google.genai import types
import random
from datetime import date

import bot.utils_db as db
from bot.utils_mail import sendMail
from config import API_KEY, MAX_TOKEN

def generatePrompt():

    difficulty = random.choice(['Facile', 'Moyenne', 'Difficile'])

    with open("./prompt.txt", "r", encoding="utf-8") as f:
        prompt_template = f.read()
    prompt = prompt_template.format(MAX_TOKEN=MAX_TOKEN, difficulty=difficulty)

    lastResponses = db.getLastResponses()
    for i, res in enumerate(lastResponses):
        prompt += f'Réponse {i+1} : \n'
        prompt += res[0].replace("\\n", "\n")
        prompt += '\n'
        
    return prompt, difficulty

def main():

    client = genai.Client(api_key=API_KEY)
    prompt, difficulty = generatePrompt()
    response = client.models.generate_content(
        model = 'gemini-2.0-flash-001', 
        contents = prompt,
        config = types.GenerateContentConfig(
            max_output_tokens = MAX_TOKEN*1.5,
            temperature=0.2,
        ),
    )
    db.addResponse(difficulty, response.usage_metadata.candidates_token_count, response.text)
    
    content = response.text
    content = content.replace("```html", "").replace("```", "")
    content = f"<i>Difficulté : {difficulty}</i><br><br>" + content
    sendMail(content)
    print(f"Exercice sended : {date.today()}")

    #print(response.usage_metadata.prompt_token_count)
    #print(response.usage_metadata.candidates_token_count)
    #print(response.usage_metadata.total_token_count)


if __name__ == "__main__":
    main()