Asignaturas=["Matemáticas","Física","Química","Historia","Lengua"]
print(Asignaturas)
Notas=[]
for asignatura in Asignaturas:
    nota=int(input("Ingrese nota del estudiante: "))
    Notas.append(nota)
for i in range(len(Asignaturas)):
    print("En",Asignaturas[i],"has sacado",Notas[i])