import sys

CH = ["W", "B"]
W = 0
B = 1


# 체스 한줄 만드는 함수
def make_line(first_ch_idx, length):
    idx = first_ch_idx
    ret = [CH[idx]]

    for _ in range(length - 1):
        idx = (idx + 1) % 2
        ret.append(CH[idx])

    return ret


# 체스판 만드는 함수
def make_chess_board(first_ch_idx, _n, _m):
    chess_board = []
    for _ in range(_n):
        chess_board.append(make_line(first_ch_idx, _m))
        first_ch_idx = (first_ch_idx + 1) % 2

    return chess_board


ans = 9876543210
n, m = map(int, sys.stdin.readline().rstrip().split())
board = [list(sys.stdin.readline().rstrip()) for _ in range(n)]

correct_board = [
    make_chess_board(W, 8, 8),
    make_chess_board(B, 8, 8)
]

# 완전 탐색
for board_num in range(2):
    for offset_i in range(n - 8 + 1):
        for offset_j in range(m - 8 + 1):
            tmp_ans = 0
            for i in range(8):
                for j in range(8):
                    if board[i + offset_i][j + offset_j] != correct_board[board_num][i][j]:
                        tmp_ans += 1

            ans = min(ans, tmp_ans)

print(ans)
