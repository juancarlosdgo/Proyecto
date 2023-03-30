meses={1:"Enero",2:"Febero",3:"Marzo",4:"Abril",5:"Mayo",6:"Junio",7:"Julio",8:"Agosto",9:"Septiembre",10:"Octubre",11:"1Noviembre",12:"Diciembre"}
Fecha=input("Ingrese fecha en formato dd/mm/aaaa: ")
Fecha=Fecha.split("/")
print(Fecha[0],"de",meses[int(Fecha[1])],"de",Fecha[2])