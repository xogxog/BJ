ls_1=[1,0,1]
ls_2=[0,1,1]
for i in range(3,41) :
    ls_1.append(ls_1[i-1]+ls_1[i-2])
    ls_2.append(ls_2[i-1]+ls_2[i-2])

for _ in range(int(input())) :
    n = int(input())
    print(ls_1[n], ls_2[n])