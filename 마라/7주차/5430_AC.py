from collections import deque

N = int(input())

def test(queue, function) :
  rTime = 0
  for c in function :
    #R이 나올때마다 reverse 하면 비효율적 -> 횟수를 기록하여 홀수번 나왔을 경우에만 reverse
    if c == "R" : 
      rTime += 1
    if c == "D" :
      if len(queue) == 0:
        print("error")
        return 
      #여태 R 이 짝수번 나왔으면 오른쪽에서 pop
      if rTime % 2 == 0 :
        queue.popleft()
      #여태 R 이 홀수번 나왔으면 왼쪽에서 pop
      else :
        queue.pop()
  #최종 R이 홀수번 나왔으면 reverse
  if rTime % 2 == 1 :
    queue.reverse()
  print('['+','.join(list(queue))+']')
  return 
      
      

for _ in range(N) :
  p = input()
  n = int(input())
  lstString = input()
  tmp = lstString[1:-1].split(",")
  lst = []
  #공백 없애주기(리스트 크기가 0인경우를 위함)
  for t in tmp :
    if t != '' :
      lst.append(t)
  q = deque(lst)
  test(q, p)