import sys
sys.setrecursionlimit(10 ** 5)


def power(x, n):
    # 1승은 그대로 리턴
    if n == 1:
        return x % c

    # 지수가 짝수면 -> 2로 나눈거 제곱
    if n % 2 == 0:
        return (power(x, n // 2) ** 2) % c

    # 지수가 홀수면 -> 1 빼주고 2로 나눔
    else:
        return (x * (power(x, n // 2) ** 2)) % c


a, b, c = map(int, sys.stdin.readline().rstrip().split())
print(power(a, b))
