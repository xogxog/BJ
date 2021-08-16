def MySearch(x) :
    n = int((2*x)**(1/2))
    while (n**2) + (3*n) >= 2*(x-1) :
        n-=1
        # print(n)
    cnt = int((n**2 + 3*n) / 2) + 1
    # print(cnt)


    #print(n)
    if n % 2 : #홀수이면
        row = n+1-(x-cnt-1) # 한칸 내려간 뒤, x-cnt-1만큼 위로 올라감
        col = x-cnt-1 # 가장 왼쪽에 있으니, 옮겨야하는 남은수(x-cnt) 에 +1칸 움직인다.
        return row,col

    else : #짝수이면
        col = n+1 - (x-cnt-1) #한칸 오른쪽으로 옮긴 후에, x-cnt-1만큼 왼쪽으로 이동
        row = x-cnt-1
        return row,col


x = int(input())

curr_loca = MySearch(x)
print(str(curr_loca[0] + 1) + '/' + str(curr_loca[1] + 1))




