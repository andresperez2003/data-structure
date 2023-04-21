class TupleList:
    def __init__(self):
        self.countres_list = []
        self.country_name = ""
        self.population = 0
        self.continent = ""

    #Funcion que solicita al usuario numero de paises a crear
    def total_countries(self):
        print("Ingresa la siguientes informacion: ")
        print(" ================================= ")
        while True:
            try:
                number_countries = int(input("Cantidad a añadir: ")) 
                for i in range(number_countries):
                    self.country_name = input(' >> Pais ')
                    self.continent = input(' >> Continent ') 
                    while True:
                        try:
                            self.population = int(input(' >> Population '))
                            print('------------------------------------------')
                            #Agregamos una tupla a la lista de paises
                            self.countres_list.append((self.country_name,self.population, self.continent))
                            break
                        except ValueError:
                            print(">> Se esperaba un numero <<")
                print(self.countres_list)
            except ValueError:
                print(" >> Error en el tipo de dato suministrado")
