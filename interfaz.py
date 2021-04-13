from tkinter import Tk, Text, Button, Entry, END, Label
import tkinter as tk
from tkinter import ttk
from random import randrange
import time
import random



sospechoso=["El/la mejor amigo(a)","El/la novio(a)","El/la vecino(a)","El mensajero","El extraño","El/la hermanastro(a)","El/la colega de trabajo"]
arma=["Pistola","Cuchillo","Machete","Pala","Bate","Botella","Tubo","Cuerda"]
motivo=["Venganza","Celos","Dinero","Accidente","Drogas","Robo"]
pdc=["Cabeza","Pecho","Abdomen","Espalda","Piernas","Brazos"]
lugar=["Sala","Comedor","Baño","Terraza","Cuarto","Garage","Patio","Balcón","Cocina"]

cards = [["El/la mejor amigo(a)","Pistola", "Venganza","Cabeza", "Sala"],
         ["El/la novio(a)","Cuchillo", "Celos", "Pecho", "Comedor"],
         ["El/la vecino(a)","Machete","Dinero","Abdomen","Baño"],
         ["El mensajero","Pala","Accidente","Espalda","Terraza"],
         ["El extraño","Bate","Drogas","Piernas","Cuarto"],
         ["El/la hermanastro(a)","Botella","Robo","Brazos","Garage"],
         ["El/la colega de trabajo","Tubo","","","Patio"],
         ["","Cuerda","","","Balcón"],
         ["","","","","Cocina"]]

categ=[sospechoso,arma,motivo,pdc,lugar]

solution=[]

restringedCards = []
restrictedPairs = []
mostrar=[]

def crearSol(c):
    salida=[]
    for i in range(5):
        salida.append(c[i][randrange(len(c[i]))])
    return salida

