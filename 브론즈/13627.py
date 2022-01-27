n,r = map(int,input().split())
comeback = list(map(int,input().split()))
check = [0]*(1+n)
for i in range(r) :
    check[comeback[i]] = 1
ans=[]

for j in range(1,len(check)):
    if check[j] == 0 :
        ans.append(j)

if len(ans) == 0 :
    print('*')
else :
    print(*ans)