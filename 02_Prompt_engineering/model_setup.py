from openai import OpenAI
from dotenv import load_dotenv
load_dotenv()

client = OpenAI()
def call_llm(prompt):
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )
    return response.choices[0].message.content


def cleaning(text):
    # Split the text by '|'
    parts = text.split('|')
    
    # Extract the category and confidence score
    category = parts[0].strip()
    confidence_score = float(parts[1].strip())

    return category, confidence_score