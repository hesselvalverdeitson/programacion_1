while True:
 print("calculadora interactiva")
 numero1=int(input("numero inicial de la operación"))
 numero2=int(input("numero secundario de la operación"))
 opcion=input(""""
  sumar
  restar
  multiplicar
  dividir
  salir
 """)

 match opcion:
  case "sumar":
   suma1=numero1+numero2
   print("Tu suma es de",suma1)
  case "restar":
   resta1= numero1+numero2
   print("Tu resta es de",resta1)
  case "multiplicar":
   multiplica1=numero1*numero2
   print("Tu multiplicación es de",multiplica1)
  case "dividir":
   dividir1=numero1/numero2
   print("Tu multiplicación es de",dividir1)
  case "salir":
   print ("gracias por usar la calculadora interactiva")
   break 