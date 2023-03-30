import random
tam=int(input("Cuántos números: "))
vector=[]
for i in range(tam):
    vector.append(round(random.random()*100))
    print(vector)
suma=tam+vector.append
print("La suma es de: ", suma)