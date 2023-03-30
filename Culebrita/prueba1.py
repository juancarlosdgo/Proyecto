import turtle
import time
import random
posponer=0.1

#Incrementador marcador
score=0
high_score=0
game_over=False

wn=turtle.Screen()
wn.title("Culebrita")
wn.bgcolor("black")
wn.setup(width=600,height=600)
wn.tracer(0)

cabeza=turtle.Turtle()
cabeza.speed(0)
cabeza.shape("circle")
cabeza.color("#40E0D0")
cabeza.penup()
cabeza.goto(0,0)
cabeza.direction="stop"
#Comida
comida=turtle.Turtle()
comida.speed(0)
comida.shape("circle")
comida.color("#e30000")
comida.penup()
comida.goto(0,100)
comida.direction="stop"
#Segmentos
segmentos=[]
#Marcador
texto=turtle.Turtle()
texto.speed(0)
texto.color("White")
texto.penup()
texto.hideturtle()
texto.goto(0,260)
texto.write("Score:0        High score:0",align="center",font=("arial",24,"normal"))

def arriba():
    cabeza.direction="up"
def abajo():
    cabeza.direction="down"
def izquierda():
    cabeza.direction="left"
def derecha():
    cabeza.direction="right"
#Teclado
wn.listen()
wn.onkeypress(arriba,"Up")
wn.onkeypress(abajo,"Down")
wn.onkeypress(izquierda,"Left")
wn.onkeypress(derecha,"Right")

def move():
    if cabeza.direction=="up":
        y=cabeza.ycor()
        cabeza.sety(y+20)
    if cabeza.direction=="down":
        y=cabeza.ycor()
        cabeza.sety(y-20)
    if cabeza.direction=="left":
        x=cabeza.xcor()
        cabeza.setx(x-20)
    if cabeza.direction=="right":
        x=cabeza.xcor()
        cabeza.setx(x+20)

while True:
    if cabeza.xcor()>290 or cabeza.xcor()<-290 or cabeza.ycor()>259 or cabeza.ycor()<-290:
        time.sleep(1)
        cabeza.goto(0,0)
        cabeza.direction="stop"
        game_over = True
    #Esconder los segmentos
        for segmento in segmentos:
            segmento.goto(2000,2000)
    #Limpiar lista
        segmentos.clear()
        #Resetear marcador
    if game_over and cabeza.direction != "stop":
        texto.clear()
        game_over = False

        score=0
        texto.clear()
        texto.goto(0,260)
        texto.write("Score:{}        High score:{}".format(score,high_score),align="center",font=("arial",24,"normal"))
    #LEtrero game over
    if game_over:
        texto.goto(0,0)
        texto.write("Game over",align="center",font=("arial",25,"normal"))
        texto.goto(0,260)
    wn.update()
    if cabeza.distance(comida)<20:
        x=random.randint(-280,280)
        y=random.randint(-280,250)
        comida.goto(x,y)

        nuevo_segmento=turtle.Turtle()
        nuevo_segmento.speed(0)
        nuevo_segmento.shape("circle")
        nuevo_segmento.color("#E30052")
        nuevo_segmento.penup()
        segmentos.append(nuevo_segmento)

        score+=10
        if score>high_score:
            high_score=score
        texto.clear()
        texto.goto(0,260)
        texto.write("Score:{}        High score:{}".format(score,high_score),align="center",font=("arial",24,"normal"))
    #Mover el cuerpo de la serpiente
    totalseg=len(segmentos)
    for i in range(totalseg -1,0,-1):
        x=segmentos[i-1].xcor()
        y=segmentos[i-1].ycor()
        segmentos[i].goto(x,y)
    if totalseg>0:
        x=cabeza.xcor()
        y=cabeza.ycor()
        segmentos[0].goto(x,y)
    move()
    #Colisiones con el cuerpo
    for segmento in segmentos:
        if segmento.distance(cabeza)<20:
            time.sleep(1)
            cabeza.goto(300,300)
            cabeza.direction="stop"
            #Esconder los segmentos
            texto.goto(0,0)
            texto.write("Game over",align="center",font=("arial",25,"normal"))
            for segmento in segmentos:
                segmento.goto(1000,1000)
            segmentos.clear()
    time.sleep(posponer)
