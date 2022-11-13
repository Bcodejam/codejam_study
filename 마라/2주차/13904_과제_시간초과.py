# 시간초과

import sys


N = sys.stdin.readline()

lst = []

for _ in range(int(N)):
  lst.append(list(map(int, sys.stdin.readline().split())))

lst.sort(key = lambda x : (-x[0]))

answer = 0
date = lst[0][0]
index = 0 


while date > 0 and index <= int(N) :
  if lst[index][0] == 0 : 
    continue
  if date > lst[index][0] :
    date -= 1
    continue
  else :
    tmp = 0
    tmpIndex = 0
    for i in range(index , int(N)) :
      if date > lst[i][0] :
        break
      if date <= lst[i][0] :
        if tmp < lst[i][1] :
          tmp = lst[i][1]
          tmpIndex = i
    answer += lst[tmpIndex][1]
    lst[tmpIndex] = [0,0]
    index += 1
    date -= 1


print(answer)