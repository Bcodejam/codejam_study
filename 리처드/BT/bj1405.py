import sys

input = sys.stdin.readline

n, a, b, c, d = map(int, input().rstrip().split())


a /= 100
b /= 100
c /= 100
d /= 100

ans = 0
li = [[0,0]]

def func(n_tmp, prob):
    global ans
    if n_tmp == 0:
        ans += prob
        return
    if [li[-1][0] + 1, li[-1][1]] not in li and a > 0:
        li.append([li[-1][0] + 1, li[-1][1]])
        func(n_tmp-1, prob*a)
        li.pop()
    if [li[-1][0] - 1 , li[-1][1]] not in li and b > 0:
        li.append([li[-1][0] - 1 , li[-1][1]])
        func(n_tmp-1, prob*b)
        li.pop()
    if [li[-1][0] , li[-1][1] + 1] not in li and c > 0:
        li.append([li[-1][0] , li[-1][1] + 1])
        func(n_tmp-1, prob*c)
        li.pop()
    if [li[-1][0] , li[-1][1] - 1] not in li and d > 0:
        li.append([li[-1][0] , li[-1][1] - 1])
        func(n_tmp-1, prob*d)
        li.pop()
    return

func(n, 1)
print(ans)