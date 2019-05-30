import numpy as np
from scipy.fftpack import fft
import matplotlib.pyplot as plt
# Number of sample points
N = 600
# sample spacing
T = 1.0 / 800.0
x = np.linspace(0.0, N*T, N) # pesquisar sobre np.linspace
#x = list(np.arange(0.0, N*T, N)) # nao permite o funcionamento do comando seguinte
y = np.sin(50.0 * 2.0*np.pi*x) + 0.5*np.sin(80.0 * 2.0*np.pi*x) + 0.3*np.sin(100.0 * 2.0*np.pi*x) 
# amplitude(deslocamento vertical)*np.sin(frequencia(deslocamento horizontal na transformada) * 2.0*np.pi*x) 
yf = fft(y)
xf = np.linspace(0.0, 1.0/(2.0*T), N//2)
plt.plot(x,y)
plt.show()
plt.plot(xf, 2.0/N * np.abs(yf[0:N//2]))
#plt.xkcd()
plt.grid()
plt.show()










