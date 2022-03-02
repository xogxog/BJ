from collections import Counter
import sys
input =sys.stdin.readline
ls =[]
sum = 0
for _ in range(int(input())) :
    a= int(input())
    ls.append(a)
    sum += a

ls.sort()
cnt = Counter(ls)
cnt = cnt.most_common()

print(round(sum/len(ls))) # 산술평균
print(ls[len(ls)//2]) #중앙값
#최빈값
if len(cnt)>1 and cnt[0][1] == cnt[1][1] :
    # for i in range(len(cnt)) :
    #     if cnt[0][1] == cnt[i][1] :
    #         continue
    #     else :
    #         cnt = cnt[:i+1]
    #         break
    # cnt.sort(key=lambda x : x[0])
    print(cnt[1][0])
else :
    print(cnt[0][0])
print(ls[-1]-ls[0])

