import sys
input = sys.stdin.readline
N = int(input())
ls = list(map(int,input().split()))
dic = {}
for num in ls :
    dic[num]= 1
M=int(input())
compare_ls = list(map(int,input().split()))
for num in compare_ls :
    try :
        if dic[num] == 1:
            print(1)
    except :
        print(0)