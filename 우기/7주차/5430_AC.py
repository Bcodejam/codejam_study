import sys

T = int(sys.stdin.readline().rstrip())
for test_case in range(T):
    commands = list(sys.stdin.readline().rstrip())
    n = int(sys.stdin.readline().rstrip())
    arr = []
    if n != 0:
        arr = list(map(int, sys.stdin.readline().rstrip()[1:-1].split(',')))
    else:
        sys.stdin.readline()

    cursor = [0, n - 1]
    state = 0
    error = False
    for cmd in commands:
        if cmd == 'D':
            if cursor[0] > cursor[1]:
                error = True
                break
            cursor[state] += (1 + (-2)*state)

        if cmd == 'R':
            state = 1 - state

    arr = arr[cursor[0]:cursor[1] + 1]
    if state:
        arr.reverse()

    print('error' if error else str(arr).replace(' ', ''))
