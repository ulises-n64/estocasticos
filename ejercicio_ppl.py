import numpy as np


def input_int(message=""):
    return int(input(message))


def ppl():

    estados = 3
    decisiones = 3
    n_matrices = 3

    mat_trans = [[0.4,0.5,0.1],[0.1,0.7,0.2],[0.1,0.2,0.7]]
    mat_costos = [[280, 220, -130]]
    mat_trans=np.array(mat_trans)
    mat_costos = np.array(mat_costos)
    


    #print("\nLlenemos las {} matrices de transición\n".format(n_matrices))
    '''
    for i in np.arange(n_matrices):
        lista_matrices_t=[]
        datos_extraidos = []
        print ("\nDe la matriz {}".format(i+1))

        for j in np.arange(estados):
            temp_rest = []
            datos_extraidos=[]
            for k in np.arange(decisiones):
                temp_rest.append(float(input(
                    "Dime el valor en la posicion ({},{}): ".format(j+1, k+1)
                    )))

            lista_matrices_t.append(temp_rest)
        lista_matrices_t=np.array(lista_matrices_t)
        print("\nLa matriz {} de transicion queda: \n".format(i+1))
        print(lista_matrices_t,"\n")
        print("{}".format(lista_matrices_t[i)]''' 



    print("\nArmando el PPL queda de la siguiente forma: \n")

    print("Yik = {}".format(
            "".join([" Y{}{} +".format(i+1, j+1)
                     for i in range(estados) for j in range(len(mat_trans[i]))])[:-1]
        ))

    #Funcion objetivo
    contador=0
    temp=[]
    for i in range(len(mat_costos)):
 
        for j in range (len(mat_costos[i])):
            temp.append(mat_costos[:,contador])
            contador=contador +1
        print("{}{} ".format("\nMinZ=",
            "".join([" ({})y{}{} +".format(val, i+1,index+1)
                     for index, val in enumerate(temp)])[:-1]
            ))
        
    #Restricciones
    print ("s.a")
    print("     {} {} {}".format(
            "".join([" Y{}{} +".format(i+1, j+1)
                     for i in range(estados) for j in range(len(mat_trans))])[:-1],
            "=",
            "1"
        ))

   
    #Armar las j
    mat_j = np.transpose(mat_trans)
    mat_j[:,0]=mat_j[:,0]-1
    mat_j=(-1)*mat_j
    mat_j=np.array(mat_j)
    temp_j=[]
    for i in range (len(mat_j)):
        print ("\nJ={}\n".format(i+1))
        for j in range (len(mat_j[i])):
            temp_j.append(mat_j[i,j])
            
        
        print("{} {} {} ".format(
            "".join([" ({})y{}{} +".format(mat_j[i,j], i+1,j+1)
            for j in range(decisiones)
                    ])[:-1],
            "=",
            "0"                
            ))
    

    print("\nYik >=0 ")
    
            
        

            
            










if __name__ == "__main__":
    ppl()