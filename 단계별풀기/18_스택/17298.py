#오큰수

import sys

def NGE() :
    start = 0
    end = 1
    ans = []
    while True:
        while end < len(ls) and ls[start] > ls[end]:
            end += 1
            # print(f'1 : start : {start}, end : {end}')
            # print(f'1 :{ans}')
            while end == len(ls) - 1 and ls[start] > ls[end]:  # 끝까지 왔는데 큰 수가 없다면
                print(-1, end=' ')
                # ans.append(-1)
                start += 1
                # print(f'2 : start : {start}, end : {end}')
                # print(f'2 :{ans}')
                if end == start: # 내림차순인 경우, 모두 -1값을 가진다.
                    break

        while ls[start] < ls[end]:
            # ans.append(ls[end])
            print(ls[end], end=' ')
            start += 1
            if end < len(ls)-1 and start == end:
                end += 1
            # print(f'3 : start : {start}, end : {end}')
            # print(f'3 :{ans}')

        if start == end and end == len(ls)-1 :
            ans.append(-1)
            print(-1)
            # print(f'4 : start : {start}, end : {end}')
            # print(f'4 :{ans}')
            # return ans
            return






N = int(sys.stdin.readline().rstrip())

ls = list(map(int,sys.stdin.readline().split()))

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

NGE()
