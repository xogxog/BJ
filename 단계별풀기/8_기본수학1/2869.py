A, B, V = map(int, input().split()) # A : 올라감 , B : 미끄러짐, V : 나무막대길이

# snail = 0
# days = 0
# 런타임 에러
# while snail < V :
#     snail += A
#     if snail >=V:
#         days += 1
#         break
#     snail -= B
#     days += 1
#     print(days)
#
# print(days)

# n =(V-B) / (A-B)
n = divmod(V-B , A-B)
if n[1] > 0 :
    print(n[0]+1)
else :
    print(n[0])
