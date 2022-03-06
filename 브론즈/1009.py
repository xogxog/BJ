for _ in range(int(input())) :
    a,b = map(int,input().split())
    computer = [0]*11

    for i in range(len(computer)) :
        tmp = a**i
        if tmp < 10 :
            computer[i] = str(tmp)
        else :
            tmp2 = str(tmp)[-1]
            computer[i] = tmp2
    print(computer)
    b = str(b)[-1]
    for j in range(21):
        print(j,7**j)

    if b == '0' :
        print(computer[10])
    else :
        print(computer[int(b)])