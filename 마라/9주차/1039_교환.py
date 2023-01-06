from collections import deque

N , K = map(int, input().split())
q = deque()
visited = [[False for _ in range(1000001)] for _ in range(11)]
length = len(str(N))
#숫자 , times(bfs의 깊이) 를 저장
q.append([N, 0])
lst = []
while q :
    num , times = q.popleft()
    #K번 만족했을경우
    if times == K  :
        lst.append(num)
    if times < K :
        visited[times][num] = True
        for i in range(length) :
            for j in range(i + 1, length) :
                numStr = str(num)
                #i 와 j를 바꿨을때 맨앞이 0이면 안됨
                if numStr[j] == '0' and i == 0 :
                    continue
                else :
                    tmp = numStr[i]
                    numStr = list(numStr)
                    numStr[i] = numStr[j]
                    numStr[j] = tmp
                    newNum = int(''.join(numStr))
                    if not visited[times+1][newNum] :
                        q.append([newNum, times + 1])
                        visited[times+1][newNum] = True

if len(lst) == 0:
    print(-1)
else :
    print(max(lst))