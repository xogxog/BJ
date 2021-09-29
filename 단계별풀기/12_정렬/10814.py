import sys
N = int(sys.stdin.readline().rstrip())

ls=[]
dic={}

for i in range(N) :
    age , name = sys.stdin.readline().split()
    age = int(age)
    ls.append([i,age])
    dic[i] = name

ls.sort(key=lambda x : x[1])

for j in ls :
    print(j[1], dic.get(j[0]))