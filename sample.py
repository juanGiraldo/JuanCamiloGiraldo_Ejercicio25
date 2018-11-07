import numpy as np
import matplotlib.pyplot as plt

muestra=np.genfromtxt('sample.dat')

mu=np.mean(muestra)
sigma=np.std(muestra)

gaussed=mu+sigma*muestra

bins = np.linspace(-10, 10, 100)

plt.hist(muestra, bins, normed=True, alpha=0.5, label='datos de C')
plt.hist(gaussed, bins, normed=True, alpha=0.5, label='Gaussiana de python')
plt.legend(loc='best')
plt.savefig('sample.pdf')

