# 동전분배 ( 펠린드롬말고 다른방법 써야할듯 )
# 다이나믹 프로그래밍
import sys
input = sys.stdin.readline

# def check_money(start, A_money) :
#     global ans, flag
#     if A_money == total_money - A_money:
#         flag = 1
#         ans = 1
#         return
#     if start == len(money_list)-1 :
#         return
#
#     for j in range(start,len(money_list)) :
#         A_money += money_list[j]
#         check_money(start + 1 , A_money)
#         A_money -= money_list[j]
#         if flag :
#             return

for tc in range(3) :
    N = int(input())
    total_money = 0
    money_list = []
    accumul_money_list = []
    ans = 0
    flag= 0
    for _ in range(N) :
        price, cnt = map(int,input().split())
        total_money += price * cnt
        for i in range(cnt) :
            money_list.append(price)
    money_list.sort()
    accumul_money_list.append(money_list[0])
    for j in range(1,len(money_list)) :
        accumul_money_list.append(accumul_money_list[j-1]+money_list[j])
    # print(accumul_money_list)

    for k in range(len(accumul_money_list)) :
        if accumul_money_list[k] == total_money // 2 :
            ans = 1
            print(1)
            break
        else :
            for l in range(0,k) :
                if accumul_money_list[k]-accumul_money_list[l] == total_money // 2 :
                    ans = 1
                    break
        if ans == 1 :
            print(ans)
            break

    if ans == 0 :
        print(ans)