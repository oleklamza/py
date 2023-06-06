from turtle import *
import random

def podstawa_1():
    left(45)
    fd(50)

def podstawa_2():
    right(90)
    fd(50)

def slup():
    pu()
    right(135)
    fd(35)
    right(90)
    pd()
    fd(150)

def belka():
    right(90)
    fd(75)

def poprzeczka():
    right(180)
    fd(50)
    left(45)
    fd(35)
    left(180)
    fd(35)
    right(45)
    fd(50)
    pass

def lina():
    right(90)
    fd(20)
    pass

def glowa():
    pu()
    fd(40)
    left(90)
    pd()
    circle(20)

def tulow():
    right(90)
    fd(50)

def nogi():
    right(45)
    fd(20)
    right(180)
    fd(20)
    right(90)
    fd(20)
    right(180)
    fd(20)

def rece():
    right(45)
    fd(35)
    right(90)
    fd(20)
    right(180)
    fd(40)

def wypisz_slowo(slowo):
    pu()
    xy = pos()
    goto(0, -50)
    f = ("Courier", 16, "normal")
    color("white")
    write("█"*len(slowo), align="center", font=f)
    color("black")
    write(slowo, align="center", font=f)
    goto(xy)
    pd()

def napis_koncowy(napis):
    pu()
    goto(0,200)
    write(napis, align="center", font=("Courier", 32, "bold"))

rysuj_elementy = (podstawa_1, podstawa_2, slup, belka, poprzeczka, lina, glowa, tulow, nogi, rece)

hideturtle()
pu()
setx(-60)
pd()
color("silver")
for e in rysuj_elementy:
    e()
pu()
home()
setx(-60)
color("black")
pensize(2)
hideturtle()

#
slowa = ["jesiotr", "klawesyn", "przepierzenie", "głownia", "majstersztyk",
         "krowa", "zoo", "hiacynt"]
slowo = random.choice(slowa)
wypisz_slowo("*" * len(slowo))

litery = []
etap = 0

while True:
    # nowa_litera = input("Podaj literę: ")
    nowa_litera = textinput("Wisielec", "Podaj literę")
    litery.append(nowa_litera)

    odkryte = ""
    czy_trafiona = False
    czy_wszystkie = True
    for litera in slowo:
        if litera in litery:
            odkryte += litera
            if litera == nowa_litera:
                czy_trafiona = True
        else:
            odkryte += "*"
            czy_wszystkie = False

    # print(odkryte)
    wypisz_slowo(odkryte)


    if czy_wszystkie:
        # print("BRAWO!!!")
        color("green")
        napis_koncowy("BRAWO!!!")
        break

    if not czy_trafiona:
        rysuj_elementy[etap]()
        etap += 1
        if etap == 10:
            # print("NIE UDAŁO SIĘ...")
            color("red")
            napis_koncowy("NIE UDAŁO SIĘ...")
            break

done()