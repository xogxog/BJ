N= int(input())
ls = []
for i in range(N):
    ls.append(list(map(int,input().split())))

ls.sort()

for i in range(N):
    print(' '.join(map(str,ls[i])))


