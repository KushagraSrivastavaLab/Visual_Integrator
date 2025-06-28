import matplotlib.pyplot as plt
import numpy
import sympy

x = sympy.symbols('x')
f_raw = input('Please enter an equation in one variable ')
print('please enter the limits to integrate ')
a = int(input('from '))
b = int(input('to '))

f = sympy.lambdify(x, f_raw, modules=['numpy'])

x_vals = numpy.linspace(-20, 20, 500)
y_vals = f(x_vals)

mask = (x_vals >= a) & (x_vals <= b)
x_selected = x_vals[mask]
y_selected = f(x_selected)
area = numpy.trapezoid(y_selected, x_selected)

plt.figure(figsize=(10, 6), dpi=100)
plt.plot(x_vals, y_vals, label='f(x)', color='darkblue')
plt.fill_between(x_selected, y_selected, color='skyblue', alpha=0.4, label=f'Area = {area:.2f}')
plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)
plt.axvline(a, color='red', linestyle='--', linewidth=1)
plt.axvline(b, color='red', linestyle='--', linewidth=1)


plt.text(4.5, max(y_selected)*0.5, f"Area = {area:.2f}", fontsize=12, bbox=dict(facecolor='white', edgecolor='blue', boxstyle='round,pad=0.5'))

plt.title(f"Area Under Curve from x = {a} to x = {b}", fontsize=16, fontweight='bold')
plt.xlabel("x", fontsize=14)
plt.ylabel("f(x)", fontsize=14)
plt.grid(True, linestyle='--', alpha=0.6)
plt.legend(loc='upper right', fontsize=12)
plt.tight_layout()
plt.show()

print("Area under curve from x = 3 to x = 7:", area)
