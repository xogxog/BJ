import sys
input = sys.stdin.readline

n,k = map(int,input().split())
coins = list(int(input()) for _ in range(n))
ls = [987654321]*(k+1)
ls[0]= 0
for i in range(k+1) :
    for j in range(n) :
        if i+coins[j]< k+1 :
            ls[i+coins[j]] = min(ls[i+coins[j]], ls[i]+1)
if ls[-1] == 987654321 :
    print(-1)
else :
    print(ls[-1])