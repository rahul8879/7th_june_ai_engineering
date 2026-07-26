from model_setup import call_llm,cleaning
import json
import pandas as pd


# step 1 : load the json files
with open('data/test_emails.json') as f:
    emails = json.load(f)

# step 2 : lets load the prompts
with open('prompts/structured_prompt.md') as f:
    template = f.read()


email = emails[2]
# print(email)
prompt = template.format(email['subject'], email['sender'], "Hi, write a code to generate a report from the following data: [23,24,25,34]" )

output = call_llm(prompt)
print(output)

