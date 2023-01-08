# Code to print dictionary with respect to decreasing prices


guitars = [
{'model': 'yamaha £310', 'price':8400},
{'model': 'faith naptune', 'price':50000 },
{'model': 'faith apollo venus', 'price': 35000},
{'model': 'taylor 814ce', 'price': 450000},
]

print(sorted(guitars, key = lambda x: x['price'], reverse = True))