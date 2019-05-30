from scipy.fftpack import ifftn,fftn
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import numpy as np
def plot_3d(x,Z):
    fig = plt.figure(figsize=(6,6))
    ax = fig.add_subplot(111, projection='3d')
    X,Y = np.meshgrid(x,x)
    ax.plot_surface(X, Y, Z)
    ax.view_init(45, 45) #rotaciona eixos de visualizacao 
    plt.show()
    

N = 30
f, ((ax1, ax2, ax3), (ax4, ax5, ax6)) = plt.subplots(2, 3, sharex='col', sharey='row')
xf = np.zeros((N,N)) #matrix nula NxN
xf[1, 1] = 10
#xf[N-5, N-5] = 10
Z1 = fftn(xf)
#plot_3d(x,Z)
ax1.imshow(xf, cmap=cm.Reds)
ax4.imshow(np.real(Z1), cmap=cm.gray)

#funcoes 
xf = np.zeros((N,N)) #matrix nula NxN
T = np.pi
x = np.linspace(0, T, N) # vetor de 0 ate N em 30 numeros
y = np.sin(x) # funcao para brincar
#plt.plot(x,y)
#plt.show()
xf[15,:] = y
xf[:,15] = y
Z2 = fftn(xf)
#plot_3d(x,Z)
ax2.imshow(xf, cmap=cm.Reds)
ax5.imshow(np.real(Z2), cmap=cm.gray)

Z3 = np.zeros((N,N))
T = 4*np.pi # FREQUENCIAS
x = np.linspace(0.0, T, N) 

for i,vx in enumerate(x):
    Z3[i,:] = np.sin(vx) #FUNCOES
    for j,vx in enumerate(x):
        Z3[i,j] = Z3[i,j]*np.sin( vx)

#Z[15, :] = np.sin(x)
#Z[:, 15] = np.sin(x)
#Z = ifftn(xf)

yf = ifftn(Z3)
ax3.imshow(np.real(yf), cmap=cm.Reds)
ax6.imshow(np.real(Z3), cmap=cm.gray)
plt.show()

plot_3d(x,Z1)

plot_3d(x,Z2)

plot_3d(x,Z3)