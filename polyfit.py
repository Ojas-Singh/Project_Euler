import numpy as np
import matplotlib.pyplot as plt

points = np.array([(2.1,0.605),(2.94,0.58),(3.36,0.532),(3.53,0.478),(3.85,0.312),(4.4,0.258),(7.2,0.227)])
# get x and y vectors
x = points[:,0]
y = points[:,1]

# calculate polynomial
z = np.polyfit(x, y, 1)
f = np.poly1d(z)

# calculate new x's and y's
x_new = np.linspace(x[0], x[-1], 50)
y_new = f(x_new)

plt.plot(x,y,'o', x_new, y_new)
plt.xlim([x[0]-1, x[-1] + 1 ])
plt.show()
