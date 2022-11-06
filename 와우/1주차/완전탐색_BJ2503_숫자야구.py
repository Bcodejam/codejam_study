import sys
from itertools import permutations

n=int(input())
num=list(permutations(range(10), 3))

for _ in range(n):
    q, s, b = map(int, input().split())
    q=list(str(q))
    remove_cnt=0
    
    for i in range(len(num)):
        s_cnt = b_cnt =0
        i-=remove_cnt
        for j in range(3):
            q[j]=int(q[j])
            if q[j] in num[i]:
                if j==num[i].index(q[j]):
                    s_cnt+=1
                else:
                    b_cnt+=1
        if not(s==s_cnt and b==b_cnt):
            num.remove(num[i])
            remove_cnt+=1
            
print(len(num))