# coding=utf-8
import sys


# 현재 계획에 새 과제를 추가
def add(plan, d, w):
    # 현재 마감일까지의 값들 중 최소값이
    # 현재 과제 점수보다 낮으면 교체
    min_idx = plan[:d].index(min(plan[:d]))

    # print(plan[:d], w, min_idx)

    if plan[min_idx] < w:
        plan[min_idx] = w


def main():
    n = int(sys.stdin.readline().rstrip())
    arr = []

    for _ in range(n):
        d, w = map(int, sys.stdin.readline().rstrip().split())
        arr.append((d, w))

    # 마감일 오름차순, 점수 내림차순 정렬
    arr.sort(key=lambda x: (x[0], -x[1]))

    plan = [0] * 1001
    for d, w in arr:
        add(plan, d, w)

    print(sum(plan))


main()
