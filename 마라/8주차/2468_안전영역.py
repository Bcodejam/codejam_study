import sys

N = int(input())

sys.setrecursionlimit(1000*9)

board = []
#최대 높이 찾기위함
forMax =[]
visited =[]

dx = [-1, 1 , 0, 0]
dy = [0, 0, -1, 1]

for _ in range(N) :
  board.append(list(map(int, input().split())))
  
for row in board :
  forMax += row
  visited.append([False for _ in range(N)])

#최대 높이
maxHeight = max(forMax)

def dfs(x, y, height) :
  visited[x][y] = True
  for i in range(4):
    nx = x + dx[i]
    ny = y + dy[i]
    if nx < N and ny < N and nx >= 0 and ny >= 0 :
      if not visited[nx][ny] and board[nx][ny] > height:
        dfs(nx, ny, height)

safeAreaList =[0]

#최대높이로 물이 찼을때 ~ 0까지 검사
for h in range(maxHeight, -1, -1) :
  #검사할때마다 visited 초기화
  for i in range(len(visited)) :
    visited[i] = [False for _ in range(N)]

  safeArea = 0
  for i in range(N) :
    for j in range(N):
      #방문한적 없고, 물에잠기지않으면 
      if not visited[i][j] and board[i][j] > h:
        safeArea += 1
        dfs(i ,j ,h)
  safeAreaList.append(safeArea)

print(max(safeAreaList))