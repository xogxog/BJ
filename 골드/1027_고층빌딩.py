import sys
input = sys.stdin.readline


N = int(input())
ls = list(map(int,input().split()))
ans = 0

if N == 1 :
    print(0)

else :
    for i in range(N) : # 기준
        l = 1000000001 # 왼쪽 기울기
        r = -1000000001 # 오른쪽 기울기
        cnt = 0 # 볼 수 있는 건물

        # 왼쪽 보기
        for j in range(i-1,-1,-1) :
            tmp_l = (ls[i]-ls[j])/(i-j)
            if tmp_l < l : # 왼쪽건물은 기울기가 점점 작아져야함
                l = tmp_l
                cnt += 1


        # 오른쪽 보기
        for k in range(i+1,N):
            tmp_r = (ls[k] - ls[i]) / (k - i)
            if tmp_r > r :
                r = tmp_r
                cnt += 1
        ans = max(ans,cnt)
    print(ans)
