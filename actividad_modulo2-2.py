print("hola, con este programa podras clacular el cuadrante mediante los datos de los ejes de coordenadas")
eje_x= int(input("ingrese valor del eje x de las coordenadas : "))
eje_Y= int(input("ingrese valor del eje y de las coordenadas"))
coordenada=[eje_x,eje_Y]
print("las coordenadas son :", coordenada)

if eje_x >0 and eje_Y >0 :
    print("estas en el cuadrante I")
elif eje_x <0 and eje_Y >0 :
    print: ("estas en el cuadrante  II ")
elif eje_x>0 and eje_Y<0 :
    print("estas en el cuadrante IV")  
elif eje_x<0 and eje_Y<0 :
    print("estas en el cuadrante III")      
