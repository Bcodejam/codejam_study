import sys

input = sys.stdin.readline

l,w,h = map(int, input().rstrip().split())

ans = 0

def func(x,y,z):
    for i in range(19,-1,-1):
        if (li[i] > 0) and ((x+(2**i)) <= h) and ((y+(2**i)) <= w) and ((z+(2**i)) <= l):
            for j in range(x, x+(2**i)):
                for k in range(y, y+(2**i)):
                    for m in range(z, z+(2**i)):
                        print(j,k,m)
                        box[j][k][m] = 1
            li[i] -= 1
            return 1
    return -1

# h w l
box = [[[0 for _ in range(l)] for _ in range(w)] for _ in range(h)]

li = [0]*20

n = int(input().rstrip())

for i in range(n):
    a,b = map(int, input().rstrip().split())
    li[19-a] = b

print(li)

chk = True
for i in range(l):
    for j in range(w):
        for k in range(h):
            if box[k][j][i]==0:
                ans += func(k,j,i)

print(box)

for i in range(l):
    for j in range(w):
        for k in range(h):
            if box[k][j][i] == 0:
                chk = False

if not chk: print(-1)
else: print(ans)