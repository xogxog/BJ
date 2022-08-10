# 문자열 폭발
import sys
from collections import deque
input = sys.stdin.readline
word = input().rstrip()
bomb = input().rstrip()
cnt = len(bomb)
s = []

for w in word :
    s.append(w)
    if s[-1] == bomb[-1] :
        if ''.join(s[-cnt:]) == bomb :
            del s[-cnt:]
            # for _ in range(cnt) :
            #     s.pop()
if len(s) != 0 :
    print(''.join(s))
else :
    print('FRULA')















# q = deque()
# left_q = deque()
#
# flag = 1 # 폭발할 문자열이 남았는지 체크용
# left_word = len(word) # 남은 문자열
# compare_word = 0
#
# for i in range(len(word)) :
#     q.append((word[i],i))
#
# idx = 0
# cnt = 0
# tmp_word = ''
# tmp_q = []
# while flag :
#
#     w = q.popleft()
#
#     if idx == 0 and w[0] == bomb[idx]:
#         tmp_q.append(w)
#         tmp_word += w[0]
#         idx += 1
#
#     # 첫번째 문자열 이후, 폭발 문자와 같고
#     elif idx and w[0] == bomb[idx] :
#         tmp_q.append(w)
#         tmp_word += w[0]
#         idx += 1
#
#     # 그 다음것이 폭발 문자열이 아니라면 다시 초기화 시켜줘야함
#     elif idx and w[0] != bomb[idx] :
#         for j in range(len(tmp_q)):
#             left_q.append(tmp_q[j])
#         tmp_q = []
#         idx = 0
#         tmp_word = ''
#         if w[0] == bomb[idx] :
#             tmp_q.append(w)
#             tmp_word += w[0]
#             idx += 1
#
#     # 폭발 문자열이 아니면
#     else :
#         left_q.append(w)
#
#     # 폭발 문자열 발견 시
#     if tmp_word == bomb :
#         cnt += len(bomb)
#         idx = 0
#         tmp_word = ''
#         tmp_q = []
#
#     # 한바퀴 다돌고 일단 break
#     if not len(q) :
#
#         compare_word = len(left_q)
#         if compare_word == 0 :
#             break
#         else :
#             q = deque([l[:] for l in left_q])
#             left_q = deque()
#             if compare_word != left_word :
#                 left_word = compare_word
#             elif compare_word == left_word :
#                 break
#
# ans = ''
#
# if not compare_word :
#     print(f'FRULA')
# else :
#     while q :
#         w_2, __ = q.popleft()
#         ans += w_2
#     print(ans)