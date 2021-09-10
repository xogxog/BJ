N = int(input())
cnt = 0
for i in range(N):
    words = input()
    ls =[words[0]]
    flag=0
    for j in range(1, len(words)) :
        # print(ls)
        if words[j] in ls and words[j-1] != words[j] :
            # print(f'{words}')
            flag=1
        elif words[j] not in ls : 
            ls.append(words[j])

        if flag :
            break
    else : cnt +=1

print(cnt)