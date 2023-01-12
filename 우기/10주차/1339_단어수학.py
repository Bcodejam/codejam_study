import sys

ans = 0
n = int(sys.stdin.readline().rstrip())
ch = {}

for _ in range(n):
    word = list(sys.stdin.readline().rstrip())
    for i in range(len(word)):
        if word[i] not in ch:
            ch[word[i]] = 0
        ch[word[i]] += (10 ** (len(word) - i - 1))
        # print(word[i], (10 ** (len(word) - i - 1)))

weights = sorted(ch.values(), reverse=True)
for i in range(len(weights)):
    ans += (weights[i] * (9 - i))

print(ans)

