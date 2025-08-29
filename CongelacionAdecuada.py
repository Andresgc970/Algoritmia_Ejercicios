#Nombre: Programa que determina si al ingresar una temperatura es adecuada para congelar.

#Entrada: Variable tipo real (temperatura)  
#	Nombre  : Andres Felipe 
#	Apellido:Guavita Cardenas

#Salida:
# Se valida si la temperatura ingresada es adecuada para congelar.

#Proceso solicita que se ingrese una temperatura la cual si es menor o igual a 0 sera adecuada para congelar del caso
#contrario el sistema informara que no es adecuda.

temperatura=float(input("Ingrese la teperatura actual"))

if temperatura <= 0:
  print("La temperatura es adecuada Para congelar")
else:
  print("La temperatura no es adecuada")  