
sales_data = {
   'day_1':[100, 200, 300],
   'day_2':[150, 250, 350],
   'day_3':[200, 300, 400],
   'day_4':[250, 350, 450],
   'day_5':[12]

}


sales_data_1 = {
   'day_1':[100, 200, 300],
   'day_2':[150, 250, 350],
   'day_3':[200, 300, 400],
   'day_4':[250, 350, 450],
   'day_5':[12]

}

from utils import sales_avg
output = sales_avg(sales_data)
print(output)

# def test(a):
#     return a,'Learning Python'
#     fsdfs
#     sdfsdf 
#     fsdfsdf


# output,output_1 = test([12,23])
# print(output)



# output = {}
# for key, value in sales_data.items():
#     avg_sales = sum(value) / len(value)
#     output[key] = avg_sales
# print(output)

# output_1 = {}
# for key, value in sales_data_1.items():
#     avg_sales = sum(value) / len(value)
#     output_1[key] = avg_sales

# print(output_1)