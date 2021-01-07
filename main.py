# Calculus
import sympy as sp # library for differentiation and integration

x = sp.Symbol('x') # declare variable for functions

# POWER RULE
# f(x) = 3x^4 + x^3 + 2x^2 + 10
print(sp.diff(3*x**4+x**3+2*x**2+10)) # derivative of 3x^4+x^3+2x^2+10 = 12x^3 + 3x^2 + 4x
# f(x) = x^9
print(sp.diff(x**9,x,x)) # 2nd derivative of x^9 = 72x^7 (1st derivative = 9x^8)

# f(x) = cos(x) x (3x^2+1) PRODUCT RULE
print(sp.diff(sp.cos(x)*(3*x**2+1))) # -6xcos(x)+(3x^2+1)sin(x)

# f(x) = tan(x)/x QUOTIENT RULE
print(sp.diff((sp.tan(x))/x)) # tan^2(x)+1 = sec^2(x)

# f(x) = (x^3+10)*8 # CHAIN RULE
print(sp.diff((x**3+10)**8)) # 24x^2(x^3+10)^7

# Exponential Derivatives f(x) = 4e^4x
print(sp.diff(sp.exp(4*x)))