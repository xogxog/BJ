import sys
input = sys.stdin.readline

N = input().strip()
n_len = len(N)
if n_len == 1 :
    print(N)
else :
    tmp_num = '9' * (n_len-1)
    ans = 0
    ans += (int(N)-int(tmp_num))*n_len
    while 1 :
        cnt = 2
        if len(tmp_num) == 1:
           ans += 9
           break
        else :
            tmp_num2 = '9'*(n_len-cnt)
            ans +=(int(tmp_num)-int(tmp_num2))*len(tmp_num)
            cnt += 1
            tmp_num = tmp_num2
    print(ans)
