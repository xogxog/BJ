# 인덱스 유효성 검사 항상 하기!!!

N = int(input()) # 스위치 개수
switch = [0] + list(map(int,input().split()))

S_n = int(input()) #학생의 수

for i in range(S_n) :
    sex, num = map(int,input().split())

    if sex == 1 : # 남학생인 경우
        multi = 1
        while num * multi < len(switch) :
            switch[num * multi] = 1- switch[num * multi]
            multi += 1

    else : #여학생인 경우
        switch[num] = 1 - switch[num] # 자기 방번호 바꾸기
        change = 1
        while True :
            if 1<= num-change <N+1 and 1<= num+change <N+1 and switch[num-change] == switch[num+change] : # 양옆이 같은 경우
                switch[num-change] = 1 - switch[num-change]
                switch[num+change] = 1 - switch[num+change]
                change += 1
            else :
                break

for i in range(1,N+1) :
    print(switch[i], end = " ")
    if i % 20 == 0 :
        print()