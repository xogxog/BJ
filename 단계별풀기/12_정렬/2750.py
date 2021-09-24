# 수 정렬하기
import sys
N = int(sys.stdin.readline())

ls = []

for i in range(N) :
    ls.append(int(sys.stdin.readline()))

ls.sort()

for j in range(len(ls)) :
    print(ls[j])
