def get_fixed_price(price, rate) :
    fixed_price = price * 100 // (100 - rate)
    return fixed_price

sale_rate = int(input('할인율은? '))
sale_price1 = int(input('A 상품의 할인된 가격은? '))
sale_price2 = int(input('B 상품의 할인된 가격은? '))
fixed_price1 = get_fixed_price(sale_price1, sale_rate)
print('A 상품의 정가는', fixed_price1, '원')
fixed_price2 = get_fixed_price(sale_price2, sale_rate)
print('B 상품의 정가는', fixed_price2, '원')