class Interfaz:
    def __init__(self, ventana):
        self.ventana=ventana
        self.ventana.title("Juego de cartas")
        self.pantalla=Text(ventana, state="disabled")
        self.pantalla.grid(row=1,column=0,columnspan=4,padx=5,pady=5)
        self.pantalla2=Text(ventana,state="disabled")
        self.pantalla2.grid(row=1,column=4,columnspan=8,padx=5,pady=5)

        #En esta variable se concatena lo que sea desea mostrar en la pantalla
        self.salida=""
        self.salida2=""

        self.entrada = tk.StringVar()
        self.entry=ttk.Entry(ventana, textvariable=self.entrada, width=30).place(x=525, y=418)

        self.var5 = tk.StringVar()
        self.campo=ttk.Entry(ventana, textvariable=self.var5, width=30).place(x=300, y=2)

        self.var6 = tk.StringVar()
        self.campo2=ttk.Entry(ventana, textvariable=self.var6, width=30).place(x=950, y=2)

        self.var9 = tk.StringVar()
        self.campo3=ttk.Entry(ventana, textvariable=self.var9, width=30).place(x=len("Número de parejas:")+150, y=418)

        self.var = tk.StringVar()
        self.label = Label(ventana,textvariable=self.var,width=10,height=1).place(x=0,y=0)
        self.var.set("Exhaustivo")

        self.var7 = tk.StringVar()
        self.label4 = Label(ventana,textvariable=self.var7,width=len("Número de parejas:"),height=1).place(x=len("Número de ejecuciones:")+350,y=418)
        self.var7.set("Número de parejas:")
        
        self.var8 = tk.StringVar()
        self.label5 = Label(ventana,textvariable=self.var8,width=len("Número de ejecuciones:"),height=1).place(x=0,y=418)
        self.var8.set("Número de ejecuciones:")

        self.var4 = tk.StringVar()
        self.label4 = Label(ventana,textvariable=self.var4,width=20,height=1).place(x=150,y=0)
        self.var4.set("Tiempo de ejecución:")

        self.var3 = tk.StringVar()
        self.label3 = Label(ventana,textvariable=self.var3,width=20,height=1).place(x=800,y=0)
        self.var3.set("Tiempo de ejecución:")

        self.var2 = tk.StringVar()
        self.label2 = Label(ventana,textvariable=self.var2,width=10,height=1)
        self.label2.grid(row=0,column=4)
        self.var2.set("Backtracking")

        botonE=Button(self.ventana,text="Ejecución simple",width=len("Ejecución simple"),height=1,command=lambda:self.click(self.entrada.get(),True))
        botonE.grid(row=5,column=3,columnspan=8)
        botonEM=Button(self.ventana,text="Ejecución múltiple",width=len("Ejecución múltiple"),height=1,command=lambda:self.click2(self.entrada.get(),self.var9.get(),False))
        botonEM.grid(row=5,column=5,columnspan=8)
        botonEM=Button(self.ventana,text="Limpiar",width=len("Limpiar"),height=1,command=lambda:self.limpiar())
        botonEM.grid(row=5,column=9,columnspan=8)

    def limpiar(self):
        global solution
        global restrictedPairs
        global restringedCards
        solution=[]
        restrictedPairs=[]
        restringedCards=[]
        self.salida=""
        self.salida2=""
        self.pantalla.configure(state="normal")
        self.pantalla.delete("1.0",END)
        self.pantalla.configure(state="disabled")
        self.pantalla2.configure(state="normal")
        self.pantalla2.delete("1.0",END)
        self.pantalla2.configure(state="disabled")
        self.var5.set("")
        self.var6.set("")
    
    def click(self,entrada,valor):
        #entrada corresponde al numero de parejas
        #mostrar correponde a un booleano para saber si la funcion
        #debe imprimir resultados

        global solution
        global restrictedPairs
        global restringedCards
        global mostrar
        mostrar=valor

        #Se crea el arreglo solucion y las parejas de restricciones para ambos algoritmos
        restrictedPairs=self.crearRestric(categ,int(entrada))
        solution=self.crearSol(categ)
        
        #llamada al algoritmo exhaustivo
        t_ini=time.perf_counter()
        self.busquedaE(solution)
        t_fin=time.perf_counter()-t_ini
        self.var5.set("%0.10f segundos." % t_fin)

        #llamada al backtracking
        t_ini2=time.perf_counter()
        if(mostrar==True):
            self.salida2+="Solución a encontrar: "+str(solution)+"\n"
        self.backtracking([False], 0, 0, ["", "", "", "", ""])
        t_fin2=time.perf_counter()-t_ini2
        self.var6.set("%0.10f segundos." % t_fin2)

        #Mostrar resultados en pantalla
        self.mostrarEnPantalla(self.salida)
        self.mostrarEnPantalla2(self.salida2)

    def click2(self,entrada,numEje,valor):
        global solution
        global restrictedPairs
        global restringedCards
        global mostrar
        ejecuciones=int(numEje)
        mostrar=valor
        exhaus=[]
        back=[]
        while(ejecuciones!=0):
            restringedCards=[]
            if(entrada=="n" or entrada=="N"):
                restrictedPairs=self.crearRestric(categ,randrange(100))
            else:
                restrictedPairs=self.crearRestric(categ,int(entrada))
            solution=self.crearSol(categ)

            #llamada del exhaustivo
            t_ini=time.perf_counter()
            self.busquedaE(solution)
            t_fin=time.perf_counter()-t_ini
            exhaus.append(t_fin)

            #Llamada del backtracking
            t_ini2=time.perf_counter()
            if(mostrar==True):
                self.salida2+="Solución a encontrar: "+str(solution)+"\n"
            self.backtracking([False], 0, 0, ["", "", "", "", ""])
            t_fin2=time.perf_counter()-t_ini2
            back.append(t_fin2)
            ejecuciones-=1
            
        self.var5.set("%0.10f segundos." % (sum(exhaus)/len(exhaus)))
        self.var6.set("%0.10f segundos." % (sum(back)/len(back)))

        self.mostrarEnPantalla(self.salida)
        self.mostrarEnPantalla2(self.salida2)

    def mostrarEnPantalla(self, valor):
        self.pantalla.configure(state="normal")
        self.pantalla.insert(END,valor)
        self.pantalla.configure(state="disabled")
        
    def mostrarEnPantalla2(self, valor):
        self.pantalla2.configure(state="normal")
        self.pantalla2.insert(END,valor)
        self.pantalla2.configure(state="disabled")


