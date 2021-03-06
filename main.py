from MejoramientoPoliticaDescuento import mejoramientoPoliticaDescuento

from MejoramientoPolitica import mejoramientoPolitica


from AproximacionSucesiva import aproximacionSucesiva

from EnumeracionExahustiva import Enumeracion_Politicas
from ejercicio_ppl import ppl

#from (nombre archivo) import (nombre funcion)
import numpy as np
from fractions import Fraction

 #Para aceptar fracciones en la entrada

def input_int(message=""):
    return int(input(message))
#Definición variables de lectura
m=0
k=0
matriztrans=[]
politica=[]
costos=[]
s='s'

def lectura_datos():
    global m, k, matriztrans, politica, costos, s
    print("Por:")
    print("Rangel Huerta Alejandra")
    print("Hernandez Martinez Abraham")
    print("Ramiréz Calnacasco Ulises")
    print("Soto Aguilar Ethel\n")

    print("Procederemos a capturar los datos de tu problema:\n")
    
    m=int(input("Cuantos estados tienes?\n"))
    m=m+1 #Los estados deben ser m+1
    k=int(input("Cuantas decisiones tienes?\n")) #Leemos las decisiones(k)
    print("¿Es un problema maximizado o minimizado? Escribe max o min")
    s=input()

    #Inicializamos la matriz de mxm con 0's
    matriztrans=[] #Definimos la matriz de costos
    politica=[] #Definimos la matriz
    aux=[]
    
    for i in range(k):
       aux=np.zeros((m,m)) #La matriz k de tamaño mxm se llena de 0's
       matriztrans.append(aux) #Guardamos 
    matriztrans=np.array(matriztrans) #Convertimos numpy array
            
    for i in range(m):
        print("Escribe las decisiones que aplica al estado "+str(i)+", separado por espacios")
        estados=list(map(int, input().split())) #Leemos los datos, solo aceptamos enteros
        aux=np.array(estados)
        politica.append(aux)
    politica=np.array(politica) #Convertimos a numpy array
    
    c=0 #inicializamos la variable costos
    a=[] #Guardamos los tamaños de las matrices de decisión  
    print("Escribe los datos de la fila de la matriz de transición, separados por espacios")
    for i in range(k):
        for j in range(len(politica)): #De acuerdo al tamaño de la política, aunque también es m
            if(i+1 in politica[j]): #Si la decisión k está en la política j 
                print("Estado m="+str(j)+", Decision k="+str(i+1))
                matriztrans[i][j]=list(map(Fraction, input().split())) #Aceptamos fracciones

                
    costos=[] #Definimos una matriz que guardará la información
    for i in range(m):
        for j in range(len(politica[i])): #Leemos la longitud de cada matriz de Politca. TIP: politica[i][j]
            print("Escribe el costo de C"+str(i)+str(politica[i][j]))
            c=float(input())#Leemos costos
            costos.append(c) #Agregamos a la lista

    costos=np.array(costos) #Convertimos a numpy array
    return (k, m, s, matriztrans, politica, costos)
def main():
    otro_metodo=1
    while(otro_metodo==1):

        print("Hola usuario.")
        print("¿Qué metodo quieres resolver hoy?")
        print("1. Enumeracion exhaustiva de politicas")
        print("2. Plantear el modelo de programacion lineal")
        print("3. Metodos de mejoramiento de politicas")
        print("4. Mejoramiento de politica con descuento")
        print("5. Metodo de aproximaciones sucesivas")
        while True:
            try:
                metodo = int(input(""))
                if (metodo == 1 or metodo == 2 or metodo == 3 or metodo == 4 or metodo == 5):
                    break

                else:
                    print("Por favor digita un numero valido")



            except ValueError:
                print("Por favor digita un numero valido")



        if metodo == 1:
            print("Resolveremos por Enumeracion exhaustiva de politicas")
            
            Enumeracion_Politicas(m,k, s, matriztrans, politica, costos)
            
            print("¿Desas resolver otro metodo con los mismos datos? Presiona 1 para si, 2 para no, 0 para cerrar el programa")
            while True:
                try:
                    otro_metodo = int(input(""))
                    if (otro_metodo==2):
                       
                        lectura_datos()
                        main()
                    if (otro_metodo == 1 or otro_metodo == 0 ):
                        break

                    else:
                        print("Por favor digita un numero valido")

                except ValueError:
                    print("Por favor digita un numero valido")


        elif metodo == 2:
            print("Plantearemos el PPL")
            ppl(m,k, matriztrans, costos, s)
            print("¿Desas resolver otro metodo con los mismos datos? Presiona 1 para si, 2 para no, 0 para cerrar el programa")
            while True:
                try:
                    otro_metodo = int(input(""))
                    if (otro_metodo==2):
                       
                        lectura_datos()
                        main()
                    if (otro_metodo == 1 or otro_metodo == 0 ):
                        break

                    else:
                        print("Por favor digita un numero valido")

                except ValueError:
                    print("Por favor digita un numero valido")
        elif metodo == 3:
            print("Resolveremos por Metodos de mejoramiento de politicas")

            mejoramientoPolitica(m,k, s, matriztrans, politica, costos)

            print("¿Desas resolver otro metodo con los mismos datos? Presiona 1 para si, 2 para no y 0 para cerrar el programa")
            while True:
                try:
                    otro_metodo = int(input(""))
                    if (otro_metodo==2):
                       
                        lectura_datos()
                        main()
                    if (otro_metodo == 1 or otro_metodo == 0 ):
                        break

                    else:
                        print("Por favor digita un numero valido")

                except ValueError:
                    print("Por favor digita un numero valido")
        elif metodo == 4:
            print("Resolveremos por Mejoramiento de politica con descuento")

            mejoramientoPoliticaDescuento(m,k,s,matriztrans,politica,costos)

            print("¿Desas resolver otro metodo con los mismos datos? Presiona 1 para si, 2 para no y 0 para cerrar el programa")
            while True:
                try:
                    otro_metodo = int(input(""))
                    if (otro_metodo==2):
                       
                        lectura_datos()
                        main()
                    if (otro_metodo == 1 or otro_metodo == 0 ):
                        break

                    else:
                        print("Por favor digita un numero valido")
                except ValueError:
                    print("Por favor digita un numero valido")
        elif metodo == 5:
            print("Resolveremos por Metodo de aproximaciones sucesivas")
            aproximacionSucesiva(m,k, s, matriztrans, politica, costos)

            print("¿Desas resolver otro metodo con los mismos datos? Presiona 1 para si, 2 para no y 0 para cerrar el programa")
            while True:
                try:
                    otro_metodo = int(input(""))
                    if (otro_metodo==2):
                       
                        lectura_datos()
                        main()
                    if (otro_metodo == 1 or otro_metodo == 0 ):
                        break
                    else:
                        print("Por favor digita un numero valido")
                except ValueError:
                    print("Por favor digita un numero valido")



if __name__ == "__main__":
    
    lectura_datos()
    main()
