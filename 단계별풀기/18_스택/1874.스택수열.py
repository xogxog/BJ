"""
8
1
3
2
4
3
5
4
6
"""

N = int(input())
ls = []
for _ in range(N):
    ls.append(int(input()))

num = 1
point = 0
stack = []
ans = []
while num <= N or stack :
    if num <= ls[point] :
        stack.append(num)
        ans.append('+')
        if num == ls[point] :
            stack.pop()
            point += 1
            ans.append('-')
        num += 1

    elif num > ls[point] :
        tmp = stack.pop()
        if tmp == ls[point] :
            ans.append('-')
            point += 1
        else :
            ans.append('NO')
            break

if ans[-1] =='NO':
    print('NO')
else :
    for i in range(len(ans)) :
        print(ans[i])







