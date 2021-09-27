import sys

N = int(sys.stdin.readline())
word=[]

ls= []
for i in range(N) :
    w = sys.stdin.readline().rstrip()
    if w not in word:
        word.append(w)
        ls.append([len(w), w])

ls.sort()

for i in range(len(ls)):
    print(ls[i][1])