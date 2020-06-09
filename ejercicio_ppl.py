import numpy as np
from scipy.optimize import linprog
def solucion_lineal(m,k,costos,matriztrans):
    c = []
    b = [1]
    a = []
    mat_unos = []
    for i in range(m):
        for i in range(k):
            mat_unos.append(1)
    a.append(mat_unos[:])
   
    for i in range(m):
        for j in range(k):
            c.append(costos[i])
   
    for i in range(m):
        b.append(0)
   
    for j in range(m):
        ecuacion = []
        for i in range(m):
            for x in range(k):
                
                if j == i:
                    ecuacion.append(1-matriztrans[x][i][j])
                else:
                    ecuacion.append(-matriztrans[x][i][j])
        a.append(ecuacion[:])                    
    return np.array(a),np.array(b),np.array(c)

def ppl(m,k, matriztrans, costos, s):
   
    matriztrans=np.array(matriztrans)
    costos = np.array(costos)

    print("\nArmando el PPL queda de la siguiente forma: \n")

    print("Yik = {}".format(
            "".join([" Y{}{} +".format(i+1, j+1)
                     for i in range(m) for j in range (len(matriztrans))])[:-1]
        ))

    #Funcion objetivo
    temp=[]
    for i in range(len(costos)):
        temp.append(costos[i])
    print("{}{} ".format("\nMinZ=",
            "".join([" ({})y{}{} +".format(val, i+1,index+1)
                    for index, val in enumerate(costos)])[:-1]
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

    A,b,c = solucion_lineal(m,k,costos,matriztrans)
    if s=="max":
        res = linprog(-c,A_eq = A, b_eq = b)    
        print(res)
    else:
        res = linprog(c,A_eq = A, b_eq = b)    
        print(res)