import sys
sys.setrecursionlimit(10**7)

input = sys.stdin.readline

n, k = map(int, input().rstrip().split())
list_n = list(map(int, input().rstrip().split()))

list_ans = sorted(list_n)
ans = float("inf")
list_chk = []

def func(list_tmp, cnt):
    global ans
    if list_tmp == list_ans:
        print(ans)
        ans = min(ans, cnt)
        return

    for i in range(0, n-k+1):
        tmp = list_tmp[0:i]+list_tmp[i:i+k][::-1]+list_tmp[i+k:]
        if tmp not in list_chk:
            # print(tmp)
            list_chk.append(tmp)
            func(tmp, cnt + 1)

    return

func(list_n, 0)
print(ans)