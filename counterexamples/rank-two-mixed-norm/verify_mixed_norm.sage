# SageMath outward-rounded certificate for the rank-two mixed-norm ratio.
R = RealIntervalField(250)
mult = [1,18,1,1]
weights = [46,17,42,1]
dirs = [(R(1),R(0)),(R(1),R(1)/50),(R(1),R(3)/50),(R(0),R(1))]
rows=[]
for m,w,y in zip(mult,weights,dirs):
    scale = R(w)^(R(5)/6)
    rows += [(scale*y[0],scale*y[1])]*m
A = matrix(R, 21, 21, lambda i,j: rows[i][0]*rows[j][0]+rows[i][1]*rows[j][1])

def npq(p,q):
    return sum((sum(abs(A[i,j])^p for i in range(21)))^(q/p) for j in range(21))^(1/q)
s=R(6)/5; q=R(6)
ratio=npq(s,q)/(npq(s,s)*npq(q,q)).sqrt()
print(ratio)
assert ratio.lower()>1
