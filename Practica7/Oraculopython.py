def calcular_elemento(año):

 ultimo_digito=año%10
 if ultimo_digito==0 or ultimo_digito == 1:
   return "Metal"
 elif ultimo_digito==2 or ultimo_digito == 3:
   return "Agua"
 elif ultimo_digito==4 or ultimo_digito == 5:
   return "Madera"
 elif ultimo_digito==6 or ultimo_digito == 7:
   return "Fuego"
 elif ultimo_digito==8 or ultimo_digito == 9:
  return "Tierra"

def iniciar_oraculo():
 while True:
    print("¿Deseas conocer tu destino?")
    destino=input(""""
    si
    no
    """).lower().strip() 
    match destino:
        case "si":
         print("Que asi sea")
        case "no":
         print("Sigue tu camino")
         break
    nombre=input("Dime tu nombre:")                                                                      
    año_nacimiento=int(input("Dime tu año de nacimiento:"))
    Numero_suerte=(input("Dime un numero entre 1 y 4:"))
    elemento=calcular_elemento(año_nacimiento)
    match Numero_suerte:
      case "1":
        print(f"*****Tu afinidad con el elemento {elemento},{nombre} te traera buena fortuna en el ambiente laboral***** ")
      case "2":
        print(f"*****Tu afinidad con el elemento {elemento},{nombre} te traera buena salud***** ")
      case "3":
        print(f"*****Tu afinidad con el elemento {elemento},{nombre} te traera buena suerte en el amor***** ")
      case "4":
        print(f"*****Tu afinidad con el elemento {elemento},{nombre} te traera buena fortuna a tus familiares***** ")
    
iniciar_oraculo()


