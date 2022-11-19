import sys

input = sys.stdin.readline

list_n = list(map(int, input().rstrip().split()))
p,m = 0,0
for i in range(len(list_n)-1):
    val = list_n[i+1] - list_n[i]
    if(val < 0): m += 1
    elif(val > 0): p += 1

if p == 7: print("ascending")
elif m == 7: print("descending")
else: print("mixed")