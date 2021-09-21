m=int(input())
n=int(input())
total = 0
flag2 = 0
my_min = 0

for i in range(m,n+1):
    flag = 0
    if i == 0 or i == 1:
        continue
    for j in range(2, i) :
        if i % j == 0 :
            flag = 1
            break
    if flag == 1 :
        continue
    elif flag == 0 :
        total += i
        flag2 += 1
    if flag2 == 1 :
       my_min = i

if total == 0 :
    print(-1)
else :
    print(total)
    print(my_min)
