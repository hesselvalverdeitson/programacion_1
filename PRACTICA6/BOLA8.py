import random
while True:
    def bola_8():
        input("Di tu pregunta a bola 8.\t").lower().strip()
        Aleatorio=random.randint(1,20)
        match Aleatorio:
            case 1:
                print("Es cierto")
            case 2:
                print("Es decididamente así")
            case 3:
                print("Sin lugar a dudas.")
            case 4:
                print("Puedes confiar en ello")
            case 5:
                print("Como yo lo veo, sí")
            case 6:
                print("Sí, definitivamente.")
            case 7:
                print("Lo más probable")
            case 8:
                print("Perspectiva buena.")
            case 9:
                print("Las señales apuntan a que sí")
            case 10:
                print("Respuesta confusa, vuelve a intentarlo")
            case 12:
                print("Vuelve a preguntar más tarde.")
            case 13:
                print("Mejor no decirte ahora.")
            case 14:
                print("No se puede predecir ahora")
            case 15:
                print("Concéntrate y vuelve a preguntar")
            case 16:
                print("No cuentes con ello")
            case 17:
                print("Mi respuesta es no")
            case 18:
                print("Mis fuentes dicen que no")
            case 19:
                print("las perspectivas no son muy buenas")
            case 20:
                print("Muy dudoso.")
    bola_8()         