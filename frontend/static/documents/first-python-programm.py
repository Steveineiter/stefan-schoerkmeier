from turtle import *


def on_click_handler(x, y):
    print("Clicked on:", [x, y])
    movingTurtle.goto(x, y)


sc = Screen()
sc.setworldcoordinates(-300, -300, 300, 300)
sc.onclick(on_click_handler)




movingTurtle = Turtle()
movingTurtle.speed(0)

'info'
print("Hey there, YOU SHALL NOT PASS the controlls. You have to" \
    "have 3 symbols in one line to win. Place a Symbol by pressing" \
    "a number between 1 and 9, 1 is the upper left corner, 2 the upper middle corner and so on.")



'Drawing the field'

movingTurtle.penup()
movingTurtle.goto(-225, -225)
movingTurtle.pendown()

movingTurtle.forward(450)
movingTurtle.left(90)
movingTurtle.forward(450)
movingTurtle.left(90)
movingTurtle.forward(450)
movingTurtle.left(90)
movingTurtle.forward(450)
movingTurtle.left(90)
movingTurtle.forward(150)
movingTurtle.left(90)
movingTurtle.forward(450)
movingTurtle.right(90)
movingTurtle.forward(150)
movingTurtle.right(90)
movingTurtle.forward(450)
movingTurtle.left(90)
movingTurtle.forward(150)
movingTurtle.left(90)
movingTurtle.forward(150)
movingTurtle.left(90)
movingTurtle.forward(450)
movingTurtle.right(90)
movingTurtle.forward(150)
movingTurtle.right(90)
movingTurtle.forward(450)


movingTurtle.penup()
movingTurtle.goto(150, 0)
movingTurtle.pendown()
movingTurtle.pensize(2)

#if __name__ == '__main__':
    #print("Hello World!")

'Variables'

n=0

'Variables Cross'

ac=0
bc=0
cc=0
dc=0
ec=0
fc=0
gc=0
hc=0
ic=0

'Variables Cirkle'

ak=0
bk=0
ck=0
dk=0
ek=0
fk=0
gk=0
hk=0
ik=0

'Variables dont cheat'

a=0
b=0
c=0
d=0
e=0
f=0
g=0
h=0
i=0


'1.player_cross 1'

str1 = input("Please enter a number between 1 and 9: ")

'Not working if higher number first :('

#a=0
#b=1

if str1 == "1" :
        a=a+1
        while a==2:
            print("no")
            str1= input("please enter...")
            print(str1)
            if str1 != "1":
                    break
        x= -150
        y= 150
        ac=1


if str1 =="2":
        b=b+1
        while b==2:
            print("no")
            str1= input("please enter...")
            print(str1)
            if str1 != "2":
                    break
        x=0
        y=150
        bc=1


if str1 == "3" :
        c=c+1
        while c==2:
            print("no")
            str1= input("please enter...")
            print(str1)
            if str1 != "3":
                break
        x= 150
        y= 150
        cc=1


if str1 == "4" :
        d=d+1
        while d==2:
            print("no")
            str1= input("please enter...")
            print(str1)
            if str1 != "4":
                break
        x= -150
        y= 0
        dc=1


if str1 == "5" :
        e=e+1
        while e==2:
            print("no")
            str1= input("please enter...")
            print(str1)
            if str1 != "5":
                break
        x= 0
        y= 0
        ec=1


if str1 == "6" :
        f=f+1
        while f==2:
            print("no")
            str1= input("please enter...")
            print(str1)
            if str1 != "6":
                break
        x= 150
        y= 0
        fc=1


if str1 == "7" :
        g=g+1
        while g==2:
            print("no")
            str1= input("please enter...")
            print(str1)
            if str1 != "7":
                break
        x= -150
        y= -150
        gc=1

if str1 == "8" :
        h=h+1
        while h==2:
            print("no")
            str1= input("please enter...")
            print(str1)
            if str1 != "8":
                break
        x= 0
        y= -150
        hc=1


if str1 == "9" :
        i=i+1
        while i==2:
            print("no")
            str1= input("please enter...")
            print(str1)
            if str1 != "9":
                break
        x= 150
        y= -150
        ic=1


movingTurtle.color("violet")
movingTurtle.penup()
movingTurtle.goto(x, y)

movingTurtle.setheading(180)
movingTurtle.forward(75)
movingTurtle.left(90)
movingTurtle.forward(75)
movingTurtle.setheading(45)
movingTurtle.pendown()
movingTurtle.forward(213)
movingTurtle.penup()

movingTurtle.setheading(180)
movingTurtle.forward(150)
movingTurtle.setheading(315)
movingTurtle.pendown()
movingTurtle.forward(213)

'Winning Condition Cross'

