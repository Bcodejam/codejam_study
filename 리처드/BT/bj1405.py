import sys

input = sys.stdin.readline

n, a, b, c, d = map(int, input().rstrip().split())


a /= 100
b /= 100
c /= 100
d /= 100

ans = 0

def func(n_tmp, prob, li):
    global ans
    if n_tmp == 0:
        ans += prob
        return
    if [li[-1][0] + 1, li[-1][1]] not in li and a > 0:
        func(n_tmp-1, prob*a, li+[[li[-1][0] + 1, li[-1][1]]])
    if [li[-1][0] - 1 , li[-1][1]] not in li and b > 0:
        func(n_tmp-1, prob*b, li+[[li[-1][0] - 1 , li[-1][1]]])
    if [li[-1][0] , li[-1][1] + 1] not in li and c > 0:
        func(n_tmp-1, prob*c, li+[[li[-1][0] , li[-1][1] + 1]])
    if [li[-1][0] , li[-1][1] - 1] not in li and d > 0:
        func(n_tmp-1, prob*d, li+[[li[-1][0] , li[-1][1] - 1]])

    return

func(n, 1, [[0,0]])
print(ans)