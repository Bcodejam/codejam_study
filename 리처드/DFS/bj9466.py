import sys

input = sys.stdin.readline

test = int(input().rstrip())

def dfs(i, chk, tmp, a):
    chk += 1
    a.append(1)
    if tmp == list_n[i-1]-1:
        print(tmp)
        return chk
    if chk == n or i == list_n[i-1]:
        # print(chk)
        return 0
    return dfs(list_n[i-1], chk, tmp, a)

for _ in range(test):
    n = int(input().rstrip())
    list_n = list(map(int, input().rstrip().split()))
    ans = 0
    list_chk = [0]*n
    for i in range(n):
        if list_chk[i-1] == 0:
            ans += dfs(list_n[i], 0, i, [])
    print(ans)
    print(n - ans)


'''
2
7
3 1 3 7 3 4 6
8
1 2 3 4 5 6 7 8
'''
'''
1
7
3 1 3 7 3 4 6
'''