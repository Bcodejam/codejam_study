import sys

input = sys.stdin.readline

n = int(input().rstrip())

list_n = [0, 1, 2, 3]

for i in range(4, n+1):
    tmp = (list_n[i-1] + list_n[i-2]) % 15746
    list_n.append(tmp)

print(list_n[n])