import matplotlib.pyplot as plt
import numpy as np 
import sympy as sp

x = np.linspace(-5,5,100) 
y = x**2

plt.plot(x,y)
plt.show()

#Expanding the algebraic expression
x = sp.symbols('x')
expr = (x+1)**3
expr1 = sp.expand(expr)
print(sp.latex(expr1))