from collections import deque

N = int(input())
cards = deque(i for i in range(1,N+1))

while len(cards) >1 :
    cards.popleft()
    tmp = cards.popleft()
    cards.append(tmp)

print(cards[0])