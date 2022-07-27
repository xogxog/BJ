# A와 B
# 작은 것 부터 시작하면 경우의 수가 너무 많아짐
# 아이디어 큰 -> 작
import sys
input = sys.stdin.readline

S = list(input().rstrip())
T = list(input().rstrip())
s = len(S)
t = len(T)

while s != t :
    if T[-1] == 'A':
        T.pop() # 자르기
        t -= 1
    elif T[-1] == 'B':
        T.pop()
        T = T[::-1]
        t -= 1


if ''.join(S) == ''.join(T):
    print(1)
else :
    print(0)