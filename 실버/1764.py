# 듣보잡
import sys
input = sys.stdin.readline
ppl_list = {}
dont_know = []
n,m = map(int,input().split())

for _ in range(n+m) :
    name = input().rstrip('\n')
    if name in ppl_list :
        dont_know.append(name)
    else :
        ppl_list[name] = 1
dont_know.sort()
print(len(dont_know))
print('\n'.join(dont_know))
