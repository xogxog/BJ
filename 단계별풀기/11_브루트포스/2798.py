

def blackjack(cards,m) :
    my_m = 0
    for i in range(len(cards)):
        for j in range(i+1,len(cards)):
            for k in range(j+1,len(cards)):
                if cards[i] + cards[j] + cards[k] == m :
                    return cards[i] + cards[j] + cards[k]
                elif cards[i] + cards[j] + cards[k] <= m:
                    if cards[i] + cards[j] + cards[k] > my_m :
                        my_m = cards[i] + cards[j] + cards[k]
    return my_m






n, m = map(int, input().split())

cards = list(map(int, input().split()))

print(blackjack(cards,m))