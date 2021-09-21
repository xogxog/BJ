import sys
import math
while True :

    n = int(sys.stdin.readline())

    if n == 0 :
        break

    else :
        cnt = 0
        for i in range(n+1, (2*n)+1) :
            flag = 0
            if i == 0 or i == 1:
                continue
            for j in range(2, int(math.sqrt(i))+1) :
                if i % j == 0:
                    flag = 1
                    break
            if flag == 1:
                continue
            elif flag == 0:
                cnt += 1
        print(cnt)