if (ac == 1 and bc== 1 and cc==1) or (dc == 1 and ec ==1 and fc ==1) or (gc ==1 and hc ==1 and ic==1) or \
 (ac ==1 and dc ==1 and gc ==1) or (bc==1 and ec==1 and hc==1) or (cc==1 and fc==1 and ic==1) or \
 (ac==1 and ec==1 and ic==1) or (cc==1 and ec==1 and gc==1):

    print("Cross WON")

n= n+1

'2. player_circle 1 '

str1 = input("Please enter a number between 1 and 9: ")

if str1 == "1" :
        x= -150
        y= 150
        ak=1

if str1 =="2":
        x=0
        y=150
        bk=1

if str1 == "3" :
        x= 150
        y= 150
        ck=1

if str1 == "4" :
        x= -150
        y= 0
        dk=1

if str1 == "5" :
        x= 0
        y= 0
        ek=1
if str1 == "6" :
        x= 150
        y= 0
        fk=1

if str1 == "7" :
        x= -150
        y= -150
        gk=1

if str1 == "8" :
        x= 0
        y= -150
        hk=1

if str1 == "9" :
        x= 150
        y= -150
        ik=1


movingTurtle.penup()
movingTurtle.goto(x, y)
movingTurtle.color("orange")


movingTurtle.setheading(0)
movingTurtle.forward(75)
movingTurtle.setheading(90)
movingTurtle.pendown()
movingTurtle.circle(75)

'Winning Condition Circle'

if (ak == 1 and bk== 1 and ck==1) or (dk == 1 and ek ==1 and fk ==1) or (gk ==1 and hk ==1 and ik==1) or \
 (ak ==1 and dk ==1 and gk ==1) or (bk==1 and ek==1 and hk==1) or (ck==1 and fk==1 and ik==1) or \
 (ak==1 and ek==1 and ik==1) or (ck==1 and ek==1 and gk==1):

    print("Circle WON")

n= n+1

'1.player_cross 2'

str1 = input("Please enter a number between 1 and 9: ")


if str1 == "1" :
        x= -150
        y= 150
        ac=1

if str1 =="2":
        x=0
        y=150
        bc=1

if str1 == "3" :
        x= 150
        y= 150
        cc=1

if str1 == "4" :
        x= -150
        y= 0
        dc=1

if str1 == "5" :
        x= 0
        y= 0
        ec=1
if str1 == "6" :
        x= 150
        y= 0
        fc=1

if str1 == "7" :
        x= -150
        y= -150
        gc=1

if str1 == "8" :
        x= 0
        y= -150
        hc=1

if str1 == "9" :
        x= 150
        y= -150
        ic=1

movingTurtle.penup()
movingTurtle.goto(x, y)
movingTurtle.color("violet")

movingTurtle.setheading(180)
movingTurtle.forward(75)
movingTurtle.left(90)
movingTurtle.forward(75)
movingTurtle.setheading(45)
movingTurtle.pendown()
movingTurtle.forward(213)
movingTurtle.penup()

movingTurtle.setheading(180)
movingTurtle.forward(150)
movingTurtle.setheading(315)
movingTurtle.pendown()
movingTurtle.forward(213)

'Winning Condition Cross'

if (ac == 1 and bc== 1 and cc==1) or (dc == 1 and ec ==1 and fc ==1) or (gc ==1 and hc ==1 and ic==1) or \
 (ac ==1 and dc ==1 and gc ==1) or (bc==1 and ec==1 and hc==1) or (cc==1 and fc==1 and ic==1) or \
 (ac==1 and ec==1 and ic==1) or (cc==1 and ec==1 and gc==1):

    print("Cross WON")

n= n+1

'2. player_circle 2 '

str1 = input("Please enter a number between 1 and 9: ")

if str1 == "1" :
        x= -150
        y= 150
        ak=1

if str1 =="2":
        x=0
        y=150
        bk=1

if str1 == "3" :
        x= 150
        y= 150
        ck=1

if str1 == "4" :
        x= -150
        y= 0
        dk=1

if str1 == "5" :
        x= 0
        y= 0
        ek=1
if str1 == "6" :
        x= 150
        y= 0
        fk=1

if str1 == "7" :
        x= -150
        y= -150
        gk=1

if str1 == "8" :
        x= 0
        y= -150
        hk=1

if str1 == "9" :
        x= 150
        y= -150
        ik=1


movingTurtle.penup()
movingTurtle.goto(x, y)
movingTurtle.color("orange")

movingTurtle.setheading(0)
movingTurtle.forward(75)
movingTurtle.setheading(90)
movingTurtle.pendown()
movingTurtle.circle(75)

'Winning Condition Circle'

