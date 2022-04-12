import sys
input = sys.stdin.readline
for _ in range(3) :
    N = int(input())
    ans = 0
    for i in range(N):
        ans += int(input())
    if ans == 0 :
        print(0)
    elif ans > 0 :
        print('+')
    else :
        print('-')