#Mi programa de calculo de indice de masa corporal
print("Hola , con este progrma podras calcular tu IMC")
nombre=input("introduce tu nombre : ")
apellido_paterno=input("introduce tu apellido paterno : ")
apellido_materno =input("introduce tu apellido materno : ")
edad=int(input("dime  tu edad : "))
estatura=float(input("dime tu estatura en metros : "))
peso=int(input("dime tu peso : "))

imc=peso/(estatura**2)
print(nombre.capitalize() ,apellido_paterno.capitalize(),apellido_materno.capitalize(), )
print("Edad",edad)
        
print("Tienes un  IMC de : ")

print(imc)


