# 아 ... split이 있었지...
import sys
input = sys.stdin.readline

ls = input().split('-')
s= 0
for i in ls[0].split('+') :
    s+=int(i)
for i in ls[1:]:
    for j in i.split('+'):
        s-=int(j)
print(s)