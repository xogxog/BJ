import sys


def VPS(words):
    stack = []
    if words[-1] == '(' or words[0] == ')':
        return 'NO'
    else:
        for word in words:
            if word == '(':
                stack.append(word)
            else:
                if len(stack) > 0:
                    stack.pop()
                else:
                    return 'NO'
    if len(stack) == 0:
        return 'YES'
    else:
        return 'NO'



N = int(sys.stdin.readline())

for _ in range(N):
    words = sys.stdin.readline().rstrip()
    print(VPS(words))