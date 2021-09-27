import sys

while True :
    words= sys.stdin.readline().rstrip()
    if words == '.':
        break
    stack = []
    for word in words :
        if word == '.': # 마지막에 마침표
            if len(stack) == 0 : # 스택이 없다는 것은 균형
                print('yes')
            else : #스택에 남아있다는 것은 균형 X
                print('no')
            break
        else :
            if word == '(' or word == '[': # 열린 괄호는 stack에 넣어주기
                stack.append(word)
            elif word ==')' or word == ']':
                if len(stack) > 0 :
                    if stack[-1] == '(' and word == ')': # 짝이 맞으면 pop
                        stack.pop()
                    elif stack[-1] == '[' and word == ']':
                        stack.pop()
                    else : # 짝이 맞지 않은 경우 no하고 반복문 종료
                        print('no')
                        break
                else : # 열린 괄호가 없는데 닫힌 괄호가 있는 경우
                    print('no')
                    break
