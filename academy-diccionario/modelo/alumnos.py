def agregarAlumno():
    alumnos={
        "Alumnos":{},
    }
    while True:
        alumno=input("Dime el nombre del alumno (o 'fin' para terminar): ")
        idalumno=input("Dime el id del alumno")
            if alumno.lower().strip() == 'fin':
                break
    return alumnos