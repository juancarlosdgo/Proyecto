palabra=input("Ingrese una palabra: ")
vocals=["a","e","i","o","u"]
time=0
for vocal in vocals:
    if palabra==vocal:
        time+=1
        print(time)
