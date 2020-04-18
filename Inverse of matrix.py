def Inverse(a,m):
    m0 = m
    t1 = 0
    t2 = 1

    while (m != 0):
        # quotient
        q = a // m
        t = m
        # switch m=r
        m = a % m
        a = t
        t = t1
        t1 = t2 - q * t1
        t2 = t

        # positive
    if (t2 < 0):
        t2 = t2 + m0

    return t2

a = 12
m = 23
print("multiplicative inverse is",
      Inverse(a, m))