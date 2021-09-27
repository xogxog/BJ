# 좌표압축

import sys

N = int(sys.stdin.readline())
ls = list(map(int, sys.stdin.readline().split()))
sorted_ls = sorted(set(ls))
# print(sorted_ls)
dic ={sorted_ls[i] : i for i in range(len(sorted_ls))}

for j in ls :
    print(dic[j], end=' ')