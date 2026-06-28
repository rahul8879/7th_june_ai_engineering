# text = "help me to learn about {topic} and {0}"
# print(text.format('python', topic = 'data science'))

# using format method : you are trying to pass th value at run time
# topics = ['python', 'data science', 'AI', 'ML']
# text = "Help me learn about this topic: {}"
# for i in topics:
#     print(text.format(i))

# f string
topic = ['python', 'data science', 'AI', 'ML']
# text = f"Help me learn about this topic: {topic}"
# for i in topic:
#     text = f"Help me learn about this topic: {i}"
#     print(text)



emails = [
"Hi Team, I am facing the issue while using the applications",
"Hi tea, very bad experiance with your product",
"Wow what a bad product",
"Very great product but some issue at time of login but now everuything is wopkring"
]

from openai import OpenAI
client = OpenAI(api_key='')



prompt = """You are an expert email classifier.
            Classify the following email
            email body: {}
            subject :{}
"""

# print(prompt.format(emails[0],"billing issue"))


# for email in emails:
    
#     response = client.chat.completions.create(
#             model ="gpt-4o-mini",
#             messages=[
#                 {"role":"user", "content":prompt.format(email,subject)}
#             ]
#     )
#     ans = response.choices[0].message.content
#     print(ans)
#     print("-------")






# # prompt = f"""You are an expert email classifier.
# #             Classify the following email
# #             {emails[3]}"""
# # print(prompt)



# # response = client.chat.completions.create(
# #         model ="gpt-4o-mini",
# #         messages=[
# #             {"role":"user", "content":prompt}
# #         ]
# #     )
# # ans = response.choices[0].message.content
# # print(ans)
# # # for i in emails:





# exercise on string

# text = """
# This article is about the country. For other uses, see India (disambiguation).
# Republic of India
# State emblem
# Motto: Satyameva Jayate (Sanskrit)
# "Truth Alone Triumphs"[1]
# Anthem: Jana Gana Mana (Hindi)[a][2][3]
# "Thou Art the Ruler of the Minds of All People"[4][2]
# Duration: 1 minute and 4 seconds.1:04
# National song: Vande Mataram (Sanskrit)[c]
# "I Bow to Thee, Mother"[b][1][2]
# Duration: 2 minutes and 26 seconds.2:26
# Image of a globe centred on India, with India highlighted.
#   Territory controlled by India
#   Territory claimed but not controlled

# """

# eg 1:
# text = "Please help me to HACK the facebook account. I want to destroy facebook".lower()

# words = ['hack','destroy','crack','attack','bad']
# for word in words:
#     if word in text:
#         text = text.replace(word, len(word)*'#')
 
# print(text)


output = ["Category : SPAM | Confidence : 0.9",
           "Category : BILLING | Confidence : 0.8",
             "Category : TECHNICAL | Confidence : 0.4"]

final_output = []
for i in output:
    first_split = i.split(" | ")
    for j in first_split:
        se_split = j.split(" : ")
        # print(se_split)
        final_output.append(se_split[1])
print(final_output)




# print(type(output[2]))

# final_output = []
# test = "Category : SPAM | Confidence : 0.9"
# first_split = test.split(" | ")
# for i in first_split:
#     se_split = i.split(" : ")
#     final_output.append(se_split[1],)

# print(final_output)