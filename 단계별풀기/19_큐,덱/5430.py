# 로직 보다는 입력받는게 어려웠다.

from collections import deque
T = int(input())

def AC(ls):
    pointer = 0
    for ord in order:
        if ord == 'R':
            if pointer == 0:
                pointer = -1
            else:
                pointer = 0
        elif ord == 'D':
            if len(ls) > 0 :
                if pointer == 0:
                    ls.popleft()
                else:
                    ls.pop()
            else :
                return 'error'


    return ls


for tc in range(1,T+1) :
    order = input()
    n = int(input())
    ls = deque(input().lstrip('[').rstrip(']').split(','))

    if '' in ls :
        ls.pop()

    result = AC(ls)
    if result == 'error' :
        print('error')
    elif order.count('R') % 2 == 0:
        print('[{}]'.format(','.join(result)))
    else :
        print('[{}]'.format(','.join(reversed(result))))