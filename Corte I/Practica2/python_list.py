'''
    List methods
    Date: 27/01/23
'''

class ListMethods:
    def __init__(self):
        #Definimos una lista vacia
        self.pets = []
        self.vehicles = list()

    #2. Metodo para añadir elementos a la  lista
    def add_list_elements(self):
        #['dog','cat']
        self.pets.append('dog')
        self.pets.append('cat')
        print(self.pets)

    #3. Metodo que solicita metodos al usuario
    def input_data_vehicle(self):
        #Variables locales: vehicles_number, vehicle_type
        vehicles_number = int(input("Cuantos vehiculos tienes: "))
        #Recorrer la lista
        for vehicle_item in range (vehicles_number):
            vehicle_type = str(input('Tipo de vehiculo: '))
            self.vehicles.append(vehicle_type)
        print(self.vehicles)
        #Imprimir ultimo elemento, penultimo y antepenultimo de la lista
    # Descomentar
    # print(self.vehicles[-1], self.vehicles[-2], self.vehicles[-3])


    #4. Extraer valores de una lista
    def show_collection_data_list(self):
        #Imprimir desde posicion 2 hasta 3
        print(self.vehicles[2:4])
        #Todos los elementos de la lista
        print(self.vehicles[:])
        #Elementos desde un indice especifico
        print(self.vehicles[2:])
        #Elementos hasta unn indice especifico
        print(self.vehicles[:2])
        #Acceder a los elementos de 2 en 2
        print(self.vehicles[::2])
        #Acceder a un SUBCONJUNTO de elementos de 2 en 2
        print(self.vehicles[1:5:2])

    #5. Iterar los elementos de una lista con for
    def iteration_list(self):
        for item in self.vehicles:
            print(item)
            #Validar si la lista contiene un valor especifico
        if "carro".capitalize() in self.vehicles:
            print("Si se encontro valor")
        else:
            print("No se en encontro el valor")
    
    #6. Añadir varios elementos al final de la lista
    def add_elements(self):
        self.vehicles.extend(['Avion', 'TractoMula', 'Otro medio'])
        print(self.vehicles)

    #7. Añadir un elemento en posicion especifica de la lista
    def add_specific_element(self):
        self.vehicles.insert(0, 'Moto')
        print(self.vehicles)

    #8. Eliminar ultimo elemento de la lista
    def remove_last_element(self):
        self.vehicles.pop()
        print(self.vehicles)

    #9. Eliminar elemento de posicion especifica
    def remove_specific_element(self):
        self.vehicles.pop(0)
        print(self.vehicles)

    #10. Eliminar todos los elementos de la lista
    def remove_all_elements(self):
        self.vehicles.clear()
        print(self.vehicles) 
    #11. Eliminar un valor especifico: }
    def remove_specific_element(self):
        self.vehicles.remove("Tractomula".capitalize())
        print(self.vehicles)

    #12. Eliminar todas las coincidencias de valor en la lista
    def remove_all_elements_match(self):
        newList = list(filter("Tractomula".__ne__,self.vehicles))
        print(newList)
    
