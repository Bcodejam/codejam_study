import sys

input = sys.stdin.readline

n = int(input().rstrip())
list_n = list(map(int, input().rstrip().split()))

m,M = float("inf"), float("-inf")

for i in list_n:
    if m > i: m = i
    if M < i: M = i

print(m, M)