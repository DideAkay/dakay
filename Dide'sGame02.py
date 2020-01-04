import turtle
import math
import random
import winsound


isStart = 0
isGameOver = 0

#screen tanımları
wi = turtle.Screen()
wi.bgcolor("black")

#sınır cizimi
mypen = turtle.Turtle()
mypen.penup()
mypen.setposition(-300,-300)
mypen.down()
mypen.color("white")

for side in range(4):
    mypen.forward(600)
    mypen.left(90)
    mypen.hideturtle()

#goal yaratma
goal1 = turtle.Turtle()
turtle.pensize(25)
goal1.color("red")
goal1.shape("circle")
goal1.penup()
goal1.speed(0)
goal1.setposition(-100,100)


p1 = turtle.Turtle()
p1.color("green")
p1.shape("turtle")
p1.penup()
p1.speed(0)

hunter = turtle.Turtle()
hunter.color("orange")
hunter.shape("arrow")
hunter.penup()
hunter.setposition(-200,-200)
hunter.speed(0)

hunter1 = turtle.Turtle()
hunter1.color("orange")
hunter1.shape("arrow")
hunter1.penup()
hunter1.setposition(200,-200)
hunter1.speed(0)

hunter2 = turtle.Turtle()
hunter2.color("orange")
hunter2.shape("arrow")
hunter2.penup()
hunter2.setposition(-100,100)
hunter2.speed(0)

hunter3 = turtle.Turtle()
hunter3.color("orange")
hunter3.shape("arrow")
hunter3.penup()
hunter3.setposition(100,-100)
hunter3.speed(0)


speed1 = 3
speed2 = 3

score = 0
life = 3

def increaseSpeed(s):   
    s = s + 1
    return s

def decreaseSpeed(s):   
    if (s > 1):
        s = s - 0.25
    return s 


def turnleft1():
    p1.left(30)
    
def turnright1():
    p1.right(30)    

    
#pisagor ile verilen iki turtle arasi uzaklik hesaplar:   
def distance(a,b):
     
    d2 = math.sqrt(math.pow(a.xcor()-b.xcor(),2) + math.pow(a.ycor()-b.ycor(),2))
    return d2

#verilen turtle'i belirlediğim sinirlara carpinca verilen acida saga dondurur: 
def restrictTurtle(a, b):
    if a.xcor() < -300  or a.xcor() > 300:
        a.right(b)
        
    if a.xcor() < -300 and a.ycor() < -300:
        a.right(b)
        
    if a.xcor() > 300 and a.ycor() > 300:
        a.right(b)
        
    if a.ycor() < -300 or a.ycor() > 300:
        a.right(b)
        
pen = turtle.Turtle()
pen2 = turtle.Turtle()
pen3 = turtle.Turtle()

def Score(i):
#sol ust kosede score'u gosterir   
    pen.speed(0)
    pen.penup()
    pen.color("White")
    pen.goto(-300,310)
    pen.write("Score: " + str(i), font = ("Arial", 16, "normal"))
    pen.hideturtle()

def Life(i):
#sag ust kosede kalan cani gosterir  
    pen2.speed(0)
    pen2.penup()
    pen2.color("Red")
    pen2.goto(250,310)
    pen2.write("Life: " + str(i), font = ("Arial", 16, "normal"))
    pen2.hideturtle()
    
def GameOver():
    winsound.PlaySound("sad.wav", winsound.SND_ASYNC)
    pen3.clear()
    pen3.speed(0)
    pen3.penup()
    pen3.color("crimson")
    pen3.goto(-50,0)
    pen3.write("GAME OVER", font = ("Verdana", 16, "italic"))
    pen3.goto(-50,-50)
    pen3.write("Score: " + str(score), font = ("Verdana", 16, "italic"))
    pen3.goto(-50,-100)
    pen3.write("Press R to Restart", font = ("Verdana", 16, "italic"))
    pen3.hideturtle()
    pen.clear() 
    
  
def Restart():
    global speed1
    global speed2
    global life
    global isGameOver
    life = 3
    speed1 = 3
    speed2 = 3
    pen2.clear()
    Life(life)
    p1.setposition(random.randint(-300,300), random.randint(-300,300))
    pen3.clear()
    pen.clear()
    Score(score)
    isGameOver = 0
   

#YONLENDIRME
turtle.listen()
turtle.onkey(turnleft1, "Left")
turtle.onkey(turnright1, "Right")
turtle.onkey(Restart, "r")
turtle.onkey(Restart, "R")


while True:    
    
#iki hunter hizlanirken diger ikisi yavas kalsin istedigimden farkli hizlar atadim:
    p1.forward(speed1)
    hunter.forward(speed2)
    hunter1.forward(speed1)
    hunter2.forward(speed2)
    hunter3.forward(speed1)

        
# yazdigim Restrict fonksiyonu ile turtle'lari oyun alanina hapsettim:
    restrictTurtle(p1, 180)        
    restrictTurtle(hunter, 110)    
    restrictTurtle(hunter1, 100)
    restrictTurtle(hunter2, 80)
    restrictTurtle(hunter3, 70)
    
        
#Carpismalar icin uzakligi pisagor teoremini kullanarak koordinatlar ile hesapladim:
        
    if distance(hunter, p1) < 20:             
        winsound.PlaySound("hunter.wav", winsound.SND_ASYNC)
        life = life - 1
        pen2.clear()
        Life(life)
        p1.setposition(random.randint(-300,300), random.randint(-300,300))  
    
    elif distance(hunter1, p1) < 20:
        winsound.PlaySound("hunter.wav", winsound.SND_ASYNC)
        life = life - 1
        pen2.clear()
        Life(life)
        p1.setposition(random.randint(-300,300), random.randint(-300,300))
    
    elif distance(hunter2, p1) < 20:
        winsound.PlaySound("hunter.wav", winsound.SND_ASYNC)             
        life = life - 1
        pen2.clear()
        Life(life)
        p1.setposition(random.randint(-300,300), random.randint(-300,300))  
    
    elif distance(hunter3, p1) < 20:
        winsound.PlaySound("hunter.wav", winsound.SND_ASYNC)        
        life = life - 1
        pen2.clear()
        Life(life)
        p1.setposition(random.randint(-300,300), random.randint(-300,300))  
        
#score ve life göstergeleri:
    if isStart == 0:
        Score(score)
        Life(life)
        isStart = 1
         
#goal'a ulasinca score ve speed artiyor:    
    if distance(goal1, p1) < 20:
        winsound.PlaySound("goal.wav", winsound.SND_ASYNC)
        speed1 = increaseSpeed(speed1)
        goal1.setposition(random.randint(-300,300), random.randint(-300,300))
        score = score + 1
        pen.clear()        
        Score(score)
    
    if life == 0 and isGameOver == 0:        
        isGameOver = 1
        GameOver()
        speed1 = 0
        speed2 = 0
        score = 0
        
 #Dide Akay
 #18401807
    
        
        
        
    