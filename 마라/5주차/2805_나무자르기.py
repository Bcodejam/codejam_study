N, M = map(int, input().split())
lst = []
lst = list(map(int, input().split()))

#height 길이만큼 자를 때 상근이가 가져갈 길이 계산
def countLength(height) :
  sum = 0
  for i in lst :
    sum += max(i - height , 0)
  return sum


#최적의 절단기 높이 찾기, 이분탐색
low = 0
high = max(lst)


while (low <= high) :
  mid = (low + high) //2 
  if countLength(mid) >= M :
    low = mid + 1
  else :
    high = mid -1

print(high)