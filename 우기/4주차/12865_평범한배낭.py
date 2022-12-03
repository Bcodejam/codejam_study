# coding=utf-8
import sys

n, k = map(int, sys.stdin.readline().split())
arr = [(0, 0)]
for _ in range(n):
    w, v = map(int, sys.stdin.readline().split())
    arr.append((w, v))

# dp[n][k] -> n번째 까지 봤을 때, 최대 무게 k인 배낭의 최대 가치
dp = [[0 for _ in range(k + 1)] for _ in range(n + 1)]

for i in range(1, n + 1):
    # 가방의 최대 무게 양을 1씩 늘려감
    for j in range(1, k + 1):
        w, v = arr[i]
        # 현재 가방 허용 무게보다 크면 안담음
        if j < w:
            dp[i][j] = dp[i - 1][j]
        # 현재 물건 안넣었을때 최대 값, 넣었을 때 최대값중 큰 값
        else:
            dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - w] + v)

print(dp[n][k])
