import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
import numpy as np

def func(x, a, b, c):
    return a * np.exp(-b * x) + c


points=[(2.1,0.605),(2.94,0.58),(3.36,0.532),(3.53,0.478),(3.85,0.312),(4.4,0.258),(7.2,0.227)]
xdata= np.array([i[0] for i in points])
ydata= np.array([i[1] for i in points])





popt, pcov = curve_fit(func, xdata, ydata)
plt.plot(xdata, ydata, 'b-', label='data')
plt.plot(xdata, func(xdata, *popt), 'r-',label='fit: a=%5.3f, b=%5.3f, c=%5.3f' % tuple(popt))
print(np.sqrt(np.diag(pcov)))

plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.show()

