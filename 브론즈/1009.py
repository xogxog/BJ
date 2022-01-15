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

    b = str(b)[-1]
    print(computer[int(b)])