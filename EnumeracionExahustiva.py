import numpy as np
from fractions import Fraction #Para aceptar fracciones en la entrada
from sympy import Matrix, linsolve, symbols
from scipy import linalg
from itertools import product
#Método de Mejoramiento de políticas con descuento
def Enumeracion_Politicas(m,k, s, matriztrans, politica, costos):
       # Empezamos el algoritmo    
    
    permutaciones=[]
    mat=[]
    for i in range(k):
        mat.append(i)
    mat=np.array(mat)
    
    
    for c in product(mat, repeat=m):
        permutaciones.append(c)     
    
    poliExha=[]
    for i in range(len(permutaciones)):
        cont=0
        for j in range(m):
            if(permutaciones[i][j] in politica[j]):
                cont=cont+1
            if(cont==m):
                   print("Politica R"+str(i+1)+" "+str(permutaciones[i]))
                   poliExha.append(permutaciones[i])
                   cont=0
                
    #print("El numero de politicas posibles es =", pow(k,m))
       # print("Politica %d" %(i+1)+ "="+ str(permutaciones(i)))
    resultado=[]

    
    for i in range(len(poliExha)):
        polArb=poliExha[i] #Se toma la primera decisión que hay en cada estado
        print("\nLa política R%d"%(i+1)+"="+str(polArb))
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
        print("\nLa costos de la política arbitraria son: \n", costoabr )  
            
        for i in range(m):
            for j in range(k):
                if(polArb[i]==j+1): #Si la política j es = al dato [i] de la política arbitraria
                    aux2=matriztrans[j][i] #De la fila i respecto a k=j
                    matriz.append(aux2)
        matriz=np.array(matriz) #Convertimos a numpy array
        print("\nLa matriz respecto a la política arbitraria es: \n", matriz)

            
        matriz2=[] #guardamos la matriz transpuesta
        aux4=[]
        aux5=[]
        resul=[]
        matriz3=[]
        aux6=[]
        aux7=[]
        matrizR=[]
        MatrizEstacionaria=[]
        MatEc=[]
        
                #matriz para la restriccion pi=p0+P1+..+Pn
        for i in range(m):
            for j in range(m):
                pi=np.ones((1,m))
                
        for i in range(m):
            for j in range(m):
                res=np.zeros((m-1,1))

                #print("matriz resultados")
        resul=np.append(res,[1])
        resul=np.array(resul)

        for c in range(len(matriz[1,: ])):
            aux4=matriz[:,c]
            matriz2.append(aux4)
        matriz2=np.array(matriz2)
            # print(matriz2)
                
            
        for i in range(m):
            for j in range(m):
                if (matriz2[i][j]!=0): #Siempre que no tenga 0's 
                   matriz2[i][j]=-1*matriz2[i][j] #Multiplicamos por -1, como si lo pasarmos al otro lado
                if(i==j):
                    matriz2[i][j]=1+matriz2[i][j]
            aux5=np.delete(matriz2,m-1, axis=0)
        
            
        matrizR=np.concatenate([aux5, pi], axis=0) #axis=0 es filas, axis=1 columnas
        matrizR=np.array(matrizR)


        print("\nEl sistema a Resolver es: " +str(matrizR)+" = "+str(costoabr))
    
        
        if np.linalg.det(matrizR) == 0:    
            x= None
            print("No se puede resolver")
        else:
            x=linalg.solve(matrizR,resul)
            x=np.array(x)
            MatrizEstacionaria=np.array(x)
            print("La solucion del sistema es:", MatrizEstacionaria)
            aux6=MatrizEstacionaria*costoabr #calculamos el vector solucion4
            print("La solucion a nuestro sistema tomando en cuenta los costos",aux6)
            aux7=np.sum(np.dot(MatrizEstacionaria,costoabr))
            print("E(c)=",aux7)
            resultado.append(aux7) 

    resultado=np.array(resultado)
    print("Estas son las E(C) de nuestras politicas\n",resultado)
     

    if(s=='min' or s=='MIN'):
        sol=np.min(resultado)  
        print("La solucion optima minima es:",sol)
    if(s=='max' or s=='MAX'):
        sol2=np.max(resultado)  
        print("La solucion optima maxima es:", sol2)     
        
        
    return 
 


