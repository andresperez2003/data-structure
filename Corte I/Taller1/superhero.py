'''
    Author: Andres Perez
    Date: 7/02/2023
'''
from colorama import *


class SuperHero:
    
    def __init__(self):
        self.mundo=0
        ###Objetos de prueba DC
        self.DC=[
        ("Batman", ["Dinero", "Armadura"],["Stan lee"]), 
        ("Flash",["SuperVelocidad"],["Stan lee","Salome"])]

        self.opcion=0
        ###Objetos de prueba Marvel
        self.Marvel = [
        ("Spiderman",["Telaraña"],["Stanlee","Andres"]),
        ("Iron man", ["Dinero", "Armadura"], ["Stan lee", "Darihana"]),
        ("Hulk",["Fuerza"],["Stan lee"])
        ]

        self.cantidad_super_heroes=0
        self.nombre_super_heroe =""
        self.super_poderes=[]
        self.creadores=[]

    #### Imprimir las operaciones que puede hacer el usuari0
    def imprimir_operaciones(self):
        print(Fore.GREEN,"\n     >>> Menu de Operaciones <<< \n")
        print(Fore.RESET,"    1. Agregar Superheroe\n     2. Buscar Superheroe\n     3. Eliminar Superheroe\n     4. SuperHeroe mas superpoderes\n     5. Superheroe menos superdores\n     6. Unir Mundos\n     7. Salir\n")


    ### Aqui el usuario seleccionar que operacion desea realizar
    def inicio(self):
        while True:
            try:
                ### Opciones para el usuario
                self.imprimir_operaciones()
                self.opcion = int(input(">>> Ingrese la operacion que desea realizar "))
                # opciones del 1 al 5 se llaman desde el mismo metodo
                if(self.opcion >= 1 and self.opcion <=5):
                    self.menu_incio()
                ### opcion 6 a la funcion para unir a Marvel o DC
                elif self.opcion==6:
                    self.unir_marve_dc()
                ### Opcion para terminar el programa
                elif self.opcion == 7:
                    print("Hasta Pronto")
                    break
            except ValueError:
                print(">>> ERROR <<<")
                self.imprimir_operaciones()

    ### Menu de inicio posterior a la eleccion de la operacion que el usuario desea realizar, ademas
    ### el usuario debe seleccionar el mundo donde van a ser las operaciones
    def menu_incio(self):
        while True:
            try:
                print(Fore.GREEN,"\n     >>> Menu de Mundos <<< ")
                print(Fore.RESET,"   \n     1. Marvel\n     2. DC\n     3. Volver\n")
                self.mundo = int(input(">>> Ingrese una opción: "))
                ### Mundo marvel
                if self.mundo==1:
                    ### Agregar un nuevo superheroe en Marvel
                    if(self.opcion == 1):
                        cant_superheroes = int(input(">>> Ingrese la cantidad de superheroes a agregar "))
                        for i in range (cant_superheroes):
                            self.estructura_nuevo_superheroe()
                            self.Marvel.append((self.nombre_super_heroe.capitalize(),self.super_poderes,self.creadores))
                            print("\n Nueva lista de Marvel\n")
                            print(self.Marvel)
                            print("\n")
                        break
                    ### Buscar el superheroe en Marvel
                    elif self.opcion==2 :
                        self.buscar_superheroe()
                        break
                    ### Eliminar el superheroe en Marvel
                    elif self.opcion == 3:
                        self.eliminar_superheroe()
                        print(self.Marvel)
                        break
                    elif self.opcion ==4:
                    ### Mas superpoderes Marvel
                        self.mayor_superpoderes()
                        break
                    elif self.opcion == 5:
                    ### Menos superpoderes Marvel
                        self.menor_superpoderes()
                    elif self.opcion == 7:
                        break

                ### DC
                if self.mundo == 2:
                    ### Agregar un nuevo superheroe en Marvel
                    if(self.opcion == 1):
                        cant_superheroes = int(input(">>> Ingrese la cantidad de superheroes a agregar "))
                        for i in range (cant_superheroes):
                            self.estructura_nuevo_superheroe()
                            self.DC.append((self.nombre_super_heroe.capitalize(),self.super_poderes,self.creadores))
                            print(self.DC)
                            print("\n Nueva lista de DC\n")
                            print(self.DC)
                            print("\n")
                            break
                    ### Buscar un superheroe DC
                    elif self.opcion ==2:
                        self.buscar_superheroe()
                        break
                    ### Eliminar un superheroe DC
                    elif self.opcion == 3:
                        self.eliminar_superheroe()
                        print(self.DC)
                        break
                    ### Superheroe de DC con mas superpoderes
                    elif self.opcion == 4:
                        self.mayor_superpoderes()
                    ### Superheroe de DC con menos superpoderes
                    elif self.opcion == 5:
                        self.menor_superpoderes()
                        break
                ### Devolveres al menu de operaciones
                if self.mundo == 3:
                    break
                else:
                    print(">>> Opcion incorrecta <<<")
            except ValueError:
                print(">>> ERROR <<<")
                break

    ### Estructura para crear un nuevo superhoeroe
    def estructura_nuevo_superheroe(self):
        self.super_poderes=[]
        self.creadores=[]
        print(Fore.GREEN,"\n   ****  Creacion de nuevo superheroe ****\n", Fore.RESET)
        ### Nombre Superheroe
        self.nombre_super_heroe = input(">>> Ingrese el nombre del superHeroe ")
        cantidadSuperpoderes=int(input(">>> Ingrese la cantidad de superpoderes "))
        ### Agregar los superpoderes al superheroe
        for i in range (cantidadSuperpoderes):
            superpoder = input(">>> Ingrese el nombre del poder ")
            self.super_poderes.append(superpoder)
        cantidadAutores = int(input(">>> Ingrese la cantidad de autores "))
        ### Agregar los autores al superheroe
        for i in range(cantidadAutores):
            autor = input(">>> Ingrese el nombre del autor ")
            self.creadores.append(autor)
        

    def solicitar_datos(self):
        ### Solicitarle al usuario cuantas veces desea 
        self.cantidad_super_heroes = int(input(">>> Cuantos superHeroes desea añadir \n"))
        for i in range (self.cantidad_super_heroes):
            self.estructura_nuevo_superheroe()


    ### Buscar Superheroes con el nombre
    def buscar_superheroe(self):
        ### Hacer la busqueda dentro del mundo de Marvel
        if self.mundo ==1:
            self.encontrado=False
            self.nombre_super_heroe = input(">>> Ingrese el superheroe a buscar ")
            ### Buscando el heroe por el nombre
            for superHeroe in self.Marvel:
                if(self.nombre_super_heroe.capitalize() == superHeroe[0]):
                    ### Si lo encuentra, imprime sus superpoderes
                    print("\n***  Superpoderes " + f'{superHeroe[1]} ***')
                    self.encontrado=True
            ### Al final de todo el ciclo, si no lo encuentra, le da la opcion al usuario de crear el superheroe
            if not self.encontrado:
                respuesta = input(">>> ¿Desea ingresar el superheroe? ")
                ### Validaciones
                if respuesta.lower() == 'si':
                    self.estructura_nuevo_superheroe()
                elif respuesta.lower() =='no':
                    print("Vuelva pronto")
                else:
                    print("Respuesta no valida")  
        ### Hacer la busqueda dentro del mundo de DC
        elif self.mundo == 2:
            self.encontrado=False
            self.nombre_super_heroe = input(">>> Ingrese el superheroe a buscar ")
            ### Buscando el heroe por el nombre
            for superHeroe in self.DC:
                if(self.nombre_super_heroe.capitalize() == superHeroe[0]): 
                    ### Si lo encuentra, imprime sus superpoderes              
                    print("\n*** Superpoderes" + f'{superHeroe[1]} ***')
                    self.encontrado=True
            ### Al final de todo el ciclo, si no lo encuentra, le da la opcion al usuario de crear el superheroe
            if not self.encontrado:
                respuesta = input(">>> Desea ingresar el superheroe? ")
                ### Validaciones
                if respuesta.lower() == 'si':
                    self.estructura_nuevo_superheroe()
                elif respuesta.lower() =='no':
                    print("Vuelva pronto")
                else:
                    print(">>> Respuesta no valida")  

        
        

    ### Funcion para eliminar un superheroe
    def eliminar_superheroe(self):

        ### Comprobacion para que elimine en la lista de Marvel
        if self.mundo == 1:
            self.encontrado=False
            self.nombre_super_heroe = input(">>> Ingrese el nombre del superheroe ")
            ### Buscando el superheroe para eliminarlo
            for superHeroe in self.Marvel:
                if(self.nombre_super_heroe.capitalize() == superHeroe[0]):
                    print('removido')
                    self.Marvel.remove(superHeroe)
                    self.encontrado=True
            ### Si no lo encuentra, no permite eliminar el superheroe
            if(not self.encontrado):
                print(">>> No se encontro el superheroe")
        
        ### Comprobacion para que elimine en la lista de DC
        elif self.mundo == 2:
            self.encontrado=False
            self.nombre_super_heroe = input(">>> Ingrese el nombre del superheroe ")
            ### Buscando el superheroe para eliminarlo
            for superHeroe in self.DC:
                if(self.nombre_super_heroe.capitalize() == superHeroe[0]):
                    print('removido')
                    self.DC.remove(superHeroe)
                    self.encontrado=True
            ### Si no lo encuentra, no permite eliminar el superheroe
            if(not self.encontrado):
                print(">>> No se encontro el superheroe")

    def mayor_superpoderes(self):
        cantidad_superpoderes=float('-inf')
        if self.mundo == 1:
            for superHeroe in self.Marvel:
                if(len(superHeroe[1])>cantidad_superpoderes):
                    cantidad_superpoderes = len(superHeroe[1])
                    self.nombre_super_heroe = superHeroe[0]
            print("\nSuperheroe con mas superpoderes "+ self.nombre_super_heroe)
        elif self.mundo ==2 :
            for superHeroe in self.DC:
                if(len(superHeroe[1])>cantidad_superpoderes):
                    cantidad_superpoderes = len(superHeroe[1])
                    self.nombre_super_heroe = superHeroe[0]
            print("\nSuperheroe con mas superpoderes "+ self.nombre_super_heroe)

    ### Funcion para comprobar el heroe con menos superpoderes
    def menor_superpoderes(self):
        cantidad_superpoderes=float('inf')

        ### Comprobacion para que ejecute la funcion solo en Marvel
        if self.mundo == 1:
            for superHeroe in self.Marvel:
                if(len(superHeroe[1])<cantidad_superpoderes):
                    cantidad_superpoderes = len(superHeroe[1])
                    self.nombre_super_heroe = superHeroe[0]
            print("\nSuperheroe con menos superpoderes" + self.nombre_super_heroe)

        ### Comprobacion para que ejecute la funcion solo en Marvel
        elif self.mundo ==2:
            for superHeroe in self.DC:
                if(len(superHeroe[1])<cantidad_superpoderes):
                    cantidad_superpoderes = len(superHeroe[1])
                    self.nombre_super_heroe = superHeroe[0]
            print("\nSuperheroe con menos superpoderes "+ self.nombre_super_heroe)

    ### Funcion para unir las listas de Marvel y Dc
    def unir_marve_dc(self):
        self.Marvel.extend(self.DC)
        print(self.Marvel)


