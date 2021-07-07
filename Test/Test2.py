import sys
N = int(sys.stdin.readline())
X = list(map(int, sys.stdin.readline().split()))
X = sorted(X, reverse=True)
def solve():
    for i in range(N):
        for j in range(i+1, N):
            for k in range(j+1, N):
                if X[i] < X[j] + X[k]:
                    return X[i] + X[j] + X[k]
    else:
        return -1
print(solve())