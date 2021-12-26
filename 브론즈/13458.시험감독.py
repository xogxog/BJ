import sys

n = int(sys.stdin.readline())
people_in_class = list(map(int,sys.stdin.readline().split()))
main_supervisor, sub_supervisor = map(int, sys.stdin.readline().split())

# print(n, people_in_class, main,sub)
result = n
for i in range(n) :
    people_in_class[i] -= main_supervisor
    cnt = 1
    if people_in_class[i] > 0 :
        while True :
            num_of_sub_supervisor = sub_supervisor * cnt
            if num_of_sub_supervisor >= people_in_class[i] :
                break
            else :
                cnt += 1
    result += cnt


print(result)