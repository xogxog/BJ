a,b = map(int,input().split())

if a>0 and b>0 :
    print(a//b)
    print(a%b)
elif a>0 and b<0 :
    print(-(a // -b))
    print(a % -b)
elif a<0 and b>0 :
    tmp = -(-a // b)-1
    print(tmp)
    print(-(b*tmp)+a)
elif a<0 and b<0 :
    tmp = (a // b)+1
    print(tmp)
    print(-(b * tmp) + a)
else:
    print(0)
    print(0)