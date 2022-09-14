# 투 포인터
import sys
from collections import defaultdict
input = sys.stdin.readline
N = int(input())
meow = input().rstrip()

alpha = 'abcdefghijklmnopqrstuvwxyz'
dic = defaultdict(int)
for al in alpha :
    dic[al] = 0

end = 0
cnt = 1
dic[meow[0]] += 1
ans = 0
flag = 0
for start in range(len(meow)):

    while cnt < N and end + 1 < len(meow) :
        end += 1
        if dic[meow[end]] == 0 :
            cnt += 1
        dic[meow[end]] += 1
        # 인식할 수 있는 수에 비해 알파벳 수가 적은 경우
        if start == 0 and end == len(meow)-1:
            ans = len(meow)

    if cnt == N:
        while end+1<len(meow) and dic[meow[end+1]] != 0 :
            end += 1
            dic[meow[end]] += 1

        ans = max(ans,(end-start)+1)

    dic[meow[start]] -= 1
    if dic[meow[start]] == 0 :
        cnt -= 1
print(ans)
