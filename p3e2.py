import numpy as np
import matplotlib.pylab as plt

L= 1.04 
x_20=np.linspace(0,L,21)
Nt= 5000
tiempo=np.linspace(0,Nt/3600,Nt)
def Calculo_matriz(delta_t,malla):
    """delta t es el tiempo pasante en segundo
    y malla la cantidad de nodos que se encuentran    """
    L= 1.04  #metros
    n= malla
    Nt= 5000 
    dx= L/n
    dt= float(delta_t)
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
    
    N_ploteo=1000
    N_skip=5
    
    for j in range(Nt-1):
        t = dt*j
    
        u[j,0]= -5*dx +u[j,1]
        u[0,0]= 20
            
        for i in range(1,n):
            u[j+1,i]= u[j,i]+  alpha*( u[j,i-1] -  2* u[j,i] +  u[j,i+1])
        
        """
        if j % N_ploteo ==0:
            plt.plot(x,u[j,:])
    
        if j % (N_ploteo*N_skip)==0:
            plt.text(x[0],u[j,0], f"{t/3600:.1f}", fontsize=8, horizontalalignment= "center", verticalalignment="center"
                     ).set_bbox(dict(facecolor="white", alpha=0.4, edgecolor="black", boxstyle="round"))
                      """
    return u


"""
plt.title(f"k = {j}  t =  {j*dt}")
plt.ylabel("Temeratura, $T$  [°C]" )
plt.xlabel("Distancia, $x$ [m]")
plt.show()
"""

pi= np.pi
e=np.e
def Serie_Fourier(t,x):
    nn=1
    Temp_f=0
    while True:
        Temp_f +=((40*(1-(-1)**nn))/(nn*pi)*np.sin( (nn*pi*x)/L)  * e**(-alpha*(nn*pi/L )**2*t))
        nn+=1
        if nn==10:
            return  Temp_f
        








Tiempo_1=Calculo_matriz(1,20)
Tiempo_2=Calculo_matriz(2,20)
Tiempo_5=Calculo_matriz(5,20)
Tiempo_10=Calculo_matriz(10,20)
Tiempo_50=Calculo_matriz(50,20)
#Tiempo_100=Calculo_matriz(100,20)


largos={2:"0.104",4:"0.208",8:"0.416"}

l_i=[2,4,8]

for i in l_i:
    plt.plot (tiempo,Tiempo_1[:,l_i],label="Malla 20 Delta_t = 1 [seg]")
    plt.plot (tiempo,Tiempo_2[:,l_i],label="Malla 20 Delta_t = 2 [seg]")
    plt.plot (tiempo,Tiempo_5[:,l_i],label="Malla 20 Delta_t = 5 [seg]")
    plt.plot (tiempo,Tiempo_10[:,l_i],label="Malla 20 Delta_t = 10 [seg]")
    plt.plot (tiempo,Tiempo_50[:,l_i],label="Malla 20 Delta_t = 50 [seg]")
    
    plt.legend(loc=1)
    plt.title(f" x = {largos[i]}")
    plt.ylabel("Temeratura, $T$  [°C]" )
    plt.xlabel("Tiempo  [Horas]")
    plt.show()




# Matriz con la serie de Fouirer

"""

for i in range(len(u_fourier[0])):
    print (i)
    for j in range (len(u_fourier)):
        u_fourier[j,i]=abs(Serie_Fourier(j/3600,i))
    
for j in range(10):
    plt.plot(x,u_fourier[100*j,:])


plt.show()

"""





