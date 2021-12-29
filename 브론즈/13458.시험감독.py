import sys

n = int(sys.stdin.readline())
people_in_class = list(map(int,sys.stdin.readline().split()))
main_supervisor, sub_supervisor = map(int, sys.stdin.readline().split())

# print(n, people_in_class, main,sub)
result = 0
for i in range(n) :
    if people_in_class[i] >= main_supervisor : # 마이너스 값일 때 나눠도 값이 나와버리기 때문에 이 조건문을 꼭 넣어줘야한다.
        people_in_class[i] -= main_supervisor
        sub1 = people_in_class[i] // sub_supervisor

        if people_in_class[i] % sub_supervisor != 0 :
            result += sub1 +1
        else :
            result += sub1


print(result +n)