if (ak == 1 and bk== 1 and ck==1) or (dk == 1 and ek ==1 and fk ==1) or (gk ==1 and hk ==1 and ik==1) or \
 (ak ==1 and dk ==1 and gk ==1) or (bk==1 and ek==1 and hk==1) or (ck==1 and fk==1 and ik==1) or \
 (ak==1 and ek==1 and ik==1) or (ck==1 and ek==1 and gk==1):

    print("Circle WON")

n= n+1

'1.player_cross 3'

str1 = input("Please enter a number between 1 and 9: ")


if str1 == "1" :
        x= -150
        y= 150
        ac=1

if str1 =="2":
        x=0
        y=150
        bc=1

if str1 == "3" :
        x= 150
        y= 150
        cc=1

if str1 == "4" :
        x= -150
        y= 0
        dc=1

if str1 == "5" :
        x= 0
        y= 0
        ec=1
if str1 == "6" :
        x= 150
        y= 0
        fc=1

if str1 == "7" :
        x= -150
        y= -150
        gc=1

if str1 == "8" :
        x= 0
        y= -150
        hc=1

if str1 == "9" :
        x= 150
        y= -150
        ic=1

movingTurtle.penup()
movingTurtle.goto(x, y)
movingTurtle.color("violet")

movingTurtle.setheading(180)
movingTurtle.forward(75)
movingTurtle.left(90)
movingTurtle.forward(75)
movingTurtle.setheading(45)
movingTurtle.pendown()
movingTurtle.forward(213)
movingTurtle.penup()

movingTurtle.setheading(180)
movingTurtle.forward(150)
movingTurtle.setheading(315)
movingTurtle.pendown()
movingTurtle.forward(213)

'Winning Condition Cross'

if (ac == 1 and bc== 1 and cc==1) or (dc == 1 and ec ==1 and fc ==1) or (gc ==1 and hc ==1 and ic==1) or \
 (ac ==1 and dc ==1 and gc ==1) or (bc==1 and ec==1 and hc==1) or (cc==1 and fc==1 and ic==1) or \
 (ac==1 and ec==1 and ic==1) or (cc==1 and ec==1 and gc==1):

    print("Cross WON")

n= n+1

'2. player_circle 3'

str1 = input("Please enter a number between 1 and 9: ")

if str1 == "1" :
        x= -150
        y= 150
        ak=1

if str1 =="2":
        x=0
        y=150
        bk=1

if str1 == "3" :
        x= 150
        y= 150
        ck=1

if str1 == "4" :
        x= -150
        y= 0
        dk=1

if str1 == "5" :
        x= 0
        y= 0
        ek=1
if str1 == "6" :
        x= 150
        y= 0
        fk=1

if str1 == "7" :
        x= -150
        y= -150
        gk=1

if str1 == "8" :
        x= 0
        y= -150
        hk=1

if str1 == "9" :
        x= 150
        y= -150
        ik=1


movingTurtle.penup()
movingTurtle.goto(x, y)
movingTurtle.color("orange")

movingTurtle.setheading(0)
movingTurtle.forward(75)
movingTurtle.setheading(90)
movingTurtle.pendown()
movingTurtle.circle(75)

'Winning Condition Circle'

if (ak == 1 and bk== 1 and ck==1) or (dk == 1 and ek ==1 and fk ==1) or (gk ==1 and hk ==1 and ik==1) or \
 (ak ==1 and dk ==1 and gk ==1) or (bk==1 and ek==1 and hk==1) or (ck==1 and fk==1 and ik==1) or \
 (ak==1 and ek==1 and ik==1) or (ck==1 and ek==1 and gk==1):

    print("Circle WON")

n= n+1

'1.player_cross 4'

str1 = input("Please enter a number between 1 and 9: ")


if str1 == "1" :
        x= -150
        y= 150
        ac=1

if str1 =="2":
        x=0
        y=150
        bc=1

if str1 == "3" :
        x= 150
        y= 150
        cc=1

if str1 == "4" :
        x= -150
        y= 0
        dc=1

if str1 == "5" :
        x= 0
        y= 0
        ec=1
if str1 == "6" :
        x= 150
        y= 0
        fc=1

if str1 == "7" :
        x= -150
        y= -150
        gc=1

if str1 == "8" :
        x= 0
        y= -150
        hc=1

if str1 == "9" :
        x= 150
        y= -150
        ic=1

movingTurtle.penup()
movingTurtle.goto(x, y)
movingTurtle.color("violet")

movingTurtle.setheading(180)
movingTurtle.forward(75)
movingTurtle.left(90)
movingTurtle.forward(75)
movingTurtle.setheading(45)
movingTurtle.pendown()
movingTurtle.forward(213)
movingTurtle.penup()

