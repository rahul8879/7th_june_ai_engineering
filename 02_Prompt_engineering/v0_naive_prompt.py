from model_setup import call_llm,cleaning
import json
import pandas as pd

# step 1 : load the json files
with open('data/test_emails.json') as f:
    emails = json.load(f)

# step 2 : lets load the prompts
with open('prompts/simple_prompt.md') as f:
    template = f.read()



# step 3 : generate the prompts and call the model

def process_emails(emails,n_num=15):
    result = {}
    for i in emails[:n_num]:
        prompt = template.format(i['body'])
        print('output from my llm : ', call_llm(prompt))
        category, confidence = cleaning(call_llm(prompt))
        result[i['id']] = {'category': category, 'confidence': confidence}

    return result

output = process_emails(emails,1)
# pandas dataframe

df = pd.DataFrame.from_dict(output, orient='index')
df.to_csv('data/email_classification_results.csv')
