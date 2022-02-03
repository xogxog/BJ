for _ in range(int(input())) :
    M = int(input())
    ls = list(map(int,input().split()))
    ans =[]
    for i in range(M) :
        if i%2 == 0 :
            tmp = ls[0:i+1]
            tmp.sort()
            print(tmp)
            ans.append(tmp[len(tmp)//2])
    print(len(ans))
    print(*ans)

