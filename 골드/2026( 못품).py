# 소풍
import sys
input = sys.stdin.readline
#1~N명의 학생, 소풍가게될 K, 친구관계정보 F
K,N,F = map(int,input().split())
relationship = [[0]*(N) for _ in range(N)]
for _ in range(F) :
  a, b =map(int,input().split())
  relationship[a-1][b-1] = 1
  relationship[b-1][a-1] = 1
for z in range(N) :
  print(*relationship[z])
checked = [0]*(N) # 0~N-1까지 학생 친구 체크
tmp_ans = [] # 경우의 수가 하나인 경우
tmp_ans2 = [] # 경우의 수가 여러개인 경우
group_chk = 0
for i in range(N) :
  if relationship[i].count(1) >= K-1 :
    if not group_chk and not checked[i] : 
      checked[i] = 1
      group_chk += 1
      tmp_ans.append(i)
      for j in range(N) : # 중복 없애기 위함
        if relationship[i][j] == 1 :
          checked[j] = 1
          tmp_ans.append(j)
    elif not checked[i] and group_chk == 1 :
      tmp_ans2.append(tmp_ans[0])
      for k in range(N) :
        if relationship[i][k] == 1 :
          if k not in tmp_ans2 :
            tmp_ans2.append(k)
            break
    elif not checked[i] :
      for l in range(N) :
        if relationship[i][l] == 1 :
          if l not in tmp_ans2 :
            tmp_ans2.append(l)
            break

if len(tmp_ans) == 0 :
  print(-1)
elif len(tmp_ans) > 0 and len(tmp_ans2) == 0 :
  for student in tmp_ans :
    print(student+1)
else :
  for student2 in tmp_ans2 :
    print(student2+1)




