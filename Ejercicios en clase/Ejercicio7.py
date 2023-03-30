Asignaturas={"Matemáticas":6,"Física":4,"Química":5}
total_créditos=0
for asignatura,créditos in Asignaturas.items():
    print(asignatura,"tiene",créditos,"créditos.")
    total_créditos+=créditos
print("Número total de créditos del curso: ",total_créditos)