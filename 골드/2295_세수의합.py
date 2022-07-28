# 세 수의 합 - 이것도 아이디어 ,,,
# O(n^3) 너무 오래걸리니까 , a+b+c = d
# 를 a+b = d-c
import sys
from collections import defaultdict

input = sys.stdin.readline
N = int(input())
ls = []
for _ in range(N):
    ls.append(int(input()))
ls.sort()

dictSum = defaultdict(int)
for i in range(N):
    for j in range(i,N):
        dictSum[ls[i]+ls[j]] += 1

# def check():
#
#     for k in range(N-1,-1,-1):
#         for l in range(k,-1,-1):
#             if dictSum[ls[k]-ls[l]] :
#                 print(ls[k])
#                 return
#
# check()

# 이분탐색

Minus_ls = set()

for k in range(N-1,-1,-1):
    for l in range(N-1,-1,-1):
        Minus_ls.add((k,l,ls[k]-ls[l]))
