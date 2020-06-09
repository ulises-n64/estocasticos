import numpy as np

def ppl(m,k, matriztrans, costos):
   
    matriztrans=np.array(matriztrans)
    costos = np.array(costos)
    

    #print("\nLlenemos las {} matrices de transición\n".format(n_matrices))
    '''
    for i in np.arange(n_matrices):
        lista_matrices_t=[]
        datos_extraidos = []
        print ("\nDe la matriz {}".format(i+1))
        for j in np.arange(m):
            temp_rest = []
            datos_extraidos=[]
            for k in np.arange(k):
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
                     for i in range(m) for j in range (len(matriztrans))])[:-1]
        ))

    #Funcion objetivo
    contador=0
    temp=[]
    for i in range(len(costos)):
        temp.append(costos[i])
    
    print("{}{} ".format("\nMinZ=",
            "".join([" ({})y{}{} +".format(val, i+1,index+1)
                     for index, val in enumerate(temp)])[:-1]
            ))
        
    #Restricciones
    print ("s.a")
    print("     {} {} {}".format(
            "".join([" Y{}{} +".format(i+1, j+1)
                     for i in range(m) for j in range(len(matriztrans))])[:-1],
            "=",
            "1"
        ))

   
    #Armar las j
    mat_j = np.transpose(matriztrans)
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
            for j in range(m)
                    ])[:-1],
            "=",
            "0"                
            ))
    

    print("\nYik >=0 ")
