import pickle
import os

filename = 'score.bin'
filepath = 'C:/pyWork/' + filename

def input_scores() :
    s = []
    i = 1
    while True :
        n = int(input(f'#{i}? '))
        if n < 0 :
            break
        s.append(n)
        i += 1
    return s

def get_average(s) :
    total = 0
    for n in s :
        total += n
    return total / len(s)

def show_scores(s) :
    for n in s :
        print(n, end = ' ')
    print()

def save_data(s, filepath) :
    with open(filepath, 'wb') as file :
        pickle.dump(s, file)
        
def load_data(filepath) :
    if os.path.exists(filename) :
        print('[파일 읽기]')
        with open(filepath, 'rb') as file :
            return pickle.load(file)

loaded_scores = load_data(filepath)
if loaded_scores :
    print('\n[점수 출력]')
    print('개인 점수: ', end = '')
    show_scores(loaded_scores)
    avg = get_average(loaded_scores)
    print(f'평균: {avg}')
else :
    print('[점수 입력]')
    scores = input_scores()
    print('\n[점수 출력]\n개인점수: ', end = '')
    show_scores(scores)
    avg = get_average(scores)
    print(f'평균: {avg}')
    save_data(scores, filepath)
