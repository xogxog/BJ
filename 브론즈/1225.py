import sys
input = sys.stdin.readline

a,b = map(str,input().split())
a_ls = []
b_ls = []
if a == '0' or b == '0' :
    print(0)
else :
    for _a in a :
        a_ls.append(int(_a))
    for _b in b :
        b_ls.append(int(_b))
    ans = 0
    for i in range(len(a_ls)) :
        for j in range(len(b_ls)) :
           ans += a_ls[i]*b_ls[j]
    print(ans)