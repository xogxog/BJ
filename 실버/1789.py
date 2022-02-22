# 수열 공식!
# 1+2+3+4+...+n = {n*(n+1)}/2

s = int(input())

i=0
sum = 0
while True :
    i += 1
    sum1 = (i*(i+1))//2
    sum2 = ((i + 1) * (i + 2)) // 2

    if sum1 <= s and sum2 > s:
        break  # 조건이 맞아떨어지면 반복문을 중단하고
print(i)  # 출력한다.