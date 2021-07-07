a, b, c = map(int, input().split())
D = b**2 - 4*a*c
if D > 0:
    d = (-b + int(D**0.5))//2*a
    e = (-b - int(D**0.5))//2*a
    if d < e:
        d, e = e, d
    print("Two different roots x1=%i , x2=%i" %(d, e))
elif D == 0:
   print("Two same roots x=%i"%(-b//(2*a)))
elif D < 0:
    print("No real root")

