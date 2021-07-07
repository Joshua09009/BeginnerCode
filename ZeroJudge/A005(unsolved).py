N = int(input())
X = list(map(int, input().split()))
if X[3] - X[2] == X[2] - X[1]:
    d1 = X[3] - X[2]
    X.append(X[3] + d1)
    print(X)
elif X[3] / X[2] == X[2] / X[1]:
    d2 = X[3] / X[2]
    X.append(int(X[3] * d2))
    print(X)
else:
    print(False)
        
        