# SageMath cross-check for the Courtade volume-conjecture counterexample.
#
# Independent of verify.py rather than a transcription of it: verify.py sums
# |det| over generator 4-subsets (Shephard's zonotope formula), while Sage's
# polytopes.zonotope builds each Minkowski sum as an honest H/V-polytope over
# QQ and computes its volume by triangulation.  The two agree only if the
# generator formula was applied correctly, which is what the whole certificate
# rests on.
#
# Exact throughout -- all generators live in QQ^4 and Polyhedron volumes are
# rational.  Every claim is asserted: tools/verify_all.py reads the exit
# status, so a printed value that no assert covers proves nothing.

A_gens = [
    (1, 0, 0, 0),
    (0, 1, 0, 0),
    (0, 0, 1, 0),
    (0, 0, 0, 1),
    (0, 1, -1, 1),
    (1, 0, -1, 1),
    (0, 0, 1, 1),
]
b = (1, -1, 1, 1)
c = (0, 0, -1, 1)


def zvol(gens):
    Z = polytopes.zonotope([vector(QQ, g) for g in gens])
    return Z.volume(measure='induced_rational')


vA = zvol(A_gens)
vAB = zvol(A_gens + [b])
vAC = zvol(A_gens + [c])
vABC = zvol(A_gens + [b, c])

assert vA == 28
assert vAB == 68
assert vAC == 44
assert vABC == 108
# The conjectured inequality, in fourth powers (segments have volume zero):
assert vAB * vAC == 2992
assert vA * vABC == 3024
assert vAB * vAC < vA * vABC
print("zonotope volumes (Sage, triangulation):", vA, vAB, vAC, vABC)
print("Vol(A+B)Vol(A+C) =", vAB * vAC, "<", vA * vABC, "= Vol(A)Vol(A+B+C)")

# Thickened form at eps = 1/100: the same five volumes as verify.py.
eps = QQ(1) / 100
cube = [tuple(eps if i == j else 0 for i in range(4)) for j in range(4)]
B_eps = [b] + cube
C_eps = [c] + cube
assert zvol(B_eps) == QQ(401) / 10^8
assert zvol(C_eps) == QQ(201) / 10^8
vABe = zvol(A_gens + B_eps)
vACe = zvol(A_gens + C_eps)
vABCe = zvol(A_gens + B_eps + C_eps)
assert vABe == QQ(6926731601) / 10^8
assert vACe == QQ(4484551401) / 10^8
assert vABCe == QQ(696978401) / 6250000
assert vABe * vACe < vA * vABCe
assert vA * vABCe - vABe * vACe == QQ(161348459184476999) / 10^16
print("thickened (eps=1/100) still violated; gap =", vA * vABCe - vABe * vACe)
