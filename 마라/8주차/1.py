import sys
sys.setrecursionlimit(10**8)

lst = []
# index가 팀이 된 상태인지
teamed = []
teamTmp = []
index = 0
cnt = 0
def dfs(start, next) :
    global index
    global cnt
    #처음 시작부터 끝까지 1사이클인경우
    if start == next :
        index = 0
        return True
    #루틴 중간에 사이클이 만들어졌을경우
    if next in teamTmp :
        index = next
        return True
    if teamed[next] or teamed[start] :
        return False
    if lst[next] == next :
        cnt += 1 
        teamed[next] = True
        return False
    if lst[start] == start :
        cnt += 1 
        teamed[start] = True
        return False
    teamTmp.append(next)
    a = dfs(start, lst[next])
    return a



T = int(input())
for _ in range(T) :
    cnt = 0
    N = int(input())
    lst = [0] + list(map(int, input().split()))
    teamed = [False for _ in range(N+1)]
    for i in lst :
        teamTmp = [i]
        if not teamed[i] :
            if dfs(i, lst[i]) :
                if index == 0:
                    for j in teamTmp:
                        cnt += 1
                        teamed[j] = True
                #루틴 중간에 사이클이 만들어졌을경우
                else :
                    flag = False
                    for j in teamTmp :
                        if j == index :
                            flag = True
                        if flag :
                            cnt += 1
                            teamed[j] = True


    # for j in teamed :
    #     if not j:
    #         answer += 1
    print(N - cnt + 1)        
              

