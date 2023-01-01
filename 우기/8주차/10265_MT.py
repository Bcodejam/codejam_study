import sys
from collections import deque


# DFS -> cycle 찾아서 저장
def make_cycle(_arr, idx):
    global cycle, cycles, visited

    # 현재 노드를 방문한적이 없으면 -> 방문체크하고 다음 노드로
    if not visited[idx]:
        visited[idx] = True
        next_idx = _arr[idx]

        # 지나온 노드들을 기록
        cycle.append(make_cycle(_arr, next_idx))

        # 순환을 찾았으면 저장
        if idx == cycle[0]:
            cycles.append(cycle[:])

    return idx


# BFS -> cycle의 각 노드에서 뻗혀있는 노드들 카운트
def count_branch(start, exception):
    cnt = 0
    q = deque([start])

    while q:
        x = q.popleft()
        cnt += 1
        for nx in graph[x]:
            if nx not in exception:
                q.append(nx)

    return cnt - 1


read = sys.stdin.readline
n, k = map(int, read().rstrip().split())
students = [int(x) - 1 for x in read().split()]

cycle = []
cycles = []
visited = [False] * n
for i in range(n):
    cycle = []
    make_cycle(students, i)

# 역방향 그래프 생성
graph = [[] for _ in range(n)]
for u, v in enumerate(students):
    graph[v].append(u)

branches = [0] * n
for c in cycles:
    e = set(c)
    for node in c:
        branches[node] = count_branch(node, e)

print(cycles)
# print(branches)

# 각 순환으로 만들 수 있는 최대값, 최소값 저장
nums = []
for c in cycles:
    min_num, max_num = len(c), len(c)
    for node in c:
        max_num += branches[node]
    nums.append((min_num, max_num))
print(nums)

# 태울 수 있는 최대 학생 수 계산 -> 모르겠음

