import numpy as np
from random import *
import itertools as it

seed(1)
np.random.seed(1)


def input_int(message=""):
    return int(input(message))


def ppl():

    estados = 0
    decisiones = 0
    n_matrices = 0

    mat_trans = []
    mat_costos = []

    precio_estimado = 0

    n_matrices =  input_int("¿Cuantas matrices tiene el problema?\n")
    estados = input_int("¿Cuantos estados tiene cada matriz?\n")
    decisiones = input_int("¿Cuantas decisiones tiene cada matriz?\n")

    print("\nLlenemos las {} matrices de transición\n".format(n_matrices))

    for i in np.arange(n_matrices):
        lista_matrices_t=[]
        print ("\nDe la matriz {}".format(i+1))

        for j in np.arange(estados):
            temp_rest = []
            
            for k in np.arange(decisiones):
                temp_rest.append(float(input(
                    "Dime el valor en la posicion ({},{}): ".format(j+1, k+1)
                    )))
            
            lista_matrices_t.append(temp_rest)
        
        lista_matrices_t=np.array(lista_matrices_t)
        print("\nLa matriz {} de transicion queda: \n".format(i+1))
        print(lista_matrices_t,"\n")



    '''print("\nAhora llenemos las {} matrices de costos\n".format(n_matrices))

    for i in np.arange(n_matrices):
        lista_matrices_c=[]
        print ("\nDe la matriz {}".format(i+1))

        for j in np.arange(estados):
            temp_rest = []
            
            for k in np.arange(decisiones):
                temp_rest.append(float(input(
                    "Dime el valor en la posicion ({},{}): ".format(j+1, k+1)
                    )))
            lista_matrices_c.append(temp_rest)
     
        lista_matrices_c=np.array(lista_matrices_c)
             
        print("\nLa matriz {} de costos queda: \n".format(i+1))
        print(lista_matrices_c,"\n")

        print("\nDime el valor de precio estimado de la matriz {}: ".format(i+1))
        precio_estimado = float(input(""))
        print("\nLa matriz {} de costos menos el costo estimado queda: \n".format(i+1))
        print(lista_matrices_c - precio_estimado,"\n")'''


    for i in range(estados):
        for j in range(len(lista_matrices_t[i])): 
            print("Escribe el costo de C({},{})".format(i+1,j+1))
            c=float(input())#Leemos costos
            mat_costos.append(c) #Agregamos a la lista

    mat_costos=np.array(mat_costos) #Convertimos a numpy array
    print(mat_costos, "{}")

    print("\nArmando el PPL queda de la siguiente forma: \n")

    print("Yik = {}".format(
            "".join([" Y{}{} +".format(i+1, j+1)
                     for i in range(estados) for j in range(len(lista_matrices_t))])[:-1]
        ))

    contador=0
    for i in range(len(lista_matrices_t)):
 
        for j in range (len(lista_matrices_t[i])):
 
            print(mat_costos[contador], "y{}{}+".format(i+1,j+1)[:-1])
            contador=contador+1






    print ("s.a")
    print("     {} {} {}".format(
            "".join([" Y{}{} +".format(i+1, j+1)
                     for i in range(estados) for j in range(len(lista_matrices_t))])[:-1],
            "=",
            "1"
        ))

    print("      Yik >=0 ")
    
            
        

            
            










if __name__ == "__main__":
    ppl()