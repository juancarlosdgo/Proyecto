for i in range(2,1000):
    cont=0
    for j in range(1,1000+1):
        if i%j==0:
            cont+=1
    if cont==2:
        print(i)
