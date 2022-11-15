import sys
# 이거 크게 잡으면 메모리 초과남 ㅠㅠ
sys.setrecursionlimit(10 ** 5)


def make_star(size):
    global arr

    # 기본 케이스
    if size == 3:
        arr[0][:3] = arr[2][:3] = ['*', '*', '*']
        arr[1][:3] = ['*', ' ', '*']
        return

    size = size // 3
    # 점점 작은 사이즈로 재귀호출
    make_star(size)

    # 이전 사이즈 크기의 그림을 9개 복사 (가운데 빼고)
    for i in range(3):
        for j in range(3):
            if i == 1 and j == 1:
                continue
            for x in range(size):
                # 슬라이싱한 배열을 재사용해서 메모리 줄임
                arr[x + i * size][(j * size):(j + 1) * size] = arr[x][:size]


n = int(sys.stdin.readline().rstrip())
arr = [[' '] * n for _ in range(n)]

make_star(n)

for arr_row in arr:
    for c in arr_row:
        print(c, end='')
    print()
