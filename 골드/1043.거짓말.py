n,m = map(int,input().split()) # 사람 수, 파티 수
know = set(list(map(int,input().split()))[1:])

party = []
for _ in range(m):
    tmp = list(map(int, input().split()))[1:]
    party.append(tmp)
for _ in range(len(party)) :
    for i in range(len(party)) :
        flag = 0
        for person in party[i] :
            if person in know :
                flag = 1
                know.update(party[i])
            if flag :
                break
# print(party)
# print(know)
cnt = len(party)
for j in range(len(party)) :
    flag2 = 0
    for k in range(len(party[j])) :
        if party[j][k] in know :
            flag2 = 1
            cnt -= 1
        if flag2 :
            break
print(cnt)