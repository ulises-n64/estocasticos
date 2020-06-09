

#from main import lectura_datos
#from (nombre archivo) import (nombre funcion)
import pdb 
import numpy as np
m=0
k=0
matriztrans=[]
politica=[]
costos=[]
s='s'

def aproximacionSucesiva(m,k, s, matriztrans, politica, costos):
    
    
    print("Dime tu error de tolerancia:\n")
    while True:
        try:
            error=float(input(""))     
            break
        except ValueError:
            print("Por favor digita un numero")

    
    print("Dime tu factor de descuento\n")
    while True:
        try:
            descuento=float(input(""))    
            break
        except ValueError:
            print("Por favor digita un numero")
    
    
    print("Dame tu numero maximo de iteraciones:\n")
    while True:
        try:
            n=int(input(""))  
            break
        except ValueError:
            print("Por favor digita un numero entero")


    
    

    #reordenamos los datos que nos llegan
    contador = 0
    if (s=="max"):
        local_costos=np.zeros((m,k))
    if (s=="min"):
        local_costos=np.full((m,k), 10**8)

        
    
    
    for i in range(len(politica)):
        for j in range (len(politica[i])):
            aux=politica[i][j]-1
            local_costos[i,aux]=costos[contador]
            contador = contador+1
            
    
    lista_auxiliar=[]
    local_matriz=np.zeros((k,(m*m)))
    for i in range (k):
        for j in range(m):
            for l in range(m):
                lista_auxiliar.append(matriztrans[i][j][l])
                
    contador=0
    for i in range(k):
        for j in range(m*m):
            local_matriz[i,j]=lista_auxiliar[contador]
            contador=contador+1
    
    #paso 1
    #buscamos los maximos
    if(s=="max"):
        vni=[]

        
        optima=[]
        #index=0
        operador=0
        sumatoria=0
        
        for i in range(m):
            lista_min=[]
            for j in range(k):
                lista_min.append(local_costos[i,j])
            minimo=min(lista_min)
            vni.append(minimo)
            for l in range(k):
                if (minimo==local_costos[i,l]):
                    index=l
            optima.append(index)
        #280+0.95[0.4(280)+0.5(255)+0.1(300)]
        #220+0.95[0.7(280)+0.2(255)+0.1(300)]
        #258+0.95[0.7(280)+0.5(255)+0.3(300)]
        iteracion=0
        error_maximo=10**8
        
        while(iteracion <= n and error_maximo > error):
            k_vni=[]
            newoptima=[]
            k_maximo=[]
            maximo=0

            contador=0
            for i in range(m):

                for j in range(k):
                    

                    for h in range(m):
                        
                        sumatoria=sumatoria+(vni[h]*matriztrans[j][i][h])
                    
                        

                    operador=local_costos[i,j]+(descuento*sumatoria)
                    k_maximo.append(operador)
                    sumatoria=0
                    operador=0
                maximo=max(k_maximo)
                for f in range(len(k_maximo)):
                    if (maximo==k_maximo[f]):
                        newoptima.append(f)
                k_vni.append(maximo)
                
                
                

                k_maximo=[] 
            er=[]
            for i in range(len(vni)):
                er.append(abs(vni[i]-k_vni[i]))
            
            error_maximo=max(er)           
                
            vni=k_vni
            print(f"los maximos de esta iteracion por estado fueron:\n\n{vni}\n")
            
            k_vni=0 
            print(f"El factor de error mas grande es de: {error_maximo}\n") 
            print(f"Iteracion: {iteracion}\n")
            print(f"R_{iteracion}({newoptima}) \nrecuerda que estamos empezando los indices en 0\n En el resultado final si empezaremos con indices iguales a 1\n")
            iteracion=iteracion+1



    if(s=="min"):
        vni=[]

        
        optima=[]
        #index=0
        operador=0
        sumatoria=0
        
        for i in range(m):
            lista_min=[]
            for j in range(k):
                lista_min.append(local_costos[i,j])
            minimo=min(lista_min)
            vni.append(minimo)
            for l in range(k):
                if (minimo==local_costos[i,l]):
                    index=l
            optima.append(index)
        #280+0.95[0.4(280)+0.5(255)+0.1(300)]
        #220+0.95[0.7(280)+0.2(255)+0.1(300)]
        #258+0.95[0.7(280)+0.5(255)+0.3(300)]
        iteracion=0
        error_maximo=10**8
        
        while(iteracion <= n and error_maximo>error):
            k_vni=[]
            newoptima=[]
            k_minimo=[]
            minimo=0

            contador=0
            for i in range(m):

                for j in range(k):
                    

                    for h in range(m):
                        
                        sumatoria=sumatoria+(vni[h]*matriztrans[j][i][h])
                    
                        

                    operador=local_costos[i,j]+(descuento*sumatoria)
                    k_minimo.append(operador)
                    sumatoria=0
                    operador=0
                minimo=min(k_minimo)
                for f in range(len(k_minimo)):
                    if (minimo==k_minimo[f]):
                        newoptima.append(f)
                k_vni.append(minimo)
                
                
                

                k_minimo=[]    
            er=[]
            for i in range(len(vni)):
                er.append(abs(vni[i]-k_vni[i]))
            error_maximo=max(er)

                
            vni=k_vni

            
            k_vni=0  
            print(f"los minimos de esta iteracion por estado fueron \n{vni}\n")
            
            print(f"El factor de error mas grande es de: {error_maximo}\n")
            print(f"Iteracion: {iteracion}\n")
            print(f"R_{iteracion}({newoptima}) \nrecuerda que estamos empezando los indices en 0\n En el resultado final si empezaremos con indices iguales a 1\n")
            iteracion=iteracion+1
    print("Problema resuelto\n\n\n")
    print(f"El numero de estados es igual a\n {m}")
    print(f"El numero de decisiones es igual a  \n {k}")
    if (s=="max"):
        print(f"Estas maximizando")
    if (s=="min"):
        print(f"Estas minimizando")
    print(f"matriz de transicion es: \n {matriztrans}")
    print(f"Las Politica aceptadas fueron \n {politica}")
    print(f"Los costos son igual a \n  {costos}")
    print(f"El error de tolerancia es igual a \n {error}")
    print(f"El factor de descuento es igual a \n {descuento}")
    print(f"Numero de iteraciones \n {n}")
    print(f"Se alcanzo la mejor aproximacion en {iteracion} iteraciones")
    for i in range(len(newoptima)):
        newoptima[i]=newoptima[i]+1
    print(f"La mejor aproximacion al optimo es de: {newoptima}")


















                


        


            





            



    


    


    





