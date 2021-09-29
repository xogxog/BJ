#오큰수

import sys

N = int(sys.stdin.readline().rstrip())
ls = list(map(int,sys.stdin.readline().split()))

stack =[[0,ls[0]]] # index값, ls 값 넣어줌
ans = [-1] * N

for i in range(1,len(ls)) :
    while stack and (stack[-1][1] < ls[i]) :
        idx, num = stack.pop()
        ans[idx] = ls[i]
    stack.append([i,ls[i]])

print(* ans)



# def NGE() :
    # 시간초과
    # start = 0
    # end = 1
    # ans = []
    # while True:
    #     while end < len(ls) and ls[start] > ls[end]:
    #         end += 1
    #         while end == len(ls) - 1 and ls[start] > ls[end]:  # 끝까지 왔는데 큰 수가 없다면
    #             ans.append(-1)
    #             start += 1
    #             if end == start: # 내림차순인 경우, 모두 -1값을 가진다.
    #                 break
    #
    #     while ls[start] < ls[end]:
    #         ans.append(ls[end])
    #         start += 1
    #         if end < len(ls)-1 and start == end:
    #             end += 1
    #
    #     if start == end and end == len(ls)-1 :
    #         print(-1)
    #         return


# 시간초과~!~!
# for i in range(len(ls)) :
#     if i == len(ls) -1 :
#         print(-1)
#     else :
#         for j in range(i+1,len(ls)) :
#             if ls[i] > max(ls[j:]) :
#                 print(-1,end=' ')
#                 break
#             elif ls[i] < ls[j] :
#                 print(ls[j],end=' ')
#                 break

# print(' '.join(map(str,NGE())))

