j,r = map(int,input().split()) # 선수 수, 라운드 수
point = list(map(int,input().split()))
ls = [0]*j
_max = 0
idx = 0
for i in range(len(point)) :
    ls[i%j] += point[i]

for j in range(len(ls)) :
    if _max <= ls[j] :
        _max = max(_max,ls[j])
        idx = j+1
print(idx)
