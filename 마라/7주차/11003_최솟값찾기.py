from collections import deque


n, l = map(int, input().split())
lst = list(map(int, input().split()))

answer = [0] * n

#[index, value] 가 저장될 큐 
dq = deque()


for idx in range(n):

  #현재 값보다 큐의 오른쪽 값이 더 클경우 pop
  while dq and dq[-1][1] > lst[idx]:
    dq.pop()

  #(왼쪽부터) 검사 범위를 벗어난 경우 pop
  while dq and idx - dq[0][0] >= l:
    dq.popleft()

  dq.append((idx, lst[idx]))

  #큐는 항상 오름차순 + 검사 범위 가 유지될것이므로
  #for문을 돌때마다 첫번째 원소의 값이 해당 범위의 최솟값이다.
  answer[idx] = dq[0][1]

  
print(*answer)

    