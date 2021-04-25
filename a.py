import numpy as np
import matplotlib.pyplot as plt

x = np.array([1,2,3])
y = x * 10
print(x, y)

plt.plot(x, y)
# plt.show()
plt.savefig("img.png")
