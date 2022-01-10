n = int(input()) # 선수의 수

player = dict()

for _ in range(n) :
    name = input()
    capital = name[:1]

    if capital in player.keys() :
        player[capital] += 1
    else :
        player[capital] = 1

answer = []

for key,value in player.items() :
    if value >= 5 :
        answer += key

answer.sort()

if len(answer)==0 :
    print(f'PREDAJA')
else :
    print(''.join(answer))