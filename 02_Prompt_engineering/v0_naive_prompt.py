from model_setup import call_llm
import json
import pandas as pd
from model_setup import cleaning

# step 1 : load the json files
with open('test_emails.json') as f:
    emails = json.load(f)

# step 2 : lets load the prompts
with open('simple_prompt.md') as f:
    template = f.read()

prompt = template.format(emails[99]['body'])
result = {}

# step 3 : generate the prompts and call the model
for i in emails[:30]:
    prompt = template.format(i['body'])
    category, confidence = cleaning(call_llm(prompt))
    result[i['id']] = {'category': category, 'confidence': confidence}

df = pd.DataFrame.from_dict(result, orient='index')
df.to_csv('email_classification_results.csv')
