import sys
from collections import deque


def main():
    read = sys.stdin.readline
    for _ in range(int(read())):
        n = int(read())
        picks = [int(x) - 1 for x in read().split()]
        print(solve(n, picks))


def solve(n, picks):
    counts = [0] * n

    for pick in picks:
        counts[pick] += 1

    remove_candidates = deque(person for person, count in enumerate(counts) if count == 0)
    # print(remove_candidates)

    # 순환이 없는 애들을 다 제거
    # 친구 없는 애들 부터 시작
    # 친구 없는 애들이 지목한 애들 체크 -> 걔네 빼고 지목한 애들이 있는지 다시 체크
    while remove_candidates:
        # print(remove_candidates, counts)
        removed = remove_candidates.popleft()
        candidate = picks[removed]
        counts[candidate] -= 1
        if not counts[candidate]:
            remove_candidates.append(candidate)
    # print(remove_candidates, counts)
    return n - sum(counts)


if __name__ == "__main__":
    sys.exit(main())