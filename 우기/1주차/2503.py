import sys
from itertools import combinations, permutations

STRIKE = 0
BALL = 1


# 몇 스트라이크, 몇 볼인지 체크하는 함수
def check(answer, guess):
    ret = [0, 0]

    for g_idx in range(3):
        flag = 2
        for a_idx in range(3):
            if answer[a_idx] == guess[g_idx]:
                flag = min(flag, BALL)
                if a_idx == g_idx:
                    flag = min(flag, STRIKE)

        if flag < 2:
            ret[flag] += 1

    return ret


ans = 0
n = int(sys.stdin.readline().rstrip())
q = [list(sys.stdin.readline().rstrip().split()) for _ in range(n)]

# 완전탐색
# 1~9 까지 3개 조합으로 뽑고 -> 모든 순열 나열
for c in combinations(range(1, 10), 3):
    for p in permutations(c):
        num = ""
        for v in p:
            num += str(v)

        can_answer = True

        for g_num, s, b in q:
            result = check(num, g_num)
            if result != [int(s), int(b)]:
                can_answer = False
                break

        if can_answer:
            ans += 1

print(ans)


