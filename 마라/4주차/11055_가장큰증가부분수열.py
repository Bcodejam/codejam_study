N = int(input())

lst= list(map(int, input().split()))
#그냥 answerList = lst 로 하면 틀림
answerList = lst[:]

for i in range(N) : 
  for j in range(0 , i) :
    if lst[i] > lst[j] : # 증가 수열이면
      # j까지 더했던 값 + 현재 i 값 vs i까지 더한 값
      answerList[i] = max(answerList[j] + lst[i] ,answerList[i])
    
print(max(answerList))