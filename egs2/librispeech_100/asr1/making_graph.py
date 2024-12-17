import numpy as np
import matplotlib.pyplot as plt

fig = plt.figure()
ax = fig.add_subplot(111)
x_1 = np.linspace(0.4, 0.6, 3)
y_1 = np.array([5,6,7])
x_2 = np.linspace(0.4, 0.6, 3)
y_2 = np.array([4,5,6])
ax.plot(x_1, y_1, label='y=x')
ax.plot(x_2, y_2, label='$y=x^2$')
plt.xticks(np.arange(0.4, 0.61, step=0.1))
ax.set_xlabel('penalty')
ax.set_ylabel('p')
plt.legend(loc='best')
plt.savefig("result.png")