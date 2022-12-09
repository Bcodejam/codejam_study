
stack = []

#string이 legal 한지 계산하는함수
def isLegal(string) :  
  for i in range(len(string)) :
    if string[i] == '<' :
      for j in range(i + 1 , len(string)) :
        if string[j] == '>' :
          #스택에 넣고, 규칙에 위배되면 바로 False를 return하여 illegal 출력
          if not stacking(string[i+1 : j]) :
            return False
          else :
            break
  #스택에 남아있는경우 요소가 닫히지 않았단 뜻이므로 illegal 출력
  if len(stack) != 0:
    return False
  return True
         
              
#stack에 요소(ex)</string> 를 넣는 함수 
def stacking(item) :
  if item[0] == "a":
    stack.append(item[0])
    return True
  if item =="br /" :
    return True
  if len(stack) == 0:
    stack.append(item)
    return True
  top = stack[-1]
  if "/" + top == item :
    stack.pop()
    return True
  stack.append(item)
  return True
  

while True:
  line = input()
  stack = []
  if line == "#" :
    break
  if isLegal(line) :
    print("legal")
  else :
    print("illegal")