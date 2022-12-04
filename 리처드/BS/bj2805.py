import sys

input = sys.stdin.readline

n, m = map(int, input().rstrip().split())

list_n = list(map(int, input().rstrip().split()))

list_n.sort(reverse=True)

# 현재 값
cur_h = list_n[0]
# 비교 값
ans = 0
# 몇개의 나무를 자르고 있는지 확인
tot_l = 0

while True:
    if ans >= m:
        break
    if tot_l != n:
        for i in range(tot_l, n):
            if list_n[i] == cur_h:
                tot_l += 1
            else:
                break
        cur_h -= 1
    else:
        cur_h -= 1
    ans += tot_l

print(cur_h)
