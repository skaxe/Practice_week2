from pprint import pprint
stock = [
   { "name": "iphone", "stock": 24, "price": 65432.1,
    "recomended": ["samsung", "iphone", "xiaomi"]},
   {"name": "xiaomi", "stock": 34, "price": 21000.0, 'discount': 5000},
   {"name": "samsung", "stock": 14, "price": 38000.5}
]


pprint(type(stock[0]['recomended']))