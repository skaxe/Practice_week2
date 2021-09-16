price = input('Введите цену, чтобы рассчитать цену со скидкой ')
discount = input('Введите скидку ')
max_discount = input('Введите максимально возможную скидку ')
def discounted(price, discount, max_discount):
    while True:
        try:
            price = abs(float(price))
            discount = abs(float(discount))
            max_discount = abs(int(max_discount))
            if max_discount >= 100:
                raise ValueError('Максимальная скидка не должна быть больше 100')
            if discount > max_discount:
                price_with_discount = price
            else:
                price_with_discount = price - (price*discount/100)
            return price_with_discount
        except (TypeError, ValueError):
            print('Неправильный формат ввода')
            return
        
            
product = {'name': 'Samsung Galaxy S21', 'price': 50000.0, 'discount': 5}
#product ['with_discount'] = discounted(product['price'], product ['discount'])
print(discounted(price, discount, max_discount))
