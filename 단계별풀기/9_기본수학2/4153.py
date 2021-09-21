#코드를 줄여보자
# 함수로 만들면 될 듯.

while True :
    a,b,c= map(int,input().split())

    if a==0 and b == 0 and c == 0 :
        break
    else :
        if a == 0 or b == 0 or c == 0 :
            print('wrong')
        if max(a,b,c) == a :
            if b**2 + c**2 == a**2 :
                print('right')
            else :
                print('wrong')
        elif max(a,b,c) == b :
            if a**2 + c**2 == b**2 :
                print('right')
            else :
                print('wrong')
        else :
            if a**2 + b**2 == c**2 :
                print('right')
            else :
                print('wrong')