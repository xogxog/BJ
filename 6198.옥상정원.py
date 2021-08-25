N = int(input())
buildings =[]
for i in range(N) :
    buildings.append(int(input()))

cnt = 0
for i in range(N-1) :
    for j in range(i+1, N) :
       if buildings[i] > buildings[j] :
           cnt += 1
           # print(buildings[i], cnt)
       else :
           break
print(cnt)