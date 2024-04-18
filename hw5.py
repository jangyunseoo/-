def read_single_digit(number):
    if number==0:
        return '영'
    elif number==1:
        return '일'
    elif number==2:
        return '이'
    elif number==3:
        return '삼'
    elif number==4:
        return '사'
    elif number==5:
        return '오'
    elif number==6:
        return '육'
    elif number==7:
        return '칠'
    elif number==8:
        return '팔'
    else:
        return '구'

def read_number(prompt):
    if int(input(prompt)):
        return read_single_digit()
    
three=int(input('세 자리 정수 입력: '))
one=read_single_digit(three)
print(f'{one} {one} {one}')
