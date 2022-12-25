import sys

input = sys.stdin.readline

n = int(input().rstrip())

for _ in range(n):
    s = input().rstrip()
    num = int(input().rstrip())
    list_n = list(input().rstrip().split(','))
    list_n[0] = list_n[0][1:]
    list_n[-1] = list_n[-1][:-1]
    # f => front , b => back
    f = 0
    b = 0
    chk = -1
    for i in s:
        if i == 'R':
            chk *= -1
        else:
            if chk == -1:
                f += 1
            else:
                b += 1
    if f+b > num:
        print("error")
    elif f+b == num:
        print("[]")
    else:
        if chk == 1:
            list_n = list_n[f:num-b][::-1]
        else:
            list_n = list_n[f:num-b]
        print('[',end='')
        for j in list_n[:-1]:
            print(j,end=',')
        print(list_n[-1],end='')
        print(']')