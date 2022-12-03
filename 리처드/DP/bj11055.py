import sys

input = sys.stdin.readline

n = int(input().rstrip())

list_n = list(map(int, input().rstrip().split()))
list_ans = [list_n[0]]
l = len(list_n)
ans = list_n[0]
for i in range(1, l):
    val = list_n[i]
    tmp = list_n[i]
    for j in range(i-1, -1, -1):
        if val > list_n[j]:
            tmp = max(tmp, list_ans[j] + val)
    list_ans.append(tmp)
    ans = max(ans, tmp)

print(ans)