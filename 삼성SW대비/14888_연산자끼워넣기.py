# 순열 직접 구현하기
# def combi(idx):
#     if idx == len(oper_ls):
#         combi_oper.add(tuple(tmp_ls))
#         return
#     for i in range(len(oper_ls)):
#         if not visited[i]:
#             visited[i] = 1
#             tmp_ls[idx] = oper_ls[i]
#             combi(idx+1)
#             visited[i] = 0
#
# N = int(input())
# nums = list(map(int,input().split()))
#
# operators = ['+','-','*','/']
# oper_cnt = list(map(int,input().split()))
# oper_ls = []
# for i in range(len(oper_cnt)) :
#     if i == 0 :
#         oper_ls += ['+'] * oper_cnt[i]
#     elif i == 1 :
#         oper_ls += ['-'] * oper_cnt[i]
#     elif i == 2 :
#         oper_ls += ['*'] * oper_cnt[i]
#     else :
#         oper_ls += ['/'] * oper_cnt[i]
#
# visited = [0]*len(oper_ls)
# tmp_ls = ['']*len(oper_ls)
# combi_oper = set()
# combi(0)
# combi_oper = list(combi_oper)
#
# min_ans = 1000000001
# max_ans = -1000000001
#
# for i in range(len(combi_oper)):
#     tmp_ans = nums[0]
#     for j in range(len(combi_oper[i])):
#         if combi_oper[i][j] == '+':
#             tmp_ans += nums[j+1]
#         elif combi_oper[i][j] == '-':
#             tmp_ans -= nums[j + 1]
#         elif combi_oper[i][j] == '*':
#             tmp_ans *= nums[j + 1]
#         else :
#             if tmp_ans < 0 :
#                 tmp_ans *= -1
#                 tmp_ans = -1*(tmp_ans//nums[j + 1])
#             else :
#                 tmp_ans //=nums[j + 1]
#     min_ans = min(min_ans, tmp_ans)
#     max_ans = max(max_ans, tmp_ans)
#
# print(max_ans)
# print(min_ans)


# 풀이 2
