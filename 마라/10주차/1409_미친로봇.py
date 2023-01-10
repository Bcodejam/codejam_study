import copy

N, dong, seo , nam , buck = map(int, input().split())

visited = [[False for _ in range(30)] for _ in range(30)]
answer = float(0)

def dfs(x, y, depth, percent) :
    global answer
    global visited
    if depth == N :
        answer += percent
        print(str(x) + str(y) + "자리에서" + str(depth) + "깊이에서" + str(percent) )
        return 
    visited[x][y] = True
    if not visited[x+1][y] and dong != 0 and x+1 < 30 and y < 30:
        dfs(x+1, y, depth + 1 , percent * dong * (0.01))
        visited[x +1][y] = False
    if not visited[x-1][y] and seo != 0 and x-1 < 30 and y < 30:
        dfs(x-1, y, depth + 1 , percent * seo * (0.01))
        visited[x-1][y] = False
    if not visited[x][y-1] and nam != 0 and x < 30 and y-1 < 30:
        dfs(x, y-1, depth + 1 , percent * nam * (0.01))
        visited[x][y-1] = False
    if not visited[x][y+1] and buck != 0 and x < 30 and y+1 < 30:
        dfs(x, y+1, depth + 1 , percent * buck * (0.01))
        visited[x][y+1] = False

dfs(14, 14, 0, 1)
print(answer)