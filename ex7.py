from sympy import *
import sympy
from sympy.vector import CoordSys3D

N = CoordSys3D('N')
M  = Matrix([[Rational(1/2), (sympy.sqrt(3))/4, Rational(3/4)],
             [-(sympy.sqrt(3))/4, Rational(7/8), -(sympy.sqrt(3))/8],
             [Rational(-3/4), -(sympy.sqrt(3))/8, Rational(5/8)]])
M = simplify(M)
f = Symbol('f')
x = Symbol('x')
y = Symbol('y')
z = Symbol('z')
u = Matrix([x, y, z])
sob = M * u
V = solve(sob - u, [x, y, z])
u[0] = V[x]
u[1] = V[y]
U = u * u.T
ux = Matrix([[0, -z, y], [z, 0, -x], [-y, x, 0]])
R = cos(f) * eye(3) + sin(f) * ux + (1 - cos(f)) * U
V = solve(Eq(R, M), [x, y, z, f])
u[0] = V[0][0]
u[1] = V[0][1]
u[2] = V[0][2]
f = V[0][3]

print(u, ' | ', f)

k = Symbol("k")
X = u
X *= k
print(simplify(M*X) == X)
print(M * X)
print(X)
solY = solve(u[0]*x + u[1]*y + u[2]*z)
Y = Matrix([x, solY[0][y], z])
print(simplify((M*Y).T*Y) == simplify((Y.T*Y)*cos(f)))