def chessPaint(board) : #8X8 보드에서 몇개 칠해야하는지 구하는 함수
  vsList = []
  paint = 0
  board88 = 'BWBWBWBWWBWBWBWBBWBWBWBWWBWBWBWBBWBWBWBWWBWBWBWBBWBWBWBWWBWBWBWB' #B로 시작할때 
  for i in range(0 , 64):
      if board[i] != board88[i]:
        paint += 1
  vsList.append(paint)
  paint = 0
  board88 = 'WBWBWBWBBWBWBWBWWBWBWBWBBWBWBWBWWBWBWBWBBWBWBWBWWBWBWBWBBWBWBWBW'  #W로 시작할때 
  for i in range(0 , 64):
      if board[i] != board88[i]:
        paint += 1
  vsList.append(paint)
  #B로 시작할때와 W로 시작할때 중 작은 경우 선택
  return min(vsList) 


N , M = map(int, input().split())
boardList = []
for i in range(N):
    boardList.append(input())


answerList = []            

for i in range(0 , N - 7): #시작점 찾기
    for j in range(0 , M - 7):
        lst=''
        for n in range(i , i + 8): #8X8으로 자르기 
            for m in range(j , j + 8):
                lst += boardList[n][m]
        answerList.append(chessPaint(lst)) #자른 체스판 얼마나 칠할지 구하여 answerList에 넣기

print(min(answerList)) #answerList에서 가장 작은 수