############################################################################ EXHAUSTIVO ############################################################################
    def busquedaE(self, solucion):
        sospechoso=["El/la mejor amigo(a)","El/la novio(a)","El/la vecino(a)",
             "El mensajero","El extraño","El/la hermanastro(a)","El/la colega de trabajo"]
        arma=["Pistola","Cuchillo","Machete","Pala","Bate","Botella","Tubo","Cuerda"]
        motivo=["Venganza","Celos","Dinero","Accidente","Drogas","Robo"]
        pdc=["Cabeza","Pecho","Abdomen","Espalda","Piernas","Brazos"]
        lugar=["Sala","Comedor","Baño","Terraza","Cuarto","Garage","Patio","Balcón",
               "Cocina"]
        #4
        
        categ=[sospechoso,arma,motivo,pdc,lugar]
        #contiene las cartas de la solución generada
        sol=solucion
        #sugerencia del algoritmo
        sug=[]
        #contiene las posiciones de un elemento que es restriccion
        resActivas=[]
        #4+5
        if(mostrar==True):
            self.salida+="Solucion: "+str(sol)+"\n"#4
            #1+4
        #4+5+5
        a=0
        b=0
        c=0
        d=0
        e=0
        while(True):
            sug=[]
            eliminado=0
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
            if(mostrar==True):
                self.salida+="Sugerencia: "+str(sug)+"\n"
            if(sug==sol):
                if(mostrar==True):
                    self.salida+="Resultado: "+str(sug)+"\n"
                return 'exito'
            elif(e<len(categ[4]) and e!=len(categ[4])):
                eliminado=self.eliminar(categ,sug,sol)
                e+=1
            elif(d<len(categ[3]) and d!=len(categ[3])):
                eliminado=self.eliminar(categ,sug,sol)
                e=0
                d+=1
            elif(c<len(categ[2]) and c!=len(categ[2])):
                eliminado=self.eliminar(categ,sug,sol)
                e=0
                d=0
                c+=1
            elif(b<len(categ[1]) and c!=len(categ[1])):
                eliminado=self.eliminar(categ,sug,sol)
                e=0
                d=0
                c=0
                b+=1
            elif(a<len(categ[0]) and a!=len(categ[0])):
                eliminado=self.eliminar(categ,sug,sol)
                e=0
                d=0
                c=0
                b=0
                a+=1
            else:
                if(mostrar==True):
                    self.salida+="Fracaso"+"\n"
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

    def comprobarSol(self, res, sol):
        for i in range(len(res)):
            result=False
            #(n+1)
            for j in range(len(res[i])):
                #(n+1)*(n+1)
                if res[i][j] in sol:
                    result=True
                else:
                    result=False
                    break
                #1
            if result==True:
                return True
            #(n+1)*1+3
        return False
        #2+(n+1)*((n+1)+3)+1

    def eliminar(self, categ, sug, sol):
        eliminar=0
        while(True):
            #1+n*(2+1)
            eliminar=randrange(5)
            if not sug[eliminar] in sol:
                break
        elemento=sug[eliminar]
        #2+3n
        if(mostrar==True):
            self.salida+="Eliminado: "+str(elemento)+"\n"
        #8+3n
        if eliminar==0:
            categ[0].remove(elemento)
        elif eliminar==1:
            categ[1].remove(elemento)
        elif eliminar==2:
            categ[2].remove(elemento)
        elif eliminar==3:
            categ[3].remove(elemento)
        else:
            categ[4].remove(elemento)
        return eliminar
        #14+3n
    def crearSol(self, c):
        global solution
        solution=[]
        salida=[]
        for i in range(5):
            salida.append(c[i][randrange(len(c[i]))])
        return salida
            

    def crearRestric(self, c, r):
        global restrictedPairs
        restrictedPairs=[]
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

