# coding=utf-8
import sys
sys.setrecursionlimit(10 ** 5)


def dfs(arr, idx):
    global grouped, visited, path
    # 현재 노드를 방문한적이 없으면 -> 방문체크하고 다음 노드로
    if not visited[idx]:
        visited[idx] = True
        next_idx = arr[idx]

        # 지나온 노드들을 기록
        path.append(dfs(arr, next_idx))

        # 순환을 찾았으면 그룹으로 기록
        if idx == path[0]:
            grouped += path
            # print(idx, path)

    return idx


read = sys.stdin.readline
tc = int(read().rstrip())

grouped = []
visited = []
path = []

for _ in range(tc):
    n = int(read().rstrip())
    grouped = []
    visited = [False] * n
    student = [x - 1 for x in list(map(int, read().rstrip().split()))]

    for i in range(n):
        path = []
        dfs(student, i)

    print(n - len(grouped))

