# 틀린이유 : 무조건 4자리수이므로, 123의 R연산이면 312가아니라, 2031이 되어야한다...
import sys
from collections import deque
input = sys.stdin.readline

for _ in range(int(input())) :
    A ,B = map(int,input().split())
    visited=[0]*10000
    q=deque([(A,'')])
    visited[A] = 1
    while 1 :

        N, ans = q.popleft()

        if N == B :
            print(ans)
            break
        else :
            # if N*2 > 9999 :
            if not visited[(N*2)%10000] :
                q.append(((N*2)%10000,ans+'D'))
                visited[(N*2)%10000] = 1
            # else :
            #     if not visited[N*2] :
            #         q.append((N*2,ans+'D'))
            #         visited[N * 2] = 1
            if N == 0 :
                if not visited[9999]:
                    q.append((9999,ans+'S'))
                    visited[9999] =1
            else :
                if not visited[N-1] :
                    q.append((N-1,ans+'S'))
                    visited[N-1] = 1

            L = (N%1000)*10 + N//1000
            R = (N%10)*1000 + N//10
            if not visited[L]:
                q.append((L, ans+'L'))
                visited[L] = 1
            if not visited[R] :
                visited[R] = 1
                q.append((R,ans+'R'))