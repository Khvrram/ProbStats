import numpy as np
import matplotlib.pyplot as plt

def geometricPmf(k, n):
   p = 1 / n
   return (1-p) ** (k-1) * p

n1 = 100
n2 = 150

kvalues = np.arange(1, 1001)
pmf1 = geometricPmf(kvalues, n1)
pmf2 = geometricPmf(kvalues, n2)

plt.figure(figsize=(10, 6))
plt.plot(kvalues, pmf1, label='n=100', color='blue')
plt.plot(kvalues, pmf2, label='n=150', color='red')

plt.title('Geometric distribution for n=100 and n=150')
plt.xlabel('Num of trials')
plt.ylabel('Probability mass function')
plt.legend()

plt.grid(True)
plt.show()
