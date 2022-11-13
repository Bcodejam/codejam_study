length, width, height = map(int, input().split())
n = int(input())
cube = [list(map(int, input().split())) for _ in range(n)]
#전체 넓이
volume = length * width * height
ans = 0
before = 0
cube.sort(reverse=True)

for w, cnt in cube:
    # 같은 공간에 들어갈 수 있는 큐브의 갯수는
    # 8배씩 늘어 난다(ex ) 2x2x2 공간에 2x2x2 큐브는 1개 , 1x1x1 큐브는 8개 들어감)
    before *= 8
    # w = 0 이면 1x1x1큐브 , w = 1 이면 2x2x2큐브이므로
    v = 2 ** w
    # VxVxV 크기의 큐브가 최대로 얼마나 들어갈수 있는지 구하고
    # (V-1)x(V-1)x(V-1)크기의 큐브가 차지했던 부피를 VxVxV 큐브의 갯수로 변환하여 빼준다.
    maxCnt = (length // v) * (width // v) * (height // v) - before
    # 큐브 최대 갯수와 가지고있는 큐브의 갯수중 작은것을 선택한다.
    # (큐브를 최대 10개 넣을 수 있다해도 8개밖에 없으면 8개만 넣을 수 있기 때문) 
    maxCnt = min(cnt, maxCnt)
    ans += maxCnt
    before += maxCnt

if before == volume:
    print(ans)
else:
    print(-1)