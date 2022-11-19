import sys

input = sys.stdin.readline
i = 1
while True:
    l,p,v = map(int, input().rstrip().split())
    if l==0 and p==0 and v==0: break
    ans = 0
    ans += (v//p) * l
    if v%p >= l: ans += l
    else: ans += v%p
    print("Case "+str(i)+": "+str(ans))
    i += 1