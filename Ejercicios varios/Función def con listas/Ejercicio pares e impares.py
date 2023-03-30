import random
num=[]
for i in range(10):
    num.append(round(random.randrange(100)))
    def primos(num):
        if num%i==0:
            print("Es primo")
        else:
            print("No es primo")
for i in num:
    print(i)
    primos(i)


    