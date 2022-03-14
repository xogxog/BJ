# 리모컨
import sys
input = sys.stdin.readline
number = int(input()) # 가고싶은 채널
b = int(input()) # 부순 리모컨숫자

break_nums = list(map(int,input().split())) # 부순 숫자
not_break_nums =[]
for i in range(10):
    if i not in break_nums :
        not_break_nums.append(i)

