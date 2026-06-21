# data = [12,13,14,76,89,101]
# # print(data[0])
# # data[0] = 26
# # print(data[0])
# # print(data)
# data.append(100)
# print(data)

# # print(data[:]) # starting : ending( excluded)
# # slicing of list
# # sales_data = [354,330,300,450,567,323,123,442]
# # print(sales_data)
# # print(sales_data[::2]) # starting : ending : step

# # odd_day_sales = sales_data[::2]
# # avg_oddday_sales = sum(odd_day_sales)/len(odd_day_sales)
# # print(avg_oddday_sales)

# # even_day_sales = sales_data[1::2]
# # avg_evenday_sales = sum(even_day_sales)/len(even_day_sales)
# # print(avg_evenday_sales)


# # operations ??
# # 1 append --> add element at the end of the list
# # data.append(-1)
# # data.insert(3, -1) # param : index, value
# # print(data)

# # 2 remove --> remove element from the list
# # data.remove(9)
# # print(data)

# # 3 pop --> remove element from the list
# data.pop(5)
# print(data)

# # data = [12.2,'rahul',14,[12,13,14],89,101]
# # for i in data:
# #     print(type(i))

# # https://docs.python.org/3/tutorial/datastructures.html

# day_1_sales = [34,56,12,45,65,78,98,34,32,12]
# day_2_sales = [45,65,78,98,34,32,12,34,56,12]
# day_1_sales.append(day_2_sales)
# print(day_1_sales)
# print(len(day_1_sales))


# day_1_sales = [34,56,12,45,65,78,98,34,32,12]
# day_2_sales = [45,65,78,98,34,32,12,34,56,12]
# day_1_sales.extend(day_2_sales)
# print(day_1_sales)
# print(len(day_1_sales))

# avg_sales = sum(day_1_sales)/len(day_1_sales)
# print(avg_sales)


data = [34,56,12,45,65,78,98,34,32,12]
data[4]= 100
print(data)

data = (34,56,12,45,65,78,98,34,32,12)
# data[4]= 100
# print(data)
# data.append(100)


# list vs tuple
# access ??
# via imdex\
# 

# for i in data:
#     print(i)

# https://docs.python.org/3.13/tutorial/datastructures.html#tuples-and-sequences


# string ??? importance for your AI engineering : prompt engineering ???

# string methods
# https://docs.python.org/3.13/library/stdtypes.html

# prompt = """We saw that lists and strings have many common properties, 
# such as indexing and slicing operations. They are two examples
#  of sequence data types (see Sequence Types — list, tuple, range). 
#  Since Python is an evolving language,
#  other sequence data types may be added. 
#  There is also another standard sequence data type: the tuple."""
# print(type(prompt))


harmful_word = ['hack','destroy']
prompt = "You are very bad person"
prompt.replace('bad','###')




# print(prompt.upper())
# result = 'hack'.upper() in prompt.upper()

# for i in harmful_word:
#     if i.upper() in prompt.upper():
#         print('yes')
#         break
# else:
#     print('no')

# import re
# prompt = "this is pan card number 4235423523534534534"
# output= re.sub('[0-9]','*',prompt)
# print(output)

# data = "12,13,14"
# output = data.replace('12','31234123412341234124124')
# print(output)


