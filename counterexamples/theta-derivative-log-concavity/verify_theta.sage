# SageMath outward-rounded certificate for J_9(1/50) < 0.
R = RealIntervalField(250)
t = R(1)/50
uvar = PolynomialRing(ZZ, 'u').gen()
P = [2*uvar - 3]
for k in range(10):
    P.append(4*uvar*P[-1].derivative() + (5-4*uvar)*P[-1])

alpha = R.pi() * (4*t).exp()
def term(k,m):
    u = alpha*m*m
    return R.pi()*m*m*(5*t-u).exp()*P[k](u)

# Sum m=1,...,19. Bound m>=20 by a geometric majorant.
vals = {}
for k in [8,9,10]:
    s = sum(term(k,m) for m in range(1,20))
    Ck = sum(abs(c) for c in P[k].list())
    # For u>=1: |P_k(u)| <= Ck*u^(k+1).
    # Conservative scalar envelope with alpha in [3,4].
    M = 20
    d = 2*k+4
    fM = R.pi().upper() * (5*t).exp().upper() * Ck * R(4)^(k+1) * M^d * (-R(3)*M*M).exp().upper()
    ratio = R((M+1)/M)^d * (-R(3)*(2*M+1)).exp()
    tail = R(0, fM.upper()/(1-ratio.upper()))
    vals[k] = s + R(-tail.upper(), tail.upper())
J = vals[9]^2 - vals[8]*vals[10]
print("Phi8 =", vals[8])
print("Phi9 =", vals[9])
print("Phi10 =", vals[10])
print("J9 =", J)
assert J.upper() < 0
