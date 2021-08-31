word = list(input())
cnt = 0
for i in range(len(word)) :
    cnt += 1
    if word[i] == "=" or word[i] == "-":
        if i-2>=0 and word[i-1]=="z" and word[i-2] == "d" :
            cnt -= 2
        elif word[i-1] in ("c","d","s","z") :
             cnt -= 1
    elif word[i] =="j" :
        if i-1>=0 and word[i-1] =="l" or word[i-1] =="n":
            cnt -= 1
print(cnt)