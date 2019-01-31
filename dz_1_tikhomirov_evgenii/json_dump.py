import json

products1 = [
    {'name': 'Amazing book', 'discription': 'For everybody',
     'img': '/static/img/trends/moms-entrepreneurs-2703456_960_720.png'},
    {'name': 'Book for you', 'discription': 'For everybody',
     'img': '/static/img/trends/moms-entrepreneurs-2703456_960_720.png'},
    {'name': 'Goog gift', 'discription': 'For everybody',
     'img': '/static/img/trends/moms-entrepreneurs-2703456_960_720.png'},
    {'name': 'Classic', 'discription': 'For everybody',
     'img': '/static/img/trends/moms-entrepreneurs-2703456_960_720.png'},
    {'name': 'Lev Tolstoy', 'discription': 'For everybody',
     'img': '/static/img/trends/moms-entrepreneurs-2703456_960_720.png'},
    {'name': 'Poetry', 'discription': 'For everybody',
     'img': '/static/img/trends/moms-entrepreneurs-2703456_960_720.png'},
]

j_son = json.dumps(products1)
with open('products1.json', 'w', encoding='utf-8') as f:
    json.dump(products1, f)

print(json.loads(j_son))

