'''
    Author: Andres Perez Ascanio
    Date: 25/01/2023
    Data type: list practice
'''

# 1. Declarar la clase
class ListPractice:
    #2. Crear funcion inicializadora de la clase 
    def __init__(self):
        #Definir las varaibles globales de la clase
        self.student_name = "Andres"
        self.courses_list=["POO", "TAD"]
    
    #3. Funcion customizada
    def show_info_list(self):
        #Imprimir el contenido de la lista courses_list
        print(self.courses_list)
        print(len(self.courses_list))

    #4. Funcion que solicita al usuario ingresar informacion
    def input_data_courses(self):
        #1. Declaramos una variable a nivel de metodo
        # Solicitud de texto
        print('Ingrese los siguientes datos: ')
        self.student_name = input('Nombre: ')
        #Solicitud de numeros
        course_number = int(input('Cantidad de asignaturas: '))
        #Validamos si el courses_number es menor al tamaño actual
        if course_number <= len(self.courses_list):
            print('>>> Error: Cursos a inscribir es menor a 2 <<<')
        else:
            #Solcitar nombre de las asginaturas al usuario
            for course in range(course_number-len(self.courses_list)):
                #Variables que almacena el nombre de la asignatura
                course_name = str(input( 'Nombre asignatura: '))
                if course_name in self.courses_list:
                    print("La materia ya esta guardada")
                else:
                    self.courses_list.append(course_name)
        print(self.courses_list)



