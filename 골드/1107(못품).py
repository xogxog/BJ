# 리모컨
import sys
input = sys.stdin.readline
number = int(input()) # 가고싶은 채널
b = int(input()) # 부순 리모컨숫자갯수

break_nums = list(input().split()) # 부순 숫자
ans = abs(100-number) # +or - 버튼만 눌러서 가는 경우

for num in range(10000001):
    for N in str(num):
        if N in break_nums :
            break
    else :
        ans = min(ans, len(str(num)) + abs(num - number))

print(ans)


