from random import randrange

#realiza 100 ejecuciones del algoritmo con parametros aleatorios
def prueba():
    exe=100
    salida=''
    while exe!=0:
        a=randrange(9)
        salida=busquedaE(a)
        if(salida=='fracaso'):
            print('fracaso')
            break
        elif(salida=='exito'):
            print('exito')
        else:
            print('no hay solucion')
        exe-=1

def busquedaE(rest):
    sus=["El/la mejor amigo(a)","El/la novio(a)","El/la vecino(a)",
         "El mensajero","El extraño","El/la hermanastro(a)",
         "El/la colega de trabajo"]
    arma=["Pistola","Cuchillo","Machete","Pala","Bate","Botella","Tubo","Cuerda"]
    motivo=["Venganza","Celos","Dinero","Accidente","Drogas","Robo"]
    pdc=["Cabeza","Pecho","Abdomen","Espalda","Piernas","Brazos"]
    lugar=["Sala","Comedor","Baño","Terraza","Cuarto","Garage",
           "Patio","Balcón","Cocina"]
    
    categ=[sus,arma,motivo,pdc,lugar]
    #contiene las cartas de la solución generada
    sol=crearSol(categ)
    #contiene las parejas de restricciones
    res=crearRestric(categ, rest)
    #sugerencia del algoritmo
    sug=[]
    #contiene las posiciones de un elemento que es restriccion
    resActivas=[]
##    print('Solución: ',sol)
##    print('Restricciones: ',res)
    a=0
    b=0
    c=0
    d=0
    e=0
    contra=comprobarSol(res,sol)
    resActivas=[]
    while(True):
        sug=[]
        eliminado=0
        resActivas=[]
        while(len(categ[0])>a):
            if(comprobarRes(categ[0][a],resActivas,res)==False):               
                break
            else:
                if(len(categ[0])-1>a):
                    a+=1
        if(len(categ[0])==a):
            sug.append(categ[0][a-1])
        else:
            sug.append(categ[0][a])
        while(len(categ[1])>b):
            if(comprobarRes(categ[1][b],resActivas,res)==False):                
                break
            else:
                if(len(categ[1])>b+1):
                    b+=1
        if(len(categ[1])==b):
            sug.append(categ[1][b-1])
        else:
            sug.append(categ[1][b])
        while(len(categ[2])>c):
            if(comprobarRes(categ[2][c],resActivas,res)==False):                
                break
            else:
                if(len(categ[2])>c+1):
                    c+=1
        if(len(categ[2])==c):
            sug.append(categ[2][c-1])
        else:
            sug.append(categ[2][c])
        while(len(categ[0])>d):
            if(comprobarRes(categ[3][d],resActivas,res)==False):
                break
            else:
                if(len(categ[3])>d+1):
                    d+=1
        if(len(categ[3])==d):
            sug.append(categ[3][d-1])
        else:
            sug.append(categ[3][d])
        while(len(categ[4])>e and len(categ[4])!=e):
            if(comprobarRes(categ[4][e],resActivas,res)==False):
                break
            else:
                if(len(categ[4])-1>e):
                    e+=1
        if(len(categ[4])==e):
            sug.append(categ[4][e-1])
        else:
            sug.append(categ[4][e])
        #print('Sugerencia: ', sug)
        if(sug==sol):
            if(contra==True):
                return 'No hay solución'
            else:
                return 'exito'
        else:
            eliminado=eliminar(categ,sug,sol)
            if(eliminado==0):
                if(a>0):
                    a-=1
                sug[eliminado]=categ[0][a]
            elif(eliminado==1):
                if(b>0):
                    b-=1
                sug[eliminado]=categ[1][b]
            elif(eliminado==2):
                if(c>0):
                    c-=1
                sug[eliminado]=categ[2][c]
            elif(eliminado==3):
                if(d>0):
                    d-=1
                sug[eliminado]=categ[3][d]
            else:
                if(e>0):
                    e-=1
                sug[eliminado]=categ[4][e]
            #print('sugerencia: ',sug)
            if(sug==sol):
                if(contra==True):
                    return 'No hay solución'
                else:
                    return 'exito'
            elif(e<len(categ[4])-1):
                e+=1
            elif(d<len(categ[3])-1):
                e=0
                d+=1
            elif(c<len(categ[2])-1):
                e=0
                d=0
                c+=1
            elif(b<len(categ[1])-1):
                e=0
                d=0
                c=0
                b+=1
            elif(a<len(categ[0])-1):
                e=0
                d=0
                c=0
                b=0
                a+=1
            elif(len(categ[0])>1):
                e=0
            elif(len(categ[1])>1):
                d=0
            elif(len(categ[2])>1):
                c=0
            elif(len(categ[3])>1):
                b=0
            elif(len(categ[4])>1):
                a=0
            else:
                return 'fracaso'
            


def comprobarSol(res, sol):
    result1=False
    result2=True
    for i in range(len(res)):
        for j in range(len(res[i])):
            if res[i][j] in sol:
                result1=True
            else:
                result2=False
        if result1==True and result2==True:
            return True
    return False        

def comprobarRes(elemento, resActivas, res):
    for i in range(len(res)):
        if elemento in res[i]:
            if i in resActivas:
                resActivas.remove(i)
                return True
            else:
                resActivas.append(i)
    return False


def eliminar(categ, sug, sol):
    eliminar=0
    while(True):
        eliminar=randrange(5)
        if not sug[eliminar] in sol:
            break
    elemento=sug[eliminar]
    #print('Eliminado: ',elemento)
    if eliminar==0:
        categ[0].remove(elemento)
    if eliminar==1:
        categ[1].remove(elemento)
    if eliminar==2:
        categ[2].remove(elemento)
    if eliminar==3:
        categ[3].remove(elemento)
    if eliminar==4:
        categ[4].remove(elemento)
    return eliminar
        
def crearSol(c):
    salida=[]
    for i in range(5):
        salida.append(c[i][randrange(len(c[i]))])
    return salida
        

def crearRestric(c, r):
    salida=[]
    #contenedor de datos
    cont=[]
    while(r>0):
        copia=c.copy()
        rango=5
        for i in range(2):
            indice=randrange(rango)
            cont.append(copia[indice][randrange(len(copia[indice]))])
            copia.pop(indice)
            rango-=1
        salida.append(cont)
        cont=[]
        r-=1
    return salida
