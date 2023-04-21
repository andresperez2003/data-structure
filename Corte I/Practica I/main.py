#Main class

#1. Importamos las clases
from activity_1 import ListPractice
from activity_2 import Activity2

user_name = 'DaRi'
#2.Creamos las instancias para ejecutar el metodo init de las clases
inst_list_practice = ListPractice()
inst_activity_2 = Activity2()

print(inst_list_practice.student_name)
""" 
inst_list_practice.show_info_list()
inst_list_practice.input_data_courses() """
print(user_name.lower())
print(user_name.upper())
print(user_name.capitalize())

