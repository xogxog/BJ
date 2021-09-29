# 요세푸스 문제 0
from collections import deque
N,K = map(int,input().split())

people = deque([i for i in range(1,N+1)])
ans=[]
num = 1
while len(people) > 0 :
    if num % K == 0 :
        ans.append(people.popleft())
    else :
        tmp = people.popleft()
        people.append(tmp)
    num = (num % K) + 1

print('<{}>'.format(', '.join(map(str,ans))))
