from collections import deque

#퍼즐 배열을 string 으로 저장
visited = set()
answer = "123456780"

board = ""
for _ in range(3) :
  board += ''.join(list(map(str, input().split())))

q = deque()
q.append([board, 0])

#퍼즐 자리 옮기는 함수
def change(string, i , j) :
  string = list(string)
  tmp = string[i]
  string[i] = string[j]
  string[j] = tmp
  return ''.join(string)

while q:
  puzzle, depth = q.popleft()

  #퍼즐이 123456780 잘 맞춰졌으면
  if puzzle == answer :
    print(depth)
    exit()

  else :
    visited.add(puzzle)
    
    #비어있는 곳 index
    empty = puzzle.find('0')
    
    #왼쪽 퍼즐 0으로 이동
    left = empty - 1
    #퍼즐이 범위를 벗어나지 않는 경우에만
    if left % 3 != 2 and left >= 0 and left < 9 :
      newPuzzle = change(puzzle, left, empty)
      if newPuzzle not in visited :
        q.append([newPuzzle , depth+1])
        visited.add(newPuzzle)

    right = empty + 1
    if right % 3 != 0 and right >= 0 and right < 9:
      newPuzzle = change(puzzle, right, empty)
      if newPuzzle not in visited :
        q.append([newPuzzle , depth+1])
        visited.add(newPuzzle)

    down = empty + 3
    if down >= 0 and down < 9 :
      newPuzzle = change(puzzle, down, empty)
      if newPuzzle not in visited :
        q.append([newPuzzle , depth+1])
        visited.add(newPuzzle)

    up = empty - 3
    if up >= 0 and up < 9 :
      newPuzzle = change(puzzle, up, empty)
      if newPuzzle  not in visited :
        q.append([newPuzzle , depth+1])
        visited.add(newPuzzle)

#퍼즐 못맞출 경우
print(-1) 