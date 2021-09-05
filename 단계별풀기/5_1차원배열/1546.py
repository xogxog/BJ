N = int(input())

ls = list(map(int,input().split()))

max_score = max(ls)
new_scores = 0
for i in range(N) :
    ls[i] = ls[i]/max_score*100
    new_scores += ls[i]



print(new_scores/N)