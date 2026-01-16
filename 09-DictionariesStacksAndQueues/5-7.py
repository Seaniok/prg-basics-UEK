# Hotels in Krakow: …,…,…,…
# Average hotel price in Krakow: …
# Hotels in Sopot: …,…,…,…
# Average hotel price in Sopot: …
# Cheaper hotels in: …

hotels_in_Krakow = [
   {"name":"Sky","price":320.00},
   {"name":"Metropol","price":480.00},
   {"name":"New Port","price":420.00},
   {"name":"Aparthotel","price":390.00}
]

hotels_in_Sopot = [
   {"name":"Focus","price":510.00},
   {"name":"Aqua","price":345.00},
   {"name":"La Boutique","price":390.00},
   {"name":"Marina","price":410.00}
]


def hotel_lists(hotels):
    names = ''
    average = 0
    for hotel in hotels:
        names = names + hotel["name"] + ','
    return names[:-1]

def avg_price(hotels):
    n = len(hotels)
    average = 0
    count = 0
    for prices in hotels:
        average = average + (prices['price'] / n)
    return average

print(hotel_lists([
   {"name":"Sky","price":320.00},
   {"name":"Metropol","price":480.00},
   {"name":"New Port","price":420.00},
   {"name":"Aparthotel","price":390.00}
]))

print(avg_price([
   {"name":"Sky","price":320.00},
   {"name":"Metropol","price":480.00},
   {"name":"New Port","price":420.00},
   {"name":"Aparthotel","price":390.00}
]))