# SageMath cross-check for the Macdonald lattice Schur-convexity counterexample.
#
# Independent of verify.py rather than a transcription of it: the rank-two
# Macdonald polynomials here come out of Sage's own Macdonald P basis, while
# verify.py recovers them from the (q,t) Hall inner product by hand.  The two
# agree only if the coefficient A is right, which is the one quantity the whole
# reversal turns on.
#
# Exact throughout -- QQ and the fraction field QQ(q,t), never floating point.
# Every claim is asserted: tools/verify_all.py reads the exit status, so a
# printed value that no assert covers proves nothing.

Sym = SymmetricFunctions(QQ['q','t'].fraction_field())
K = Sym.base_ring()
q, t = K.gens()
P, m = Sym.macdonald().P(), Sym.monomial()

# ---- the rank-two Macdonald polynomials, from Sage's basis ------------------
# P_(2,0) = m_(2) + A m_(1,1) and P_(1,1) = e_2 = m_(1,1).
A = m(P[2]).coefficient([1, 1])
assert A == (1 + q) * (1 - t) / (1 - q*t)
assert A.subs(t=q) == 1                 # q=t: P_(2,0) degenerates to Schur s_(2)
assert m(P[1,1]) == m[1,1]
print("A            =", factor(A))

p20 = P[2].expand(2, alphabet=['x1','x2'])
p11 = P[1,1].expand(2, alphabet=['x1','x2'])
x1, x2 = p20.parent().gens()
assert p20 == x1^2 + x2^2 + A*x1*x2
assert p11 == x1*x2

# Omega_lambda(x) = P_lambda(x) / P_lambda(t^delta), with t^delta = (t, 1).
# Both evaluations land in QQ(q,t), so coerce out of the x-ring: what is left
# has to be substitutable in q and t below.
def omega(p, a, b):
    return K(p.subs({x1: a, x2: b})) / K(p.subs({x1: t, x2: 1}))

# ---- the reversal as an identity in q and t --------------------------------
O20, O11 = omega(p20, 1, 1), omega(p11, 1, 1)
assert O11 == 1/t
gap = O11 - O20
assert gap == (1 - t)^2 * (1 - q*t) / (t * (1 + t) * (1 - q*t^2))
print("gap          =", factor(gap))
# Each factor of that quotient is strictly positive on 0<q,t<1, so the gap is:
# Omega_(1,1) > Omega_(2,0) although (2,0) dominates (1,1).  The denominator's
# factorization is what makes the signs visible one factor at a time.
assert (1 + t^2 + A*t) == (1 + t) * (1 - q*t^2) / (1 - q*t)

# ---- exact rational instances on the lattice t = q^k ------------------------
# 1^n lies on L_n^{q,t,a} exactly when t = q^k, so these are admissible points.
for (qv, k) in [(QQ(1)/2, 1), (QQ(1)/2, 2), (QQ(2)/3, 3), (QQ(9)/10, 1)]:
    tv = qv^k
    g = gap.subs(q=qv, t=tv)
    assert g > 0
    assert O20.subs(q=qv, t=tv) < O11.subs(q=qv, t=tv)

# The Schur subcase q=t=1/2, which is the reversal carried in the paper's body.
r = QQ(1)/2
assert O20.subs(q=r, t=r) == QQ(12)/7
assert O11.subs(q=r, t=r) == 2
assert gap.subs(q=r, t=r) == QQ(2)/7
# ... and the identity 1+r+r^2-3r = (1-r)^2 behind the whole 0<r<1 family.
rr = polygen(QQ, 'rr')
assert 1 + rr + rr^2 - 3*rr == (1 - rr)^2
print("q=t=1/2      :", O20.subs(q=r, t=r), "<", O11.subs(q=r, t=r))

# A non-Schur lattice point, t = q^2, where P_(2,0) is not a Schur polynomial.
qv, tv = QQ(1)/2, QQ(1)/4
assert A.subs(q=qv, t=tv) == QQ(9)/7
assert O20.subs(q=qv, t=tv) == QQ(368)/155
assert O11.subs(q=qv, t=tv) == 4
assert gap.subs(q=qv, t=tv) == QQ(252)/155
print("q=1/2,t=1/4  :", O20.subs(q=qv, t=tv), "<", O11.subs(q=qv, t=tv))

# ---- where it comes from: the determinant shift is not free for Omega ------
# P_lambda(y) = (y_1...y_N)^c P_{lambda-c(1^N)}(y), but evaluating at t^delta
# picks up prod_i t^{N-i} = t^{N(N-1)/2} per unit of c, so Omega carries a
# t-power the naive shift omits.  At N=2, lambda=(1,1), c=1 that power is t.
N = 2
assert sum(N - i for i in range(1, N + 1)) == N*(N - 1)/2
y1, y2 = polygens(Sym.base_ring(), 'y1,y2')
omega_11_actual = y1*y2/t                      # = P_(1,1)(y) / P_(1,1)(t,1)
omega_11_shift = (y1*y2 / t^(N*(N-1)/2)) * 1   # correct shift, Omega_(0,0) = 1
omega_11_naive = y1*y2                         # shift with the t-power dropped
assert omega_11_actual == omega_11_shift
discrepancy = omega_11_actual - omega_11_naive
assert discrepancy == (1 - t)*y1*y2/t
# t lives in the coefficients here, not among the y generators, so setting it
# to 1 is a map on coefficients.  The two shifts agree there and nowhere else.
assert discrepancy.map_coefficients(lambda c: c.subs(t=1)) == 0

# ---- scope: the 1^n-normalized ratio satisfies what Omega violates ----------
# W_lambda(x) = P_lambda(x)/P_lambda(1^n).  Its gap has the opposite sign, so
# what is refuted is a claim about the principal-specialization normalization
# and not about the Macdonald polynomials themselves.
W20 = p20 / p20.subs({x1: 1, x2: 1})
W11 = p11 / p11.subs({x1: 1, x2: 1})
assert W20 - W11 == (x1 - x2)^2 / (2 + A)
print("W20 - W11    =", (x1 - x2)^2 / (2 + A), ">= 0")