########################################################################### BACKTRACKING #########################################################################################
    def generateRestrictedPairs(self, pairAmount):
        """Generates the restricted pairs
        Args:
            pairAmount: Amount of restricted pairs
        """
        counter = 0
        while(counter < pairAmount):
            firstMid = cards[random.randint(0,len(cards) -1)][random.randint(0, len(cards[0]) -1)]
            secondMid = cards[random.randint(0,len(cards) -1)][random.randint(0, len(cards[0]) -1)] 
            if (checkPair(firstMid, secondMid)):
                restrictedPairs.append([firstMid, secondMid])
                counter += 1

    def checkPair(self, firstMid, secondMid):
        """
        Check if a generated pair is unique and does not belong to the 
        solution set
        Args:
            firstMid: First pair value
            secondMid: Second pair value
        
        Returns:
            True if the pair meets the requeriments, false otherwise
        """
        return (firstMid != secondMid and firstMid not in solution and
            secondMid not in solution and firstMid != "" and
            secondMid != "" and [firstMid, secondMid] not in restrictedPairs and
            [secondMid, firstMid] not in restrictedPairs)

    def checkRestriction(self, resultArray):
        """
        Check if the solution list contains a restriction
        Args:
            resultArray: list that contains the actual problem solution
        
        Returns:
            True if the solution list contains a restriction, False otherwise.
        """
        for pair in range(0, len(restrictedPairs)):
            if (restrictedPairs[pair][0] in resultArray and restrictedPairs[pair][1] in resultArray):
                return True
        return False

    def restrictCard(self, wrongSolution):
        """
        Choose a card from the wrong solution and add it to the restricted cards set
        Args:
            wrongSolution: list with the deeper backtracking solution
        """
        wrongSolution = self.difference(wrongSolution, solution)
        card = random.randint(0, len(wrongSolution) -1)
        if (wrongSolution[card] not in restringedCards):
            restringedCards.append(wrongSolution[card])

    def goBack(self, resultArray):
        """
        Check if it is necesary to go back in the search
        
        Args:
            resultArray: list with the actual problem solution
        
        Returns: True if it is necesary to go back, False otherwise
        """
        for card in range(0 , len(restringedCards)):
            if (restringedCards[card] in resultArray):
                return True

    def backtracking(self, isFound, index, column, resultArray):
        """
        Perfomrms the backtracking search
        Args:
            isFound: list with a unique value. Used to know if the solution was reached
            index: actual row of the cards matrix
            column: acutal column of the cards matrix
            resultArray: acutal problem solution
        """
        if(isFound[0] == True):
            return
        if (column >= len(cards[index]) ):
            self.restrictCard(resultArray)
            resultArray[column - 1] = ""
            return
        for row in range(0, len(cards)):
            if (isFound[0] == True):
                break
            if (cards[row][column] == "" ):
                return
            checkSol = resultArray
            checkSol[column] = ""
            if (self.goBack(checkSol)):
                resultArray[column] = ""
                return
            if (self.checkRestriction(resultArray)):
                resultArray[column] = ""
                return
            resultArray[column] = cards[row][column]
            
            #print(resultArray)
            if(mostrar==True):
                self.salida2+=str(resultArray)+"\n"
                
            if (resultArray == solution):
                
                #print("Solucion:", resultArray)
                if(mostrar==True):
                    self.salida2+="Solucion: "+str(resultArray)+"\n"
                    
                isFound[0] = True
                return
            else:
                self.backtracking(isFound, row, column + 1, resultArray)

    def difference(self, listA, listB):
        """
        Make the difference between list
        Used to know the wrong values in the actual solution
        Args:
            listA: minuend list
            listB: substrahend list
        Returns: listC the differece between lists
        """
        listC = []
        for element in listA:
            if element not in listB:
                listC.append(element)
        return listC

    def main():
        generateRestrictedPairs(4)
        backtracking([False], 0, 0, ["", "", "", "", ""])

    
ventana_principal=Tk()
progra=Interfaz(ventana_principal)
ventana_principal.mainloop()
