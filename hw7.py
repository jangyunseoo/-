shopping_bag = {}
print('[구입]')

while True :
    item = input('상품명? ')
    if item == '' :
        break
    amount = input('수량은? ')
    shopping_bag[item] = amount
    print(f'장바구니에 {item} {amount}개가 담겼습니다.\n')

print(f'\n>>> 장바구니 보기: {shopping_bag}')

print('\n[검색]')
check = input('장바구니에서 확인하고자 하는 상품은? ')
if check in shopping_bag :
    print(f'{check}은(는) {amount}개 담겨 있습니다.')
