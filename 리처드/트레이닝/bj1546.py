import sys

input = sys.stdin.readline

n = int(input().rstrip())
list_n = list(map(int, input().rstrip().split()))

max_val = 0
for i in list_n: max_val = max(i, max_val)

sum_total = 0
for i in range(len(list_n)): sum_total += (list_n[i]/max_val) * 100

print(sum_total / len(list_n))