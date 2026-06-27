

# Below sample code is an example of f String in python


sender = 'rahul@gmail.com'
date= '2023-01-01'
email= "I am facingthe issue while login the system. Please help me to resolve this issue"

prompt_v2 = f"""You are an expert email classifier.
Classify the following email.

From: {sender}
Date: {date}
Email: {email}

Categories:
- Spam
- Important
- Newsletter
- Personal


Your classification:"""

print(prompt_v2)