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
            print(cursos)
        case "agregar alumno":
            nuevoAlumno= agregarAlumno()
            print(nuevoAlumno)




    

