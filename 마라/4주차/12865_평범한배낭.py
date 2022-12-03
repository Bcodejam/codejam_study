N , K = map(int, input().split())
lst = [[0,0]]
dp = [[0 for _ in range(K+1)] for _ in range(N+1)]
for _ in range(N) :
  lst.append(list(map(int, input().split())))


for i in range(1, N+1) :
  for j in range(1, K+1) :
    volume = lst[i][0]
    value = lst[i][1]
    if volume > j :
      # 가정한 부피가 넣을 부피보다 작은 경우
      dp[i][j] = dp[i-1][j]
    else:
      dp[i][j] = max(dp[i-1][j] , dp[i-1][j-volume] + value)

print(dp[N][K])