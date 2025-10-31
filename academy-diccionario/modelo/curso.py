
def agregarCursos():
    curso={
        "nombre":input("Dime el nombre del curso: "),
        "instructor":input("Dime el nombre del instructor: "),
        "aula":input("Dime el aula del curso: "),
        "alumnos":{}
    }
    while True:
        alumno=input("Dime el nombre del alumno (o 'fin' para terminar): ")
        idalumno=input("Dime el id del alumno")
        if alumno.lower().strip() == 'fin':
                break
        curso["alumnos"][idalumno]["nombre"]=alumno
        curso={"nombre","instructor","aula","alumnos"}
        
        
        

    return curso