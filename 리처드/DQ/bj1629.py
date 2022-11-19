import sys

input = sys.stdin.readline

a,b,c = map(int, input().rstrip().split())

def func(a,b):
    if b == 2: return (a*a) % c
    if b == 1: return a % c
    if b % 2 == 1:
        return func((a*a)%c, b//2) * a%c
    else:
        return func((a*a)%c, b//2)
print(func(a,b))