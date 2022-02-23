# 이런방법이 ,,
# 원래 접근은 모든 수를 보는 것이었는데 시간초과가 났다.
# 이 접근법은 현재 칠할 색깔 보다 전집에선 나머지 두색깔중 더 숫자가 작은걸 색칠하고, 현재 칠할색을 더해서
# 결국 리스트 마지막엔 최소로 다 칠했을 경우가 3개나오는데 그 중 제일 작은 수를 출력..

import sys

n = int(sys.stdin.readline())

RGB = [list(map(int,input().split())) for _ in range(n)]

for i in range(1,n) :
    RGB[i][0] = min(RGB[i-1][1], RGB[i-1][2]) + RGB[i][0] # red
    RGB[i][1] = min(RGB[i-1][0], RGB[i-1][2]) + RGB[i][1] # green
    RGB[i][2] = min(RGB[i-1][0], RGB[i-1][1]) + RGB[i][2] #blue
# print(RGB)
print(min(RGB[n-1]))


# def check(tmp,depth, before_color):
#     global min_cost
#     if depth == N :
#         # print(color)
#         if tmp < min_cost :
#             min_cost = tmp
#         return
#
#     if tmp >= min_cost :
#         return
#
#     for i in range(0,3):
#         if before_color != i : # 전에 칠한 색과 다르다면
#             # color[depth] = i
#             check(tmp+ls[depth][i], depth+1, i)
#
#
#
# N = int(input())
# ls=[list(map(int,input().split())) for _ in range(N)]
# # visited = [[0]*3 for _ in range(N)]
# color = [-1]*N
# min_cost = 987654321
# depth=1 # 인덱스 기준
# before_color = 0
# for i in range(3) :
#     color[0]= i # 1번 색칠
#     before_color = i
#     check(ls[0][i],depth, before_color)
#
# print(min_cost)