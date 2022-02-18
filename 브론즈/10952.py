flag= 1
while flag:
    a, b = map(int, input().split())
    if not a and not b :
        flag=0
    else :
        print(a+b)
