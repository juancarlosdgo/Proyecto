Día_ac=18
Mes_ac=12
Año_ac=2022
Día=int(input("Ingrese día: "))
Mes=int(input("Ingrese mes: "))
Año=int(input("Ingrese año: "))
Díam=Día_ac-Día
Mesm=Mes_ac-Mes
Añom=Año_ac-Año
Días=Día-Día_ac
Mess=Mes-Mes_ac
Años=Año-Año_ac
if Día<Día_ac and Mes<Mes_ac and Año<Año_ac:
    print("Han pasado",Añom,"años",Mesm,"meses y",Díam,"días desde la fecha.")
elif Día<Día_ac and Mes<Mes_ac and Año==Año_ac:
    print("Han pasado",Díam,"días y",Mesm,"meses desde la fecha.")
elif Día==Día_ac and Mes==Mes_ac and Año<Año_ac:
    print("Han pasado",Añom,"años desde la fecha.")
elif Día==Día_ac and Mesm and Añom :
    print("Han pasado",Mes_ac-Mes,"meses desde la fecha.")
elif Día<Día_ac and Mes==Mes_ac and Año<Año_ac:
    print("Han pasado",Díam,"días y",Añom,"años desde la fecha.")
elif Día<Día_ac and Mes==Mes_ac and Año<Año_ac:
    print("Han pasado",Añom,"años desde la fecha.")
elif Día>Día_ac and Día<=31 and Mes<Mes_ac and Año<Año_ac:
    print("Han pasado",Días,"días",Mesm,"meses",Añom,"años desde la fecha.")
elif Año>Año_ac and Día<=Día_ac and Mes<=Mes_ac:
    print("Faltan",Años,"años",Mes//Mes_ac+Mes,"meses",Día//Día_ac+Día,"días para llegar a esa fecha.")
elif Año>Año_ac and Día>Día_ac and Mes<=Mes_ac:
    print("Faltan",Años,"años",Mes//Mes_ac+Mes,"meses",Días,"días para llegar hasta esa fecha.")
elif Mes>12 or Día>31:
    print("Fecha inválida")