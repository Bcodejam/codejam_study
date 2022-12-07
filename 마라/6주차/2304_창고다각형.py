N = int(input())

lst = []
for _ in range(N) :
    lst.append(list(map(int, input().split())))

lst.sort(key=lambda x : x[0])
#가장 큰 박스의 왼쪽 , 오른쪽 좌표 구하기
left = lst[0][0]
right = lst[N-1][0]

lst.sort(key=lambda x : -x[1])
#가장 긴 애 길이
tall = lst[0][1]

#가장 큰 박스 넓이
width = (right - left +1) * lst[0][1]

#왼쪽 기준, 오른쪽 기준 위치
left_std = lst[0][0]
right_std =lst[0][0]

for L , H in lst:
    #기준 사이에 있으면 넘어감
    if L >= left_std and L <= right_std :
        continue
    #기준 밖에 있으면 넓이 감소
    else :
        if L < left_std:
            width -= (left_std - L) * (tall - H)
            
            left_std = L
        if L > right_std :
            width -= ( L - right_std) * (tall - H)
         
            right_std = L
print(width)