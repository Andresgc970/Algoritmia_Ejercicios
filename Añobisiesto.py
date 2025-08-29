#Nombre: Programa que determina si un año es bisiesto o no.

#Entrada: Variable Tipo entero (año)   
#	Nombre  : Andres Felipe 
#	Apellido: Guavita Cardenas

#Salida:
# Se valida si el año es bisisesto o no

#Proceso solicita que se ingrese un año y no obstante verifica si el año cumple las caracteristicas para 
# ser bisiesto

año=int(input("Digite un año"))




if (año % 4 == 0 and año % 100 != 0) or (año % 400 == 0):
    print("El año es bisiesto")
else:
    print ("El año no es bisiesto")    

