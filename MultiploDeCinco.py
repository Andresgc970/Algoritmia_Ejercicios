#Nombre: Programa que determina si un numero es multiplo de 5.

#Entrada: Variable Tipo entero (num1)  
#	Nombre  : Andres Felipe 
#	Apellido:Guavita Cardenas

#Salida Se informa si el numero ingresado es multiplo de 5 o no

#Proceso si el numero ingresado se divide entre 5  y su residuo es 0, cuenta como multiplo de 5

num1=int(input("Digite un numero: "))


if num1 % 5 == 0:
    print("El numero es multiplo de 5")
else:
    print("El numero no es multiplo de 5")

   
