from openai import OpenAI

client = OpenAI(api_key='')




# Below sample code is an example of f String in python

emails = [
"Hi Team, I am facing the issue while using the applications",
"Hi tea, very bad experiance with your product",
"Wow what a bad product"

]

# for i in emails:
#     print(i)


# sales = [34,45,51,43,12,21,34,50]

# print(sales[2])


output = []

for email in emails:
    prompt = f"""You are an expert email classifier.
            Classify the following email.

            Email: {email}

            Categories:
            - Spam
            - Important
            - Newsletter
            - Personal
            Your classification:"""
    
    response = client.chat.completions.create(
        model ="gpt-4o-mini",
        messages=[
            {"role":"user", "content":prompt}
        ]
    )
    output.append(response.choices[0].message.content.strip())

print(output)
    
    
   
  