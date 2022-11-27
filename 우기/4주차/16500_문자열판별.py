# coding=utf-8
import sys


def solve(idx):
    # 문자열 끝까지 성공한 경우 -> 만들 수 있음
    if idx == len(target):
        dp[-1] = 1
        return

    else:
        # 1이 아닌 경우 (1인 경우는 이미 체크 끝난거)
        if dp[idx] != 1:
            dp[idx] = 1

            for i in range(n):
                # 길이 체크
                if len(target[idx:]) >= len(words[i]):
                    # 부분문자열 체크
                    for j in range(len(words[i])):
                        if target[idx + j] != words[i][j]:
                            break
                    
                    else:
                        # 부분문자열이면 그 단어 길이만큼 idx 증가 + 재귀
                        solve(idx + len(words[i]))


target = sys.stdin.readline().strip()
n = int(sys.stdin.readline())
words = []

for _ in range(n):
    words.append(sys.stdin.readline().strip())

dp = [0] * (len(target) + 1)
solve(0)

print(dp[-1])
