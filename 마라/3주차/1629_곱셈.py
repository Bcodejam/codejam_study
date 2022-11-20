
###############시간초과 코드#########
# def f(b) :

#   if b == 1 :
#     return A

#   if b % 2 == 0 :
#     return f(b//2) * f(b//2) 

#   if b % 2 == 1:
#     return f(b//2) * f(b//2) * A


# print(f(B) % C)


#################시간초과 코드 2###################
# def f(b) :
  
#   if b == 1 :
#     return A % C
#   if b % 2 == 0 :
#     return f(b//2) * f(b//2) % C

#   else :
#     return f(b//2) * f(b//2) * A % C

# print(f(B))


import sys
input = sys.stdin.readline
A, B ,C = map(int, input().split())

def f(b) :
  
  if b == 1 :
    return A % C
  tmp = f(b//2)
  if b % 2 == 0 :
    return tmp * tmp % C

  else :
    return tmp * tmp * A % C

print(f(B))
