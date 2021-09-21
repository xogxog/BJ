# 식 다시 쓰기
import sys
T = int(input())
# h, w, n : 호텔 층, 각층의 방수, 손님
for tc in range(T):
    h, w, n = map(int, sys.stdin.readline().rstrip().split())
    # h, w, n = map(int, input().split())
    if h == 1 :
        print(100+n)
    else :
        room_num, floor = divmod(n,h)
        # print(room[1],room[0])
        
        if floor == 0:
            print(h*100+room_num)
        else:
            print(floor*100 + room_num+1)