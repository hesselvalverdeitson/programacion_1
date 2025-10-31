import string
def cifrar_mensaje():
 while True:
    print("¿Que operación deceas realizar?")
    cifrar_eleccion=input("""
     Cifrar
     Descifrar
     Salir
     """).lower().strip()
    if cifrar_eleccion=="salir":
       break
    match cifrar_eleccion:
        case "Salir":
            print("gracias, vuelva pronto")
            
        case "Cifrar":
            print (mensaje)
    mensaje=input("Dime tu mensaje")
    clave=int(input("Dime la clave"))

cifrar_mensaje()