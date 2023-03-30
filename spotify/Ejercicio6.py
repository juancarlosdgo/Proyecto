Asignaturas=["Matemáticas","Física","Química","Historia","Lengua"]
aprobado=[]
for asignatura in Asignaturas:
    nota=float(input("Ingrese nota: "))
    if nota>=5:
        aprobado.append(asignatura)
for asignatura in aprobado:
        Asignaturas.remove(asignatura)
print(Asignaturas)