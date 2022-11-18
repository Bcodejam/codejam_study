lst = []

def divide(x , y , width) :
  firstNum = lst[x][y]
  for r in range(x, x + width) :
    for c in range(y, y + width) :
      if lst[r][c] != firstNum : #모두 같은 숫자가 아닌경우
        # 4등분해서 재귀
        newWidth = width //2 
        print("(", end="")
        divide(x, y, newWidth)
        divide(x  , y + newWidth, newWidth)
        divide(x+ newWidth , y  , newWidth)
        divide(x + newWidth , y + newWidth, newWidth)
        print(")", end="")
        return 

  # lst[r][c] != firstNum 인 경우 없이 for문을 다 돌면
  print(str(lst[x][y]), end ="")
  return 

N = int(input())
for _ in range(N):
    lst.append(list(map(int, list(input().rstrip()))))
divide(0 , 0 , N)