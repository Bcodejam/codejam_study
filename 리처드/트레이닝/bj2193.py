import sys

input = sys.stdin.readline

n = int(input().rstrip())

list_n = [0, 1, 1]

for i in range(3, n+1):
    list_n.append(list_n[i-1] + list_n[i-2])

print(list_n[-1])