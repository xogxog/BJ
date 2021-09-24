#카운팅정렬로 풀라는데 못하겠어 ㅎㅎ

import sys
N = int(input())

ls=[]
for _ in range(N):
    ls.append(int(sys.stdin.readline()))
# print(ls)
# print(max(ls))
# 메모리 초과^^;;
# for j in range(N-1):
#     mean_idx = j
#     for k in range(j,N):
#         if ls[mean_idx] >= ls[k]  :
#             mean_idx = k
#     ls[j] , ls[mean_idx] = ls[mean_idx], ls[j]
#
# print(ls)

cnt = [] # 리스트에 해당 숫자가 몇개 있는지 세어준걸 넣을 리스트
sub_total =[]# 누적합 저장해 줄 리스트

already_count = [] # 이미 세어준 숫자

# 인덱스랑 갯수 같이 넣어준다.
for i in range(N) :
    if ls[i] not in already_count :
        cnt.append([ls[i],ls.count(ls[i])])
        already_count.append(ls[i])
        if len(cnt) == 1 :
            sub_total.append([ls[i], cnt[len(cnt)-1][1]])
        else :
            sub_total.append([ls[i], cnt[len(cnt)-1][1] + sub_total[len(cnt)-2][1]])
print(cnt)
print(sub_total)


# sorted_ls =[0] * (N+1)
# for j in range(len(ls)-1,0,-1):
#
#     sorted_ls[sub_total[ls[j]]] = ls[j]
#     sub_total[ls[j]] -= 1
#
#
# for k in range(len(sorted_ls)):
#     if sorted_ls[k] :
#         print(sorted_ls[k])