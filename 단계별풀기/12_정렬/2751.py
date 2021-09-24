# 수 정렬하기 2
# O(nlogN) // 힙, 병합정렬 ( 풀이 해볼 것 )

import sys
N = int(sys.stdin.readline())

ls = []
for i in range(N) :
    ls.append(int(sys.stdin.readline()))

ls.sort()

for j in range(len(ls)) :
    print(ls[j])