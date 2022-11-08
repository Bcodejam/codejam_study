import sys

input = sys.stdin.readline

list_n = [1,1,2,2,2,8]
list_tmp = list(map(int, input().rstrip().split()))

for i in range(len(list_n)):
    print(list_n[i] - list_tmp[i], end=' ')