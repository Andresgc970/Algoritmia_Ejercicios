#Nombre: Programa que determina si un estudiante paso un examen

#Entrada: Variable Tipo Entero (nota) 
#	Nombre  : Andres Felipe 
#	Apellido:Guavita Cardenas

   #Salida
    #Da el resultado de si aprobo la nota o si no aprobo

#Proceso: pide la nota, verifica si le alcanza para pasar, si se ingresa un numero fuera del rango 
# lo informa

nota=float(input("Ingrese su nota")) 

if nota < 0 or nota > 100:
    print("Nota inválida, debe estar entre 0 y 100")
elif nota >= 60:
    print("Aprobo el examen")
else:
    print("Desaprobo El examen")   

 