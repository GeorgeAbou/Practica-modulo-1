#Mi programa de calculo de indice de masa corporal

#se proceden a obtener  los datos del usuario dependiendo de la necesidad del formato
print("Hola , con este progrma podras calcular tu IMC , recuerda introducir los datos de acuerdo al formato solicitado")
nombre=input("introduce tu nombre : ")
apellido_paterno=input("introduce tu apellido paterno : ")
apellido_materno =input("introduce tu apellido materno : ")
edad=int(input("dime  tu edad : "))
estatura=float(input("dime tu estatura en metros : "))
peso=int(input("dime tu peso en kilogramos : "))

#se calcula el imc de acurdo a la formula indicada 
imc=peso/(estatura**2)
print(nombre.capitalize() ,apellido_paterno.capitalize(),apellido_materno.capitalize(), )

#se usa condicional para ver si es mayor de edad
if (edad>=18 ) :    
   print("Eres mayor de edad") 

if (edad<18):   
   print("menor de edad") 

print("Tu IMC es : ", imc)
# se usa las condiconal if y elif  para saber el estado de salud de las personas dependiendo de su imc    
if imc>=0.00 and imc<=15.99 :
   print("Tienes delgadez severa")
elif imc>=16.00 and imc<= 16.99:
   print("Tienes Delgadez moderada")
elif imc >=17.00 and imc <=18.49:
   print("Tienes Delgadez leve") 
elif imc>=18.50 and imc<=24.99:
   print("Muy bien estas Normal")
elif imc>=25.00 and imc<=29.99 :
   print("Tienes Obesidad leve")
elif imc>=30.00 and imc <=34.99:
   print("Tienes Obesidad moderada")
elif imc>=35.00 and imc <=39.99 :
   print("Tienes Obesidad media") 
elif imc>=40.00 :
   print("Tienes Obesidad morbida") 

print("Gracias por usar nuestro programa")

