ls = []
ls2=[]

for i in range(3):
    a, b = map(int, input().split())
    ls.append(a)
    ls2.append(b)

for j in range(3):
    if ls.count(ls[j]) == 1 :
        a = str(ls[j])

    if ls2.count(ls2[j]) == 1 :
        b = str(ls2[j])

print(a+' '+b)