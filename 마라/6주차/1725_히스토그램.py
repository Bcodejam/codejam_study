n =int(input())
heights = []
for _ in range(n) :
  heights.append(int(input()))


def maxSize():
    max_size = 0
    stack = []

    for i in range(n):
        left = i
        #Stack 가장 위 값보다 작은 값이 들어올 경우
        while stack and stack[-1][0] >= heights[i]:
            #가장 위 기둥을 pop 하고
            h, left = stack.pop()
            #넓이를 계산해서
            tmp_size = h * (i - left)
            #max size를 계산하여 업데이트한다
            max_size = max(max_size, tmp_size)
        #스택의 위 값보다 큰 값이 들어올경우
        #스택의 높이와 왼쪽 좌표를 스택에 담는다
        stack.append([heights[i],left])

    #스택에 남아있는 값들을 가장 오른쪽 좌표(n) 기준으로 계산
    for h, point in stack:
        max_size = max(max_size, (n-point)*h)

    return max_size
print(maxSize())
