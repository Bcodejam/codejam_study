import sys

input = sys.stdin.readline

n, atk = map(int, input().rstrip().split())

list_n = []
hp = 0
for _ in range(n):
    list_n.append(list(map(int, input().rstrip().split())))
    if list_n[-1][0] == 1:
        hp += list_n[-1][1] * (list_n[-1][2] // atk)


def calc(hp, atk):
    ret = hp
    tmp_atk = atk
    for i in range(n):
        if list_n[i][0] == 1:
            ret -= list_n[i][1] * ((list_n[i][2] // tmp_atk) - 1)
            if (list_n[i][2] % tmp_atk) != 0:
                ret -= list_n[i][1]
            if ret <= 0:
                return -1
        else:
            ret += list_n[i][2]
            if ret > hp: ret = hp
            tmp_atk += list_n[i][1]
    return ret


left_hp = 0
right_hp = 9000000000000000000
hp = (right_hp + left_hp) // 2

while True:
    if calc(hp, atk) == -1:
        left_hp = hp
        hp = (hp + right_hp) // 2
    else:
        right_hp = hp
        hp = (hp + left_hp) // 2
    if right_hp - left_hp <= 1:
        break
print(right_hp)