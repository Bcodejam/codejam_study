import sys

input = sys.stdin.readline

n = int(input().rstrip())
list_dp = [0, 0, 1]

for i in range(3, n+1):
    if i % 2 == 0 and i % 3 != 0:
        list_dp.append(min(list_dp[i-1], list_dp[i//2]) + 1)
    elif i % 3 == 0 and i % 2 != 0:
        list_dp.append(min(list_dp[i-1], list_dp[i//3]) + 1)
    elif i % 2 == 0 and i % 3 == 0:
        list_dp.append(min(list_dp[i-1], min(list_dp[i//2], list_dp[i//3])) + 1)
    else:
        list_dp.append(list_dp[i-1] + 1)

print(list_dp[n])