# 문제에서는 1000 자리수 까지라 더 간단하게 짤 수 있지만
# 3자리 이상일 때도 활용할 수 있도록 짰다.

N = int(input())

def is_that_true(N):
    cnt = 99

    for i in range(100,N+1) :
        flag = 0
        ls = []
        while i>0 :
            ls.append(i%10)
            i//=10
        # print(ls)
        a_b= ls[0] - ls[1]
        for j in range(1,len(ls)-1) :
            if a_b != ls[j]-ls[j+1] :
                flag = 1
                break
        if flag == 0 :
            cnt += 1

    return cnt


if N < 100 :
    print(N)


if N >= 100 :
    result = is_that_true(N)
    print(result)