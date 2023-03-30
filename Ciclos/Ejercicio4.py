
cont=0
for i in range(1,1000):
    suma=0
    for j in range(1,i):
        if i%j==0:
            suma+=j
    if suma==i:
        cont=cont+1
        print(i)
print("Hay",cont,"números perfectos de 1 a 1000")