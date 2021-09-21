N = int(input())

if N == 1:
    pass
else :
    while N > 1 :
        # print(N)
        for i in range(2,N+1):
            if N % i == 0 :
                print(i)
                N //= i
                break
