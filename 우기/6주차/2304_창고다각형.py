import sys

n = int(sys.stdin.readline().rstrip())
info = []
max_info = (-1, -1)
for _ in range(n):
    x, h = map(int, sys.stdin.readline().rstrip().split())
    if h > max_info[1]:
        max_info = (x, h)
    info.append((x, h))

length = max(info, key=lambda item: item[0])[0] + 1

arr = [0] * length
for x, h in info:
    arr[x] = h

last_h = -1
for i in range(1, length):
    if i == max_info[0]:
        break
    last_h = max(arr[i], last_h)
    arr[i] = last_h

last_h = -1
for i in range(length - 1, 0, -1):
    if i == max_info[0]:
        break
    last_h = max(arr[i], last_h)
    arr[i] = last_h

print(sum(arr))
