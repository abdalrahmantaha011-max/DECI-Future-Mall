mall_name = "Future Mall"

products = [
    "Milk",
    "Bread",
    "Rice",
    "Apple",
    "Juice"
]

prices = [
    60,
    25,
    120,
    40,
    90
]

def print_all():
    for i in range(5):
        print(f'-{i} {products[i]} ==> {prices[i]} EG')

print_all()

total = 0

while True:
    products_number = int(input('Enter the Product-number: '))
    if products_number in range(5):
        price = prices[products_number]
        total += price
    else:
        print('Sorry, This Product is not deffind!')

    chick = input('Add another product? (y,n): ').strip()
    if chick.lower() == 'y':
        continue
    else:
        break

if total > 500:
    discount = total * 0.10
    final_total = total - discount
else : 
    discount = 0
    final_total = total


def final():
    print('='*15 , mall_name , '='*15)
    print(f'- Total: {total}')
    print(f'- Discount: {discount}')
    print(f'- Final Total: {final_total}')
    print('='*10 , 'Thank you for shopping!' , '='*10)


final()