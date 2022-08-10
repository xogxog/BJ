# 팰린드롬?

import sys

input = sys.stdin.readline

N = int(input()) # 수열의 크기
nums = list(map(int,input().split()))
ls = [[0]*(N) for _ in range(N)]

for i in range(N) :
    ls[i][i] = 1
    if i < N-1 and nums[i] == nums[i+1]:
        ls[i][i+1] = 1

for j in range(2,N) : # 몇칸 띄울지
    for k in range(N-j): # 기준점
        if nums[k] == nums[k+j] and ls[k+1][k+j-1] :
            ls[k][k+j] = 1

for l in range(int(input())) :
    S,E = map(int,input().split())
    print(ls[S-1][E-1])