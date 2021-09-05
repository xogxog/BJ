T = int(input())

for _ in range(1,T+1):
    prob = input()
    sum = 0
    cnt = 1
    for i in range(len(prob)):
        if prob[i] == "O" :
            sum += cnt
            cnt += 1
        else :
            cnt = 1

    print(sum)