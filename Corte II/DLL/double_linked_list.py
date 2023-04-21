import time

from memory_profiler import memory_usage

class Node:
    def __init__(self,data):
        self.data= data
        self.next = None
        self.prev = None

class DoubleLinkedList:
    def __init__(self):
        self.head= None
        self.tail= None
        self.length = 0


    def print_list(self):
        if self.head is None:
            return
        current = self.head
        while current is not None:
            #current.data obtiene el valor del nodo visitado
            # end =" " end=" | " end=" , "
            print(current.data, end=" | ")
            current = current.next

    def add_node_at_end(self,data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
            #current = self.head
            #Recorremos la lista hasta el final
            #while current.next is not None:
                #Visitando al nodo siguientes
                #current = current.next
            # Generando los dos enlances del nuevo nodo (next | prev)
            #current.next = new_node
            #current.prev = current
        self.length +=1

    def add_node_at_start(self,data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        self.length+=1

    def add_node_in_position(self,position,data):
        if position < 0 or position >self.length:
            raise IndexError("Posicion fuera de rango")
        new_node = Node(data)
        if position ==0:
            self.add_node_at_start(data)
        elif position == self.length+1:
            self.add_node_at_end(data)
        else:
            current_node = self.head
            for i in range(position-1):
                current_node = current_node.next
            new_node.next = current_node.next
            new_node.prev = current_node
            current_node.next.prev = new_node
            current_node.next = new_node
            self.length +=1

    def remove_node_at_start(self):
        if self.head is None:
            return
        else:
            self.head = self.head.next
            if self.head is not None:
                self.head.prev = None
        self.length -=1

    def remove_node_at_end(self):
        if self.head is None:
            return
        elif self.head.next is None:
            self.head = None
        else:
            print(self.head.data)
            current = self.head
            while current.next is not None:
                current = current.next
            current.prev.next = None
        self.length-=1


    def remove_node_by_position(self,position):
        if position<1 or position>self.length+1 :
            raise IndexError("Posicion fuera de rango")
        if position == 1:
            self.remove_node_at_start()
        elif position == self.length:
            self.remove_node_at_end
        else:
            current_node = self.head
            for i in range(1,position):
                current_node = current_node.next
            current_node.prev.next = current_node.next
            current_node.next.prev = current_node.prev
            self.length-=1

    def remove_node_by_value(self,data):
        if self.head == None:
            return
        if self.head.data == data:
            self.remove_node_at_start()
        current = self.head
        while current is not None:
            if current.data == data:
                if current.next is not None:
                    current.next.prev = current.prev
                current.prev.next = current.next
                return
            current=current.next
            self.length-=1 
        """    # Opcion mejorada de martin
        index = self.get_node_by_value(data)
        if self.head == None:
            return
        elif self.head.data == data:
            self.remove_node_at_start()
        elif index == -1:
            print("No encontrado")
        else:
            self.remove_node_by_position(index) """

        

    def get_node_at_index(self,position):
        if position<1 or position>self.length:
            return -1
        if self.head is None:
            return None
        current = self.head
        i = 1
        while current is not None and i<position:
            current = current.next
            i+=1
        return current.data
    
    def get_node_by_value(self,data):
        if self.head is None:
            return None
        current = self.head
        index = 1
        while current.data is not data:
            index+=1
            current= current.next
            if current.next is not None:
                current = current.next
            else:
                return -1
        return current

    def update_node_at_index(self,position,data):
        if position<1 or position>self.length:
            return None
        if self.head is None:
            return
        current = self.head
        i=1
        while current is not None and i<position:
            current= current.next
            i+=1
        if current is not None:
            current.data = data
    
    def update_node_by_value(self,old_data,new_data):
        if self.head is None:
            return
        current = self.head
        while current is not None:
            if current.data == old_data:
                current.data = new_data
                return print(current.data)
            current = current.next
    
    def sort_asc(self):
        if self.head is None:
            return 
        current= self.head
        while current.next is not None:
            next_node = current.next
            while next_node is not None:
                if current.data > next_node.data:
                    current.data,next_node.data = next_node.data, current.data
                next_node = next_node.next
            current = current.next

    def has_duplicates(self):
        if self.head is None:
            return
        current = self.head
        values = set()
        while current is not None:
            if current.data in values:
                print("Duplicados")
            values.add(current.data)
            current=current.next
        print(values)
        return print('No duplicados')
    
    def has_duplicates_with_information(self):
        if self.head is None:
            return 
        current = self.head
        values ={}
        found_duplicates = False
        while current is not None:
            print(current.data)
            if current.data in values:
                values[current.data].append(current)
                found_duplicates = True
            else:
                values[current.data]= [current]
            current = current.next

        if found_duplicates:
            message = "The duplicates values are : \n"
            for value, nodes in values.items():
                if len(nodes)>1:
                    print(value)
                    message+= f" {value}: {len(nodes)} veces en los nodos "
                    message += ", ".join([str(node) for node in nodes]) + " \n"
            print(message)
            return True
        else:
            return False

        print(values)
    
    def calculate_complexity(self, func):
        # Ejecutar la función una vez para que se compile
        func(0)

        # Calcular tiempo de ejecución
        start_time = time.time()
        func(0)
        end_time = time.time()
        exec_time = end_time - start_time

        # Calcular uso de memoria
        mem_usage = max(memory_usage((func, (0,)), interval=0.1))

        # Imprimir resultados

        print("------------------ CALCULANDO COMPLEJIDAD -----------------")
        """ print(f"Función {func.name}:") """
        print(f"Tiempo inicio : {start_time}")
        print(f"Tiempo de finalizacion : {end_time}")
        print(f"Tiempo de ejecución: {exec_time:.6f} segundos")
        print(f"Uso máximo de memoria: {mem_usage:.6f} MB")
        print("------------------------------------")