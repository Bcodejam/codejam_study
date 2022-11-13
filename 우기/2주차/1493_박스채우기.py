# coding=utf-8
import sys

l, w, h = map(int, sys.stdin.readline().rstrip().split())
n = int(sys.stdin.readline().rstrip())

boxes = []
for _ in range(n):
    a, b = map(int, sys.stdin.readline().rstrip().split())
    # 부피, 변 길이, 개수 저장
    boxes.append(((2 ** a) ** 3, 2 ** a, b))

boxes.reverse()

total = l * w * h
cnt = 0
curr_total = 0

for v, a, num in boxes:
    curr_total *= 8
    
    # 현재 공간에 채울 수 있는 개수 - 지금까지 채운 개수
    max_num = (l // a) * (w // a) * (h // a) - curr_total

    # 쓸 수 있는 개수, 추가로 채울 수 있는 개수 중 작은값
    use = min(num, max_num)
    cnt += use
    curr_total += use

if total == curr_total:
    print(cnt)
else:
    print(-1)


