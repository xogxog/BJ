b = list(map(int,input().split())) # bessie
d = list(map(int,input().split())) #daisy
target = list(map(int,input().split()))

# b의 경로
b_cnt = max(abs(b[0]-target[0]), abs(b[1]-target[1]))
#d의 경로
d_cnt = abs(d[0]-target[0]) + abs(d[1]-target[1])
if b_cnt == d_cnt :
    print('tie')
elif b_cnt > d_cnt :
    print('daisy')
else :
    print('bessie')