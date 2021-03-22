from random import randrange
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
    return res


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
        for i in range(2):
            indice=randrange(5)
            cont.append(copia[indice][randrange(len(copia[indice]))])
            copia.pop(indice)
        salida.append(cont)
        cont=[]
        r-=1
    return salida
