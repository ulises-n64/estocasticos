import numpy as np
from fractions import Fraction #Para aceptar fracciones en la entrada
from sympy import Matrix, linsolve, symbols
import math

#Método de Mejoramiento de políticas con descuento
def mejoramientoPoliticaDescuento(m,k, s, matriztrans, politica, costos):
    alpha=Fraction(input("¿Cuál es el factor de descuento? "))
    #Empezamos el algoritmo    
    polArb=[x[0] for x in politica] #Se toma la primera decisión que hay en cada estado
    print("La política arbitraria inicial es: R0"+str(polArb)+"") #Politica arbitraria
    stop=0
    n=1
    while (stop!=1): 
        matriz=[] #Definimos la matriz de transicion respecto a la politica 
        aux2=[]
        costoabr=[]
        aux3=[]
        b=0 #Contador
        for i in range(m):
            for j in range(len(politica[i])): #Medimos el lengeth de la política 
                for x in range(k):
                    if(polArb[i]==x+1 & x+1==politica[i][j] ): #La política arbitraria y las decisiones son iguales
                        aux3=costos[b] #El costo[i][j]
                        costoabr.append(aux3)
                b=b+1 #Aumentamos para saber la posición exacta del costo
        costoabr=np.array(costoabr)
        print("La costos de la política arbitraria son:", costoabr )       
        
        for i in range(m):
            for j in range(k):
                if(polArb[i]==j+1): #Si la política j es = al dato [i] de la política arbitraria
                    aux2=matriztrans[j][i] #De la fila i respecto a k=j
                    matriz.append(aux2)
        matriz=np.array(matriz) #Convertimos a numpy array
        print("La matriz respecto a la política arbitraria es: ", matriz)
        #gR1=Cik+sum(Pij(k)*Vj(Rn))-Vi(Rn) 
        #NOTA: VmR(n)=0
        print("ITERACION ", n)
        gRn=[]
        bmatrix=[]
        #Empezamos con la iteracion
        for i in range(m):
            for j in range(m):
                if (matriz[i][j]!=0): #Siempre que no tenga 0's 
                    matriz[i][j]=alpha*(matriz[i][j]) #Multiplicamos por -1, como si lo pasarmos al otro lado
                    matriz[i][j]=-1*matriz[i][j]
        matriz2=np.zeros((m,m)) #Creamos la matriz y la llenamos de 0's
        for i in range(m):
            for j in range(m):
                    if(i==j):
                        matriz2[i][i]=1+(matriz[i][i]) #En la diagonal
                    else:
                        matriz2[i][j]=matriz[i][j]
                
        matriz2=np.array(matriz2) #Convertimos a numpy array
        
        print("El sistema queda: " +str(matriz2)+" = "+str(costoabr))
        if np.linalg.det(matriz2) == 0: #verificamos el determinante para ver si tiene slucion
            r= None
            print("No se puede resolver")
        else:
            r=np.dot(np.linalg.inv(matriz2),costoabr).round(decimals=2) #calculamos el vector solucion
        r=np.array(r)
        print("La solución del sistema de ecuaciónes: ", r)
        
        #Mejoramiento de política
        aux6=0 #Contador
        maxmin=[]
        mejorpolitica=[]
        aux8=[]
        for i in range(m):
            aux5=0
            aux7=[]
            for j in range(k):  
                if(j+1 in politica[i]): #Si la decisión k está en la politica[i]
                    print("i= "+str(i)+" K= "+str(j+1)) 
                    aux5=r.dot(matriztrans[j][i])
                    print("("+str(costos[aux6])+")+("+str(alpha)+")*("+str(aux5)+")")
                    aux5=costos[aux6]+(alpha*aux5)
                    print("= ", aux5) 
                    aux7.append(aux5) 
                    aux8.append(aux5)    #SABER DONDE ESTA LA POLITICA OPTIMA
                    aux6=aux6+1 #Vamos aumentando
                if(j==k-1): #Ya acabó de checar los estados posibles
                    if(s=='min' or s=='MIN'):
                        maxmin.append(np.min(aux7)) #Elegimos el mínimo
                    elif(s=='max'  or s=='MAX'):
                        maxmin.append(np.max(aux7)) #Elegimos el máximo
        
        maxmin=np.array(maxmin)
        aux8=np.array(aux8)
        
        contador=0
        for i in range(m):
            for j in range(k):
                if(j+1 in politica[i]):
                    if(maxmin[i]==aux8[contador]):
                        mejorpolitica.append(j+1) 
                    contador=contador+1
                    
        mejorpolitica=np.array(mejorpolitica)
        print("El "+str(s)+" es:" +str(maxmin))
        print("La mejor política es: ", mejorpolitica)
        banderita=0
        for i in range(m):
            if(polArb[i]!=mejorpolitica[i]):
                banderita=banderita+1
            if(banderita!=0 and i==m-1):
                n=n+1
                for i in range(m):
                    polArb[i]=mejorpolitica[i]
        if(banderita==0):
            stop=1
            print("La política óptima es: ", mejorpolitica)
    return 
