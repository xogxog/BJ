import sys

def lookable_buildings(buildings) :
    stack = []  # (idx,높이)

    for i,hei in buildings: # 빌딩 idx, 높이
        if not stack:  # 스택에 아무것도 없으면
            stack.append((i,hei))

        elif stack[-1][1] <= hei:  # 들어오려는 건물이 더 크면
            while stack and stack[-1][1] <= hei:  # 안보일 건물 다빼기
                stack.pop()  # 안보이니까 원래꺼 빼기기
            if len(stack):  # 왼쪽에 보이는 건물이 있다면
                record[i][0] += len(stack)  # 건물 갯수
                if record[i][1] == 0:  # 처음 가까운 건물 넣는 경우
                    record[i][1] = stack[-1][0]  # 가까운 건물 번호 넣어줌
                elif abs(record[i][1] - i) > abs(stack[-1][0] - i):  # 현재건물에서 기존 가까운거리와 새로 들어올 건물 거리 비교해서 새로들어올 거리가 더 적으면 갱신
                    record[i][1] = stack[-1][0]  # 가장가까운 건물번호 중 가장 거리가 작은 번호

            stack.append((i,hei))

        else:  # 들어오는 건물이 작으면
            record[i][0] += len(stack)
            if record[i][1] == 0:
                record[i][1] = stack[-1][0]
            elif abs(record[i][1] - i) > abs(stack[-1][0] - i):
                record[i][1] = stack[-1][0]
            stack.append((i,hei))

    #     print(f'stack : {stack}')
    #     print(f'records : {record}')
    # print(f'한 방향 끝')

n = int(input())

buildings = list(map(int,sys.stdin.readline().split()))
buildings = list(zip(range(1,n+1),buildings)) # idx, 높이
reverse_buildings = sorted(buildings, reverse=True)
record = [[0,0]for _ in range(n+1)] # 각 건물에서 보이는 건물갯수, 가장가까운 건물번호 (건물갯수, 건물번호)

lookable_buildings(buildings)
lookable_buildings(reverse_buildings)
# print(f'=============================')
# print(f'records : {record}')

record = record[1:] # 가장 처음 것 잘라줘야함

for idx,num in record :
    if idx == 0 :
        print(0)
    else :
        print(idx,num)