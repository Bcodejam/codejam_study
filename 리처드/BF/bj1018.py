from cmath import inf
import sys

input = sys.stdin.readline

n,m = map(int, input().rstrip().split())

chessMap = [[0 for j in range(m)] for i in range(n)]

for i in range(n):
    s = input().rstrip()
    for j in range(m):
        chessMap[i][j] = s[j]

ans = float(inf)
chess1 = []
chess2 = []

for i in range(4):
    chess1.append("WBWBWBWB")
    chess2.append("BWBWBWBW")
    chess1.append("BWBWBWBW")
    chess2.append("WBWBWBWB")

for i in range(n-7):
    for j in range(m-7):
        ans1 = 0
        ans2 = 0
        for k in range(8):
            for l in range(8):
                if chess1[k][l] != chessMap[i+k][j+l]: ans1 += 1
                if chess2[k][l] != chessMap[i+k][j+l]: ans2 += 1
        ans = min(min(ans1, ans2), ans)

print(ans)