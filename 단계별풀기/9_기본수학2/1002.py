T = int(input())

for tc in range(T) :
    ls = list(map(int,input().split()))

    r1 = ls[2]
    r2 = ls[5]
    distance = ((abs(ls[0]-ls[3]))**2 + (abs(ls[1]-ls[4]))**2)**(1/2)
    if ls[0] == ls[3] and ls[1] == ls[4] and r1 == r2 :
        print(-1)
    elif ls[0] == ls[3] and ls[1] == ls[4] and r1 != r2 :
        print(0)
    elif distance < r1+r2 or max(r1,r2)>=distance and distance > abs(r1-r2):
        print(2)
    elif distance == r1+r2 or max(r1,r2)>=distance and distance == abs(r1-r2):
        print(1)
    else :
        print(0)
