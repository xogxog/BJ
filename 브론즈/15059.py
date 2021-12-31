menu = list(map(int,input().split()))
choice = list(map(int,input().split()))

answer = 0

for i in range(len(menu)) :
    if choice[i] > menu[i] :
        answer += (choice[i]-menu[i])
print(answer)