def lectura_de_prueba():
    global m, k, matriztrans, politica, costos, s
    s="max"
    m=3
    k=3
    costos=[280, 220, 258, 250, 110,255,220,-130, 300]
    costos=np.array(costos)
    politica= [[1, 2, 3],[1 ,2 ,3],[1 ,2, 3]]
    politica=np.array(politica)
    matriztrans=[[[0.4, 0.5, 0.1],[0.1, 0.7, 0.2],[0.1, 0.2, 0.7]],[[0.7, 0.2, 0.1],[0.3, 0.6, 0.1],[0.1, 0.7, 0.2]],[[0.2, 0.5, 0.3],[0, 0.7, 0.3],[0, 0.2, 0.8]]]
    matriztrans=np.array(matriztrans)
def lectura_de_prueba2():
    global m, k, matriztrans, politica, costos, s
    s="min"
    m=2
    k=5
    costos=[50,9,0,15,5]
    costos=np.array(costos)
    politica= [[4, 5],[1 ,2 ,3]]
    politica=np.array(politica)    
    matriztrans=[[[0, 0 ],[0.1,   0.9 ]], [[0,    0 ],[0.006, 0.994]],[[0,    0 ],[0,    1 ]], [[0,    1],[0, 0 ]],[[1, 0],[0,0]]]
    matriztrans=np.array(matriztrans)

    




if __name__ == "__main__":
    lectura_de_prueba()
    #lectura_de_prueba2()

    aproximacionSucesiva(m,k, s, matriztrans, politica, costos)
    
    


    
