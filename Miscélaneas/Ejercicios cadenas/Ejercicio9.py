def cifrado():
    palabra=input("Ingrese una palabra: ")
    código={"v":1,"e":2,"n":3,"t":4,"i":5,"l":6,"a":7,"d":8,"o":9,"r":10}
    for i in palabra:
        if i in código:
            print(código[i], end="")
        else:
            print(i, end="")
cifrado()