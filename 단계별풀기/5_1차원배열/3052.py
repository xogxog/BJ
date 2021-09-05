cnt=[]

for i in range(10) :
    num = int(input()) % 42
    if num not in cnt :
        cnt.append(num)

print(len(cnt))