import sys
from collections import defaultdict

input = sys.stdin.readline

n, k = map(int, input().rstrip().split())

list_n = []
for i in range(n):
    list_n.append(len(input().rstrip()))

'''
list_n : 길이 data
'''

dict_n = defaultdict(int)

ans = 0

for i in range(n):
    if i > k: dict_n[list_n[i-k-1]] -= 1
    ans += dict_n[list_n[i]]
    dict_n[list_n[i]] += 1

print(ans)