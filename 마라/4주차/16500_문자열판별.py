S = input()
N = int(input())
lst= []

#dp[i] 는 S[0:i+1]이 lst안의 단어로 나타낼 수 있는지를 저장
dp = [0 for _ in range(len(S))]

for _ in range(N) :
  lst.append(input())
  

for i in range(len(S)) : 
  #처음시작부터 i 까지 가 lst 안에 있을경우
  if S[0:i+1] in lst: 
    dp[i] = 1
    continue
  for j in range(i) :
    #처음 시작부터 j까지가 lst 안의 단어로 만들수있는경우
    if dp[j] == 1: 
      #j부터 i까지도 만들 수 있는지 검사
      if S[j+1:i+1] in lst : 
        dp[i] = 1

print(dp[len(S)-1])