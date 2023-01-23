from collections import deque

N, K = map(int, input().split())
lst = list(map(str, input().split()))
string = ''.join(lst)

answer = sorted(lst)
answerString = ''.join(answer)

visited = set()


#depth , 문자열을 저장
q = deque([[ 0 , string]])

while q :
  depth , s = q.popleft()
  #sort 된 문자열일경우
  if s == answerString :
    #깊이 출력하고 종료
    print(depth)
    exit()
  

  if s not in visited :
    if N - K + 1 <= N :
      for i in range(0 , N - K + 1) :
        #i부터 K 길이만큼 문자열 뒤집기
        j = i + K -1 
        tmp = list(s)
        tmp[i : j+1] = tmp[i : j+1][::-1]
        s_new = ''.join(tmp)
        q.append([depth + 1 , s_new])
        visited.add(s)
            
print(-1)

       
    
        
        