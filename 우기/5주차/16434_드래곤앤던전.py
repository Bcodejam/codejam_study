# coding=utf-8
import sys
import math


def play(max_h):
    curr_h = max_h
    curr_atk = h_atk

    for room in dungeon:
        _t, _a, _h = room

        if _t == 1:
            # 공격 횟수 = _h / curr_atk
            # 먼저 떄리니까 맞은 횟수 = 공격횟수 - 1
            curr_h -= (math.ceil(_h / curr_atk) - 1) * _a
            if curr_h <= 0:
                return -1

        if _t == 2:
            curr_atk += _a
            curr_h += _h
            curr_h = min(max_h, curr_h)

    return curr_h


ans = 0
n, h_atk = map(int, sys.stdin.readline().rstrip().split())
dungeon = []
for _ in range(n):
    t, a, h = map(int, sys.stdin.readline().rstrip().split())
    dungeon.append((t, a, h))

low = 0
# 123456 * 100만 * 100만 => 1.23456e+17
high = int(1e18)
mid = 0

while low <= high:
    mid = (low + high) // 2
    result = play(mid)

    # 성공
    if result > 0:
        high = mid - 1
        ans = mid
    # 실패
    else:
        low = mid + 1

print(ans)
