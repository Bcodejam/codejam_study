import sys


def make_quad_tree(x, y, size):
    if size == 1:
        return arr[x][y]

    next_size = size // 2

    # 좌상단, 우상단, 좌하단, 우하단 순서
    lt = make_quad_tree(x, y, next_size)
    rt = make_quad_tree(x, y + next_size, next_size)
    lb = make_quad_tree(x + next_size, y, next_size)
    rb = make_quad_tree(x + next_size, y + next_size, next_size)

    if lt == rt == lb == rb and (lt == '0' or lt == '1'):
        # 압축 가능 -> 압축해서 리턴
        # print(lt)
        return lt
    else:
        # 압축 불가능 -> 4개 다 출력 + 괄호로 묶음
        # print(lt + rt + lb + rb)
        return "(" + lt + rt + lb + rb + ")"


n = int(sys.stdin.readline().rstrip())
arr = []
for _ in range(n):
    arr.append(list(sys.stdin.readline().rstrip()))

print(make_quad_tree(0, 0, n))
