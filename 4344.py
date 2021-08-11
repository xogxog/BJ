T = int(input()) #test case

for t in range(T):
    N_score = list(map(int, input().split()))

    avg=sum(N_score[1:])/N_score[0] #sum for문말고 짧게 쓸수 있을까?

    cnt =0
    for i in N_score[1:] :
        if i > avg :
            cnt +=1
        else : pass

    print(f'{round(cnt/N_score[0]*100,3):.3f}%')