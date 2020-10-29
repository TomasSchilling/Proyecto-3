import numpy as np
import matplotlib.pylab as plt

L= 1.04  #metros
n= 100

Nt= 5000 

dx= L/n
dt= 2.


x=np.linspace(0,L,n+1)

u= np.zeros((Nt,n+1))
u_fourier= np.zeros((Nt,n+1))

#condiciones 



  #   u[:,0]= 0  # izquierda

u[:,-1]=  20      #derecha

u[0,0:n]= 20     # temp. inicial

K = 79.5
c=450
rho = 7800
alpha= K*dt/(c*rho*dx**2)

N_ploteo=50
N_skip=3

def Serie_Fourier(t,x):
    n=1
    Temp_f=0
    while True:
        Temp_f +=( (40*(1-(-1)**n))/(n*np.pi) * np.sin( (n*np.pi*x)/L )  * np.e**(-alpha*(n*np.pi/L )**2*t)  )
        n+=1
        if n==100:
            return  Temp_f


for j in range(Nt-1):
    t = dt*j


    u[j,0]= -5*dx +u[j,1]
    u[0,0]= 20
        
    for i in range(1,n):
        u[j+1,i]= u[j,i]+  alpha*( u[j,i-1] -  2* u[j,i] +  u[j,i+1])
    

    if j % N_ploteo ==0:
        plt.plot(x,u[j,:])


    if j % (N_ploteo*N_skip)==0:
        plt.text(x[0],u[j,0], f"{t/3600:.1f}", fontsize=8, horizontalalignment= "center", verticalalignment="center"
                 ).set_bbox(dict(facecolor="white", alpha=0.4, edgecolor="black", boxstyle="round"))
                 
u[0,0]=20.


plt.title(f"k = {j}  t =  {j*dt}")
plt.ylabel("Temeratura, $T$  [°C]" )
plt.xlabel("Distancia, $x$ [m]")
plt.show()





Val_guardar=[]
Val_guardar.append(np.array(u[int(n/10),:]))
Val_guardar.append(np.array(u[int(n/5),:]))
Val_guardar.append(np.array(u[int(n/2.5),:]))



