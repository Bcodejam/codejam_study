import sys
import heapq

input = sys.stdin.readline

n = int(input().rstrip())
day = 0
q = []

for i in range(n):
    q_tmp = list(map(int, input().rstrip().split()))
    day = max(day, q_tmp[0])
    for j in range(len(q_tmp)): q_tmp[j] *= -1
    heapq.heappush(q, q_tmp)
ans = 0
while True:
    if day == 0: break
    list_tmp = []
    le = len(q)
    for i in range(le):
        a,b = heapq.heappop(q)
        if day <= (a * -1):
            heapq.heappush(list_tmp, [b,a])
        else:
            heapq.heappush(q, [a,b])

    if len(list_tmp) > 0:
        a,b = heapq.heappop(list_tmp)
        ans += -1*a

    while list_tmp:
        a, b = heapq.heappop(list_tmp)
        heapq.heappush(q, [b,a])

    day -= 1

print(ans)