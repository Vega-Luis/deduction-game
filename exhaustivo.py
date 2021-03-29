from random import randrange

def prueba():
    exe=100
    salida=''
    while exe!=0:
        a=randrange(9)
        salida=busquedaE(a)
        if(salida=='fracaso'):
            print('fracaso')
            break
        else:
            print('exito')
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
    #sol=['El/la novio(a)','Pistola','Venganza','Cabeza','Sala']
    #res=[['Vengana','Pistola']]
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
    while(True):#len(categ[0])>0 and len(categ[1])>0 and len(categ[2])>0 and len(categ[3])>0 and len(categ[4])>0):
        sug=[]
        eliminado=0
##        print('\n')
##        print(categ)
##        print(a,b,c,d,e)
        if(len(categ[0])==a):
            sug.append(categ[0][a-1])
        else:
            sug.append(categ[0][a])
        if(len(categ[1])==b):
            sug.append(categ[1][b-1])
        else:
            sug.append(categ[1][b])
        if(len(categ[2])==c):
            sug.append(categ[2][c-1])
        else:
            sug.append(categ[2][c])
        if(len(categ[3])==d):
            sug.append(categ[3][d-1])
        else:
            sug.append(categ[3][d])
        if(len(categ[4])==e):
            sug.append(categ[4][e-1])
        else:
            sug.append(categ[4][e])
        #print('Sugerencia: ', sug)
        if(sug==sol):
            return 'exito'
        elif(e<len(categ[4]) and e!=len(categ[4])):
            eliminado=eliminar(categ,sug,sol)
            e+=1
        elif(d<len(categ[3]) and d!=len(categ[3])):
            eliminado=eliminar(categ,sug,sol)
            e=0
            d+=1
        elif(c<len(categ[2]) and c!=len(categ[2])):
            eliminado=eliminar(categ,sug,sol)
            e=0
            d=0
            c+=1
        elif(b<len(categ[1]) and c!=len(categ[1])):
            eliminado=eliminar(categ,sug,sol)
            e=0
            d=0
            c=0
            b+=1
        elif(a<len(categ[0]) and a!=len(categ[0])):
            eliminado=eliminar(categ,sug,sol)
            e=0
            d=0
            c=0
            b=0
            a+=1
        else:
            return 'fracaso'
        if(eliminado==0):
            if(a>0):
                a-=1
        elif(eliminado==1):
            if(b>0):
                b-=1
        elif(eliminado==2):
            if(c>0):
                c-=1
        elif(eliminado==3):
            if(d>0):
                d-=1
        else:
            if(e>0):
                e-=1
        
       

def comprobarRes(elemento, resActivas, res):
    for i in range(len(resActivas)):
        if elemento in res[resActivas[i]]:
            resActivas.pop(i)
            return True   
    return False


def agregarRes(elemento, restricciones):
    for i in range(len(restricciones)):
        if elemento in restricciones[i]:
            return i
    return 6

def eliminar(categ, sug, sol):
    eliminar=0
    while(True):
        eliminar=randrange(5)
        if not sug[eliminar] in sol:
            break
    elemento=sug[eliminar]
    #print('Eliminado: ',elemento)
    #print(categ)
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
