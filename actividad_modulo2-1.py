palabra=input("hola introduce una palabra: ")


if len(palabra) < 4 :
  print( "la frase  es muy corta  faltan  ", (4)-len(palabra) ,"letras para el minimo de letras admitidas " )
  

elif len(palabra)  > 8 :
    print("la palabra es muy grande sobran ",len(palabra)-(8), "letras" )
      
elif len(palabra)  <= 8 and  len(palabra)>= 4 :
    print("palabra corecta") 
    
else :
  print("caracteres incorrestos")   
    

