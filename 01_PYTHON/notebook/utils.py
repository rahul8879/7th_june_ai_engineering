def sales_avg(data):
    output = {}
    for key, value in data.items():
        avg_sales = sum(value) / len(value)
        output[key] = avg_sales
    return output