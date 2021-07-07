#X = [45, 68, 23]
#X = X[::-1]
#print(X[1])
N = int(input())
X = list(map(int, input().split()))
X.sort()
X.reverse()
def solve():
    for i in range(N):
        for j in range(i+1, N):
            for k in range(j+1, N):
                if X[i] < X[j] + X[k]:
                    print (X[i] + X[j] + X[k])
    else:
        print(-1)
#sum = 0               
#for i in range(1000):
 #   if i % 3 == 0 :
  #      sum += i 
        
#print(sum)
#print(int((1002*333/2)))
