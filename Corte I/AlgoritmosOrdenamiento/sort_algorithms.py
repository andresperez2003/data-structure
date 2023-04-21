from random import sample 
from colorama import Fore, init
init()

class SortAlgorithm:

    def __init__(self):
        self.number_list = range(100)
        self.list_burble_sort = sample(self.number_list,8)
        self.list_select_sort = sample(self.number_list,8)
        self.list_insert_sort = sample(self.number_list,8)
        self.list_merge_sort = sample(self.number_list,8)
        self.list_quick_sort = sample(self.number_list,8)
        self.list_radix_sort = sample(self.number_list,8)

    # Burble sort
    def burble_sort_function(self):
        #comparacion por pares --> iniciamos comparando los 2 primeros de la lista
        print(Fore.CYAN  + "----------------------------------------" + Fore.RESET ) 
        print (Fore.GREEN + '       Ordenamiento burbuja' + Fore.RESET)
        #Crear contador para conocer la cantidad de elementos de la lista
        count_item_list = 0
        # Recorremos la lista self.list_burble_sort
        for i in self.list_burble_sort:
            #Al contador de elementos, cada que visitemos una posicion, le sumamos 1
            count_item_list+=1
        print("     >>>Iteracion interna del for <<<")
        #Recorremos la lista e iniciamos la comparacion de valor
        print(self.list_burble_sort)
        print("Primer for contando -1: ", count_item_list-1)
        for j in range(count_item_list-1):
            print(Fore.RED +f"{j}" + Fore.RESET)
            for k in range(count_item_list-j-1):
                print(Fore.BLUE + f"{k}" + Fore.RESET)
                #Comparamos el valor de la posicion actual con el valor de la siguiente posicion
                if self.list_burble_sort[k] > self.list_burble_sort[k+1]:
                    #Transposicion de valores
                    self.list_burble_sort[k], self.list_burble_sort[k+1] = self.list_burble_sort[k+1], self.list_burble_sort[k]
                print(self.list_burble_sort)
        print(self.list_burble_sort)

    def burble_sort_fuction_refactor(self):
        change_position = True
        while change_position:
            change_position = False
            for i in range(len(self.list_burble_sort)-1):
                if self.list_burble_sort[i]> self.list_burble_sort[i+1]:
                    self.list_burble_sort[i], self.list_burble_sort[i+1] = self.list_burble_sort[i+1], self.list_burble_sort[i]
                    change_position = True
        print(self.list_burble_sort)

    def select_sort_function(self):
        #Debemos 
        print(Fore.CYAN  + "----------------------------------------" + Fore.RESET ) 
        print (Fore.GREEN + '       Ordenamiento seleccion' + Fore.RESET)
        count_list_item = 0  
        #Inicializamos el contador   
        for i in self.list_select_sort:
            count_list_item+=1
        print(self.list_select_sort)
        #Recorremos laa lista y generamos la compraracion de valores entre posiciones
        for i in range(count_list_item):
            print(Fore.RED+ str(i) + Fore.RESET)
            min = i
            for j in range(min+1, count_list_item):
                print(Fore.BLUE+ str(j) + Fore.RESET)
                print("Comparando:" + Fore.BLUE + str(self.list_select_sort[min]) + " - "+  str(self.list_select_sort[j]) + Fore.RESET )
                #Comparacion de valores
                if self.list_select_sort[min]> self.list_select_sort[j]:
                    min = j
                    #Generamos el intercambio, la transposicion
                    #Cambiamos el elemento de menor valor de la lista con el primero
            self.list_select_sort[i] , self.list_select_sort[min] = self.list_select_sort[min], self.list_select_sort[i]
            print(self.list_select_sort)
        print(self.list_select_sort)

    def insertion_sort_function(self):
        print(self.list_insert_sort)
        #Separamos la lista en dos partes (puede o no estar ordenadas) ordenadas
        for i in range(1,len(self.list_insert_sort)):
            item_visited = self.list_insert_sort[i]
            #Visitamos la posicion anterior a la actual
            j= i-1
            #Todos los elementos de valor mayor pasan adelante
            while j >= 0 and self.list_insert_sort[j]> item_visited:
                print(Fore.CYAN + str(self.list_insert_sort[j])+ Fore.RESET+ " > "+ str(item_visited))
                self.list_insert_sort[j+1] = self.list_insert_sort[j]
                j-=1
            #Transposicion
            self.list_insert_sort[j+1] = item_visited
        print(self.list_insert_sort)

    def merge_sort_function(self, list):
        print(list)
        # En el caso de que el tamaño de la lista sea menor a 2, retornamos la lista (Esto pasa porque ya está ordenada, o se dividió hasta ser sólo 1 elemento)
        if len(list) < 2:
            return list
        # En el caso de que sea 2 o mayor, se divide de nuevo
        else:
            middle = len(list) // 2 # Divide y redondea hacia abajo el resultado
            right = self.merge_sort_function(list[:middle])
            left = self.merge_sort_function(list[middle:])
            return self.merge(right, left)
        
    # Función merge
    def merge(self, list1, list2):
        i, j = 0, 0 # Variables de incremento
        result = [] # Lista de resultado
        # Intercalar ordenadamente
        while(i < len(list1) and j < len(list2)):
            if (list1[i] < list2[j]):
                result.append(list1[i])
                i += 1
            else:
                result.append(list2[j])
                j += 1
        # Agregamos datos faltantes al resultado
        result += list1[i:]
        result += list2[j:]
        print(result)
        # Retornamos el resultados
        return result

    


