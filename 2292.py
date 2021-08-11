N = int(input())

# N_list = [i for i in range(2,N+1)]
#
# bee_list=[[1]] #첫번째 값은 그냥 받아 놓는다.
# flag = 0
# i = 2 #계산 기준
# while flag <= N :# 여기 수정하자..!!
#
#     cutting = i+(4*(i-1))+(i-2)
#     if len(N_list) < cutting : break
#     bee_list.append(N_list[0:cutting])
#
#     flag = N_list[cutting-1]
#     i += 1
#
#     del N_list[0:cutting]
# if len(N_list)>0 :bee_list.append(N_list)
#
# print(bee_list)
# print(len(bee_list))

total = 1
cnt = 1
i = 2
while total < N:
    total += i+(4*(i-1))+(i-2)
    i += 1
    cnt += 1
if total < N : cnt += 1
print(cnt)