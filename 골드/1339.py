import sys
input = sys.stdin.readline

alphabet = {}
for _ in range(int(input())):
    tmp_word = input().rstrip()

    for i in range(len(tmp_word)) :
        if tmp_word[i] not in alphabet :
            alphabet[tmp_word[i]] = 10 ** (len(tmp_word)-i-1)
        else :
            alphabet[tmp_word[i]] += 10 ** (len(tmp_word)-i-1)

alphabet = sorted(alphabet.items(), key=lambda x : x[1], reverse = True)
ans = 0
tmp_num = 9
for alpha, num in alphabet :
    ans += num * tmp_num
    tmp_num -= 1
print(ans)