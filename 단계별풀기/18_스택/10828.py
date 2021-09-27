# 스택
import sys
N = int(sys.stdin.readline())

ls = []

stack=[]

for _ in range(N):
    word = sys.stdin.readline().rstrip()

    if word.find('push') != -1 : # push 단어 찾는경우
        a, num = word.split()
        stack.append(num)
    elif word == 'top' :
        if len(stack) >0 :
            print(stack[-1])
        else :
            print(-1)
    elif word == 'size' :
        print(len(stack))
    elif word == 'empty' :
        if len(stack) > 0 :
            print(0)
        else :
            print(1)
    elif word == 'pop' :
        if len(stack) > 0 :
            print(stack.pop())
        else :
            print(-1)

