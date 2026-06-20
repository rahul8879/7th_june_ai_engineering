# age = 34
# print(type(age))
# # print(age**'5')

# course = 'AI Engineering'
# trainer = 'Sachin'
# sep = ': '

# print(course + sep+ trainer)
# import keyword
# print(keyword.kwlist)

# ['False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await', 
#  'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except',
#    'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 
 
#  'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']

# ssn_number = input('Enter your ssn number : ')
# print(type(ssn_number))
# print(ssn_number)
# name = 23
# print(len(name))
# if len(ssn_number) == 9:
#     print('valid ssn number')
# else:
#     print('invalid ssn number')

# total_charges = 11834.13123123
# print(round(total_charges, 2))

# val_1 = 50
# val_2 = 60
# val_3 = 70
# val_4 = 80
# val_5 = 90

# avg_sales = (val_1 + val_2 + val_3 + val_4+val_5) / 5
# print(avg_sales)

sales_volume = [50, 60, 70, 80, 90,110,232,24234,2423,4242,223]

# avg_sales = (sales_volume[0]+sales_volume[1]+sales_volume[2]+sales_volume[3]+sales_volume[4]+sales_volume[5])/6
# for loop
# total_sum= 0
# for i in sales_volume:
#     total_sum = i + total_sum

# print(round(total_sum/len(sales_volume),2))


courses = ['ai','genai','agenticai','machine_learning','deep learning']
search= 'genai'
for i in courses:
    if i == search:
        print('Yes we have the course for this topics')
        break
else:
    print('No we dont have the course for this topics')

    