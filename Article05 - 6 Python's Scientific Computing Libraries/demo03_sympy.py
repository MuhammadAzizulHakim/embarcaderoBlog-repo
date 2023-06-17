from sympy import *
 
x, t, z, nu = symbols('x t z nu')
init_printing(use_unicode=True)
 
# Solve differential
print(diff(sin(x)*exp(x), x))
 
# Solve indefinite integral
print(integrate(exp(x)*sin(x) + exp(x)*cos(x), x))
 
# Solve definite integral
print(integrate(sin(x**2), (x, -oo, oo)))
 
# Solve limit
print(limit(sin(x)/x, x, 0))
 
# Solve quadratic equation
print(solve(x**2 - 2, x))
 
# Solve differential equation
y = Function('y')
print(dsolve(Eq(y(t).diff(t, t) - y(t), exp(t)), y(t)))