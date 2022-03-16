from collections import deque
a,b = map(int,input().split())

q = deque([(a,1)])
ans = -1
while q :
    aa, i = q.popleft()
    if aa == b :
        ans = i
        break
    if aa*2 <=b :
        q.append((aa*2,i+1))
    if aa*10 + 1 <= b :
        q.append((aa*10 + 1, i+1))

print(ans)