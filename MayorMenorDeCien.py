#Nombre: Programa que determina si el numero ingresado es mayor a cien y menor a menor a menos cien

#Entrada: Variable Tipo Entero (num1) 
#	Nombre  : Andres Felipe 
#	Apellido:Guavita Cardenas

#Salida Se informa si el numero ingresado es mayor a cien o menor de menos cien

#Proceso si el numero ingresado es mayor de 100 se dara como resultado que el numero es mayor, si el numero ingresado
# es menor a menos cien se dara como resulatdo que el numero es menor a menos cien en el caso que se ingrese un valor
#fuera de ese rango se arrojara otro mensaje informandolo

num1=int(input("Ingrese un numero"))
if num1>100:
   print("El numero es mayor a 100")
elif num1<-100:
   print("El numero es menor a -100")
else:
    print("El numero ingresado no es menor a -100 ni mayor a 100")  