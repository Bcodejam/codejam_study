N = int(input())
dp = [0 for _ in range(N + 1)]
#입력값이 홀수면 답은 무조건 0
if N % 2 == 1:
  print(0)
  exit()
#N == 2 일경우 경우의수 3
dp[2] = 3
for i in range(3, N + 1) :
  if i%2 == 0:
    dp[i] = sum(dp[2: i-2]) * 2 + dp[i-2] * 3 + 2 
print(dp[N])