movingTurtle.setheading(180)
movingTurtle.forward(150)
movingTurtle.setheading(315)
movingTurtle.pendown()
movingTurtle.forward(213)

'Winning Condition Cross'

if (ac == 1 and bc== 1 and cc==1) or (dc == 1 and ec ==1 and fc ==1) or (gc ==1 and hc ==1 and ic==1) or \
 (ac ==1 and dc ==1 and gc ==1) or (bc==1 and ec==1 and hc==1) or (cc==1 and fc==1 and ic==1) or \
 (ac==1 and ec==1 and ic==1) or (cc==1 and ec==1 and gc==1):

    print("Cross WON")

n= n+1

'2. player_circle 4'

str1 = input("Please enter a number between 1 and 9: ")

if str1 == "1" :
        x= -150
        y= 150
        ak=1

if str1 =="2":
        x=0
        y=150
        bk=1

if str1 == "3" :
        x= 150
        y= 150
        ck=1

if str1 == "4" :
        x= -150
        y= 0
        dk=1

if str1 == "5" :
        x= 0
        y= 0
        ek=1
if str1 == "6" :
        x= 150
        y= 0
        fk=1

if str1 == "7" :
        x= -150
        y= -150
        gk=1

if str1 == "8" :
        x= 0
        y= -150
        hk=1

if str1 == "9" :
        x= 150
        y= -150
        ik=1


movingTurtle.penup()
movingTurtle.goto(x, y)
movingTurtle.color("orange")

movingTurtle.setheading(0)
movingTurtle.forward(75)
movingTurtle.setheading(90)
movingTurtle.pendown()
movingTurtle.circle(75)

'Winning Condition Circle'

if (ak == 1 and bk== 1 and ck==1) or (dk == 1 and ek ==1 and fk ==1) or (gk ==1 and hk ==1 and ik==1) or \
 (ak ==1 and dk ==1 and gk ==1) or (bk==1 and ek==1 and hk==1) or (ck==1 and fk==1 and ik==1) or \
 (ak==1 and ek==1 and ik==1) or (ck==1 and ek==1 and gk==1):

    print("Circle WON")

n= n+1

'1.player_cross 5'

str1 = input("Please enter a number between 1 and 9: ")


if str1 == "1" :
        x= -150
        y= 150
        ac=1

if str1 =="2":
        x=0
        y=150
        bc=1

if str1 == "3" :
        x= 150
        y= 150
        cc=1

if str1 == "4" :
        x= -150
        y= 0
        dc=1

if str1 == "5" :
        x= 0
        y= 0
        ec=1
if str1 == "6" :
        x= 150
        y= 0
        fc=1

if str1 == "7" :
        x= -150
        y= -150
        gc=1

if str1 == "8" :
        x= 0
        y= -150
        hc=1

if str1 == "9" :
        x= 150
        y= -150
        ic=1

movingTurtle.penup()
movingTurtle.goto(x, y)
movingTurtle.color("violet")

movingTurtle.setheading(180)
movingTurtle.forward(75)
movingTurtle.left(90)
movingTurtle.forward(75)
movingTurtle.setheading(45)
movingTurtle.pendown()
movingTurtle.forward(213)
movingTurtle.penup()

movingTurtle.setheading(180)
movingTurtle.forward(150)
movingTurtle.setheading(315)
movingTurtle.pendown()
movingTurtle.forward(213)


'Winning Condition Cross'

if (ac == 1 and bc== 1 and cc==1) or (dc == 1 and ec ==1 and fc ==1) or (gc ==1 and hc ==1 and ic==1) or \
 (ac ==1 and dc ==1 and gc ==1) or (bc==1 and ec==1 and hc==1) or (cc==1 and fc==1 and ic==1) or \
 (ac==1 and ec==1 and ic==1) or (cc==1 and ec==1 and gc==1):

    print("Cross WON")

n= n+1

'Draw Condition'

if n== 9 and not ((ak == 1 and bk== 1 and ck==1) or (dk == 1 and ek ==1 and fk ==1) or (gk ==1 and hk ==1 and ik==1) or \
 (ak ==1 and dk ==1 and gk ==1) or (bk==1 and ek==1 and hk==1) or (ck==1 and fk==1 and ik==1) or \
 (ak==1 and ek==1 and ik==1) or (ck==1 and ek==1 and gk==1) or (ac == 1 and bc== 1 and cc==1) or \
 (dc == 1 and ec ==1 and fc ==1) or (gc ==1 and hc ==1 and ic==1) or \
 (ac ==1 and dc ==1 and gc ==1) or (bc==1 and ec==1 and hc==1) or (cc==1 and fc==1 and ic==1) or \
 (ac==1 and ec==1 and ic==1) or (cc==1 and ec==1 and gc==1)):

    print("Draw")


sc.mainloop()