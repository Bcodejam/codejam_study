from itertools import combinations

N, S = map(int, input().split())
answer = 0
lst = list(map(int, input().split()))

for i in range(1 , len(lst) + 1):
    #dividedList = lst 에서 길이 i 인 부분집합 tuple
    dividedList = combinations(lst, i)
    for j in dividedList : # 튜플 하나씩 꺼내서
        if sum(j) == S : # 더해보고 S랑 같으면 count
            answer += 1 

print(answer)