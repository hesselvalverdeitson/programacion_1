#listado cursos (agregar,modificar,eliminar)
#Del curso desea saber (nombre,instructor,aula y listado de Alumnos)
#Cuantos Alumnos están inscritos en el curso
#Modificar instructor, aula, dar de Alta alumnos y dar de baja alumnos
# Mostrar Listado de alumnos de un curso
#Interfaz atractiva y solo finalizar cuando ingrese salir
cursos=[]
while True:
    print("¿Que operación deceas realizar?")
    eleccion=input("""
agregar curso
modificar cursos
eliminar cursos
ver cursos
ver lista de alumnos
salir
""").lower().strip()
    if eleccion=="salir":
        break
    match eleccion:
        case "agregar curso":
            nombre=input("Dime el nombre del curso: ")
            instructor=input("Dime el nombre del instructor: ")
            aula=input("Dime el aula del curso: ")
            alumnos=[]
            while True:
                alumno=input("Dime el nombre del alumno (o 'fin' para terminar): ")
                if alumno.lower().strip() == 'fin':
                    break
                alumnos.append(alumno)
            curso={"nombre":nombre,"instructor":instructor,"aula":aula,"alumnos":alumnos,}
            cursos.append(curso)
            print(f"Curso {nombre} agregado exitosamente.")
        
        
        case "modificar cursos":
            nombre_curso=input("Dime el nombre del curso a modificar: ")
            for curso in cursos:
                if curso["nombre"].lower().strip() == nombre_curso.lower().strip():
                    print(f"Modificando curso: {curso['nombre']}")
                    nueva_instructor=input("Dime el nuevo instructor (o presiona Enter para no cambiar): ")
                    nuevo_aula=input("Dime el nuevo aula (o presiona Enter para no cambiar): ")
                    if nueva_instructor:
                        curso["instructor"]=nueva_instructor
                    if nuevo_aula:
                        curso["aula"]=nuevo_aula
                    while True:
                        accion_alumno=input("¿Deseas agregar o eliminar un alumno? (agregar/eliminar/modificar/fin): ").lower().strip()
                        if accion_alumno=="fin":
                            break
                        elif accion_alumno=="agregar":
                            nuevo_alumno=input("Dime el nombre del alumno a agregar: ")
                            curso["alumnos"].append(nuevo_alumno)
                        elif accion_alumno=="eliminar":
                            alumno_eliminar=input("Dime el nombre del alumno a eliminar: ")
                            if alumno_eliminar in curso["alumnos"]:
                                curso["alumnos"].remove(alumno_eliminar)
                       
                                
            
                        else:
                            print("Alumno no encontrado.")
                    print(f"Curso {curso['nombre']} modificado exitosamente.")
                    break
            else:
                print("Curso no encontrado.")
        case "eliminar cursos":
            nombre_curso=input("Dime el nombre del curso a eliminnar:")
            for curso in cursos:
                if curso["nombre"].lower().strip() == nombre_curso.lower().strip():
                    cursos.remove(curso)
                    print(f"Curso {nombre_curso} eliminado exitosamente.")
                    break
            else:
                print("Curso no encontrado.")
        case "ver cursos":
            print(cursos)
        case "ver lista de alumnos":
            nombre_curso=input("Dime el nombre del curso para ver la lista de alumnos:")
            for curso in cursos:
                if curso["nombre"].lower().strip() == nombre_curso.lower().strip():
                    print(f"Lista de alumnos en el curso {curso['nombre']}:")
                    for alumno in curso["alumnos"]:
                        print(alumno)
                    break
            else:
                print("Curso no encontrado.")
        case _:
            print ("opcion no valida")
            break
        
