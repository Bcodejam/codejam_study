# coding=utf-8
import sys
from collections import deque

ans = 0
n, k = map(int, sys.stdin.readline().rstrip().split())
names = []
for _ in range(n):
    names.append(sys.stdin.readline().rstrip())

idx = 0
len_count = {}
q = deque()


# 큐에 새로운 학생 추가
def enqueue():
    global len_count, q, idx
    curr_student = names[idx]
    curr_name_len = len(curr_student)

    q.append(curr_student)
    idx += 1

    if curr_name_len in len_count:
        len_count[curr_name_len] += 1
    else:
        len_count[curr_name_len] = 1


# 큐에서 맨 앞의 학생 제거
def dequeue():
    global len_count, q, idx
    curr_student = q[0]
    curr_name_len = len(curr_student)

    q.popleft()
    len_count[curr_name_len] -= 1

    return curr_student


enqueue()

while q:
    # 만약 큐에 넣을 학생이 있다면
    if idx < len(names):
        # k 범위 넘어가면 앞에서 부터 뻄
        if len(q) > k:
            curr = dequeue()
            # print(curr, q)
            ans += len_count[len(curr)]

        # 새 학생 추가
        enqueue()

    # 큐에 넣을 애들이 더 없으면
    else:
        curr = dequeue()
        # print(curr, q)
        ans += len_count[len(curr)]

print(ans)
