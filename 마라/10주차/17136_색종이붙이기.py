import sys

#r,c에서 시작하여 length 만큼의 색종이로 바꿀수있는지 
def check(r, c, length, full):
    for i in range(length):
        full -= sum(papers[r+i][c:c+length])
    if full:
        return False
    else:
        return True

def recursive(one, cnt):
    global answer
    #모든 1을 채웠을경우
    if one == 0:
        #cnt가 저장되어있던 answer보다 작을경우 업데이트
        answer = min(answer, cnt)
        return
    #현재 사용한 색종이 수가 저장된 answer 보다 크거나 같을 경우 , 더이상 계산할 필요없다.
    if cnt >= answer:
        return
    #주어진 색종이를 다 썼을경우
    if sum(used) == 0:
        return
    for r in range(10):
        for c in range(10):
            if papers[r][c]:
                #length마다 돌아가면서 r,c에 채울수 있는지 검사한다.
                for length in range(5, 0, -1):
                    #length길이의 색종이가 있고, 10x10를 넘어가지 않을 경우
                    if used[length] and r+length <= 10 and c+length <= 10:
                        #r,c부터 채울수 있는지 검사, 채울수 있다면
                        if check(r, c, length, length**2):
                            #해당 범위를 1-> 0으로 바꾼다.
                            for i in range(r, r+length):
                                for j in range(c, c+length):
                                    papers[i][j] = 0
                            #사용한 색종이 하나 감소
                            used[length] -= 1
                            #1의 수(one)와 사용한 색종이 수(cnt)를 업데이트하고 재귀
                            recursive(one - length**2, cnt+1)
                            #다른 재귀에 방해되지 않도록 원복해준다
                            for i in range(r, r+length):
                                for j in range(c, c+length):
                                    papers[i][j] = 1
                            #색종이의 수도 원복
                            used[length] += 1
                return

papers = []
used = [0]+[5]*5
#가능한 answer은 최대 100이다
answer = 101
one = 0
for _ in range(10):
    paper = list(map(int, sys.stdin.readline().split()))
    one += sum(paper)
    papers.append(paper)
if not one:
    print(0)
else:
    recursive(one, 0)
    print(-1) if answer == 101 else print(answer)