#X1 = int(input())
#X2 = int(input())
#X3 = int(input())
X1, X2, X3 = map(int, input().split())
#X1, X2, X3 = (int(input()) for _ in range(3))
listX = [X1, X2, X3]
listX.sort()
if listX[0] + listX[1] > listX[2]:
  print (True)
else:
  print (False)
