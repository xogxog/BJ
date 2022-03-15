n=int(input())

ls=[0,1,2]

if n <= 2 :
    print(ls[n])
else :
    for i in range(3,n+1) :
        ls.append(ls[i-1]+ls[i-2])
    print(ls[-1] % 10007)