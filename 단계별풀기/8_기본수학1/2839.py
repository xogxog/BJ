N = int(input())

n = N // 5
ls = [3, 6, 9, 12, 15, 18, 21, 27]

if N % 5 == 0 :
    print(N//5)

else:
    for i in range(n,-2,-1):
        if i == -1 or N-(5*i) >= 30 :
            print(-1)
            break
        elif N-(5*i) in ls :
            print(i+(ls.index(N-5*i)+1))
            break
