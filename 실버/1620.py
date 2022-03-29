import sys
input = sys.stdin.readline
N,M = map(int,input().split())
dic ={}
n = 1
for _ in range(N) :
    poke = input().rstrip('\n')
    dic[str(n)] = poke
    dic[poke] = str(n)
    n+=1

for _ in range(M):
    print(dic[input().rstrip('\n')])
