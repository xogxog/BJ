cnt = [0] * 10001

i = 1

while i < 10000 :
    num = i
    d_n = num
    while num > 0 :
        d_n += (num % 10)
        num //= 10
    # print(d_n)
    if d_n >10000 :
        pass
    else : cnt[d_n] += 1
    i +=1


# print(cnt)
for j in range(1,len(cnt)) :
    if cnt[j] == 0 :
        print(j)