# import numpy as np


# generate 1000 random values
# import time
# x = np.random.randint(20, 100, 10000)
# start_time = time.time()
# for i in x:
#     if i == 20:
#         pass
# end_time = time.time()
# print(f"Time taken: {end_time - start_time} seconds")

sales_data = {
   'day_1':[100, 200, 300],
   'day_2':[150, 250, 350],
   'day_3':[200, 300, 400],
   'day_4':[250, 350, 450],
   'day_5':12

}

# product_details = {
#    'product_1':{
#        'name':'Product 1',
#        'price':100,
#        'category':'Category 1'
#    },
#    'product_2':{
#        'name':'Product 2',
#        'price':150,
#        'category':'Category 2'
#    },
#    'product_3':{
#        'name':'Product 3',
#        'price':200,
#        'category':'Category 3'
#    },
#    'product_4':{
#        'name':'Product 4',
#        'price':250,
#        'category':'Category 4'
#    }
# }


# access some of the data
# print(product_details['product_1'])
# print(sales_data['day_6'])
# print(sales_data.get('day_6', 'No data available for day 6'))
# sales_data['day_6'] = [300, 400, 500]  # this is the way like how we can add key or data into dict
# print(sales_data.get('day_6', 'No data available for day 6'))
# sales_data['day_5'] = [434, 43, 12]  # this is the way like how we can add key or data into dict
# print(sales_data.get('day_5', 'No data available for day 5'))

# For building search functionlities 
# - Store data in a dictionary
# - use the key to search the particular key 
# - this process will not take n times ( o(n))