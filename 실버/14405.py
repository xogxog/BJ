pikachu = input()

idx = 0

while True :
    if pikachu[idx : idx+2] == 'pi'or pikachu[idx:idx+2] == 'ka' :
        idx += 2
    elif pikachu[idx:idx+3] == 'chu' :
        idx += 3
    else :
        print('NO')
        break
    if idx == len(pikachu) :
        print('YES')
        break