import random
from datetime import datetime
import json
def get_random_date():
    start_date = datetime(2025, 1, 1).timestamp()
    end_date = datetime(2025, 12, 31).timestamp()
    random_date = random.uniform(start_date, end_date)
    random_date = datetime.fromtimestamp(random_date).strftime("%Y-%m-%d")
    return random_date

def get_random_product():
    products = [["teddy", 100], ["teddy cat", 150], ["Berserk Deluxe Volume 1", 200], ["Laptop", 1200], ["Smartphone", 800], ["Tablet", 600], ["Headphones", 100], ["Smartwatch", 200]]
    return random.choice(products)

############################################################
# 1. Carga de Datos
############################################################

ventas = []
for i in range(10):
    venta = {
        "fecha": get_random_date(),
        "producto": get_random_product()[0],
        "cantidad": random.randint(1, 10),
        "precio": get_random_product()[1]
    }
    ventas.append(venta)


with open('ventas.json', 'w') as outfile:
    json.dump(ventas, outfile)


# print(json.dumps(ventas, indent=4, ensure_ascii=False))


