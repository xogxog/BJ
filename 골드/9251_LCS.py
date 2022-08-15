import sys
input = sys.stdin.readline

a = [""] + list(input().rstrip())
b = [""] + list(input().rstrip())

ls = [[0]*len(b) for _ in range(len(a))]

for i in range(1,len(a)) :
    for j in range(1,len(b)) :
        if a[i] == b[j] :
            ls[i][j] = ls[i-1][j-1]+1
        else :
            ls[i][j] = max(ls[i][j-1],ls[i-1][j])

print(ls[-1][-1])