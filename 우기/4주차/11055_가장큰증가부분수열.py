import sys

n = int(sys.stdin.readline().rstrip())
arr = list(map(int, sys.stdin.readline().rstrip().split()))

dp = [0] * n
dp[0] = arr[0]

for i in range(1, len(dp)):
    # 지금까지 값들 중에서
    # 현재 값보다 작으면서 + 가장 큰 합을 더함
    max_sum = 0
    for j in range(i):
        if arr[i] > arr[j]:
            max_sum = max(max_sum, dp[j])

    dp[i] = max_sum + arr[i]

print(max(dp))
