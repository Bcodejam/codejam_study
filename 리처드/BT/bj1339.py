import sys
from collections import defaultdict

input = sys.stdin.readline

n = int(input().rstrip())

dict_word_list = defaultdict(int)

for _ in range(n):
    s = input().rstrip()
    point = 10 ** (len(s)-1)
    for i in s:
        dict_word_list[i] += int(point)
        point /= 10

list_ans = []
for i in dict_word_list:
    # print(i)
    # print(dict_word_list[i])
    list_ans.append(dict_word_list[i])

list_ans.sort(reverse=True)
ans = 0
mult = 9
for i in list_ans:
    ans += (i*mult)
    mult -= 1
print(ans)