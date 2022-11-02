import sys
from itertools import combinations

ans = 0
n, s = map(int, sys.stdin.readline().rstrip().split())
arr = list(map(int, sys.stdin.readline().rstrip().split()))

# 수열의 모든 조합 계산
for i in range(1, n + 1):
    cases = combinations(range(0, n), i)
    for c in cases:
        # 조합으로 뽑은 애들 -> sum으로 더함
        if sum([arr[idx] for idx in c]) == s:
            ans += 1

print(ans)

