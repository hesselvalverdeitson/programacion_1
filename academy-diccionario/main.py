import modelo.curso
from modelo.curso import agregarCursos
from modelo.alumnos import agregarAlumno
while True:
    cursos={}
    acciones=(input("""¿Qué acción deseas realizar? 
Agregar curso   
Agregar alumno
Salir  """)).lower().strip()
    if acciones == "salir":
        print("Gracias por usar la app")
        break
    match acciones:
        case "agregar curso":
            cursos=agregarCursos()
        case "agregar alumno":
            idalumno=int(input("Dime el id del alumno"))
            nuevoAlumno= agregarAlumno()
            cursos["nombre"]["alumnos"][idalumno]=nuevoAlumno
            print(nuevoAlumno)




    

