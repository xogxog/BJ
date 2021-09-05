result = 1
for i in range(3):
    result *= int(input())

str_result = str(result)

cnt = [0,0,0,0,0,0,0,0,0,0]

for i in range(len(str_result)) :
    cnt[int(str_result[i])] += 1

for j in range(10):
    print(cnt[j])
