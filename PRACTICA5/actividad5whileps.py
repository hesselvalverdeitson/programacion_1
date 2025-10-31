while True:
 saldo=int(input("Cuanto dinero desea invertir en cripto"))
 numeroinvertido= int(input("dinero invertido"))
 if saldo >0:
  totalinvertido= 0
  totalinvertido=totalinvertido+1
  inverti= saldo-numeroinvertido
  print ("Tu saldo restante es de", inverti)
  print ("compras exitosas",totalinvertido)
 elif numeroinvertido > saldo:
  print ("Compra no realizada")
  

 else:
  print("Saldo insuficiciente")
  break