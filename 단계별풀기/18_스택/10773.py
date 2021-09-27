import sys

N = int(sys.stdin.readline())

stack =[]
for i in range(N):
    a = sys.stdin.readline().rstrip()
    if a == '0' :
        stack.pop()
    else :
        stack.append(int(a))

print(sum(stack))