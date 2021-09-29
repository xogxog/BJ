# 프린터 큐
from collections import deque
import sys

def paper_print(curr, cnt) :
    if len(papers) == 1 :
        return 1

    while True :
        tmp = papers.popleft()
        if len(papers) > 0:
            if tmp < max(papers) :
                papers.append(tmp)
                if curr > 0:
                    curr -= 1
                else :
                     curr = len(papers)-1

            elif tmp >= max(papers) :
                if curr == 0 :
                    cnt += 1
                    return cnt
                else :
                    cnt+=1
                    curr -=1

        else :
            cnt += 1
            return cnt




T = int(input())
for _ in range(T) :
    N , M = map(int, sys.stdin.readline().split()) # 문서 갯수, 몇 번째로 인쇄되었는지 궁금한 문서가 현재 몇번째에 놓여있는지 나타내는 정수
    papers = deque(list((map(int,sys.stdin.readline().split()))))

    # print(papers)

    curr = M
    cnt = 0

    print(paper_print(curr, cnt))

