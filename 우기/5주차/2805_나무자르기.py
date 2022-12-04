import sys

ans = 0
n, m = map(int, sys.stdin.readline().rstrip().split())
trees = list(map(int, sys.stdin.readline().rstrip().split()))

h = 0
low = 0
high = max(trees)
wood = 0

while low <= high:
    h = (low + high) // 2

    wood = 0
    for t in trees:
        if t > h:
            wood += (t - h)

    if wood > m:
        low = h + 1
        ans = h
    elif wood < m:
        high = h - 1
        ans = high
    else:
        ans = h
        break

print(ans)
