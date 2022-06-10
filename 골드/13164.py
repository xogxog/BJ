import sys
input = sys.stdin.readline

N,K = map(int,input().split())

num_list = list(map(int,input().split()))
minus_ls = []
for i in range(len(num_list)-1) :
    minus_ls.append(num_list[i+1]-num_list[i])

minus_ls.sort()

print(sum(minus_ls[0:len(minus_ls)-(K-1)]))