import sys

input = sys.stdin.readline

def chk(a, b, st, ba):
    
    a_1 = a//100
    a_2 = (a%100)//10
    a_3 = a%10

    b_1 = b//100
    b_2 = (b%100)//10
    b_3 = b%10
    
    s_tmp = 0
    b_tmp = 0

    if a_1 == b_1: s_tmp += 1
    if a_2 == b_2: s_tmp += 1
    if a_3 == b_3: s_tmp += 1

    if a_1 == b_2 or a_1 == b_3: b_tmp += 1
    if a_2 == b_1 or a_2 == b_3: b_tmp += 1
    if a_3 == b_1 or a_3 == b_2: b_tmp += 1

    if s_tmp == st and b_tmp == ba: 
        return True
    else: return False

n = int(input())
queue = []

for i in range(1,10):
    for j in range(1,10):
        for k in range(1,10):
            if i != j and i != k and j != k:
                queue.append(i*100+j*10+k)

for i in range(n):
    num, s, b = map(int, input().rstrip().split())
    lq = len(queue)
    for j in range(lq):
        a_tmp = queue.pop(0)
        if chk(a_tmp, num, s, b): 
            queue.append(a_tmp)

print(len(queue))