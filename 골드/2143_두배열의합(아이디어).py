# 이게 이분탐색 .. ?
import sys
from collections import defaultdict
input = sys.stdin.readline

T = int(input())

a = int(input())
A = list(map(int,input().split()))
b = int(input())
B = list(map(int,input().split()))

ans = 0

dictA = defaultdict(int)
dictB = defaultdict(int)

# 딕셔너리 - 부분합 수 : 부분합한 수의 경우의 수
for i in range(a) :
    for j in range(i,a):
        dictA[sum(A[i:j+1])] += 1

for k in range(b):
    for l in range(k,b):
        dictB[sum(B[k:l+1])] += 1


for key in dictA.keys() :
    ans += dictB[T-key] * dictA[key]
print(ans)