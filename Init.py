import math
import random
# This Function Takes an array that contains Coefficients of the Polynomial
def Roots0Func(coef):
    N=len(coef)-1
    P = lambda x: sum(coef*(pow(x, i)) for i, coef in enumerate(coef))
    U = 1 + 1 / abs(coef[-1]) * max(abs(coef[x]) for x in range(N))
    V = abs(coef[0]) / (abs(coef[0]) + max(abs(coef[x]) for x in range(1, N + 1)))
    def Roots0(f):
        roots = []
        for i in range(N):
            r = random.uniform(V, U)
            a = random.uniform(0, math.pi*2)
            root = complex(r * math.cos(a), r * math.sin(a))
            roots.append(root)
        return roots
    R0=Roots0(P)
    return(R0)