"""
8
4
3
6
8
7
5
2
1
"""

def stack(arr) :
    stack = []
    top = -1
    sorted_arr = sorted(arr)  # 스택에 넣어줄 수
    j=0
    result=''
    for i in range(len(arr)):
        if arr[i] < sorted_arr[j]:
            if sorted_arr[top] == arr[i]:
                # stack.pop()
                result += '-'
                top -= 1
            else:
                return 'NO'
        # if arr[i] > arr[i + 1]:
        else :
            while sorted_arr[j] < arr[i]:
                # stack.append(j)
                j += 1  # 4
                top += 1
                result += '+'
            result += '+'
            result += '-'
            # stack.pop()
            # top -=1
            j += 1
    return result
        # else:






N = int(input())
arr = []  # 입력된 수열을 받을 리스트 변수

for _ in range(N):
    arr.append(int(input()))

result = stack(arr)
if result == 'NO':
    print('NO')
else:
    for i in range(0,len(result)):
        print(result[i])









