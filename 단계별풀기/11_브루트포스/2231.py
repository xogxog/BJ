N = int(input())
ppl = []
for _ in range(N):
    ppl.append(list(map(int,input().split())))


rank = [1] * N

for i in range(N-1) :
    for j in range(i+1,N) :
        if ppl[i][0] > ppl[j][0] and ppl[i][1] > ppl[j][1] :
            rank[j] += 1
        elif ppl[i][0] < ppl[j][0] and ppl[i][1] < ppl[j][1] :
            rank[i] += 1

print(' '.join(map(str,rank)))
