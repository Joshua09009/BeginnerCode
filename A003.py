M, D = map(int, input().split())
S = M*2 + D 
if S%3==0:
  print("普通")
elif S%3==1:
  print("吉")
else:
  print("大吉")