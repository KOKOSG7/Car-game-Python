import tkinter as tk
import random


game = tk.Tk()
game.geometry("1000x800")
game.resizable(0,0)
game.overrideredirect(True)

fondo = tk.Canvas(game, height="800", width="1000", bg="#79ffae")
texto = fondo.create_text(900,700, text="", font=("Arial", 16))

ronda = 1
puntos = 0
limitD = True
limitA = True

boton = tk.Button(game, text='Iniciar', command=lambda: [movimientoglobal(r1,r2,r3,r4,r5,r6,r7,r8,r9,r10,r11,r12,r13,r14,r15), botonbloqued(), det()])
def botonbloqued():
    boton.config(state="disabled")

nombres = ["r1","r2","r3","r4","r5","r6","r7","r8","r9","r10","r11","r12","r13","r14","r15"]

rocas = []
t = 0
for t in range(15):
    rand = random.randint(25,975)
    rand0 = rand - 25
    rand2 = rand + 25
    if t < 3:
        altura = 0
    elif t < 6:
        altura = -200
    elif t < 9:
        altura = -400
    elif t < 12:
        altura = -600
    else:
        altura = -800
    create = fondo.create_rectangle(rand0, altura-50, rand2, altura, fill="gray")
    rocas.append(create)
    t += 1


r1 = rocas[0]
r2 = rocas[1]
r3 = rocas[2]
r4 = rocas[3]
r5 = rocas[4]
r6 = rocas[5]
r7 = rocas[6]
r8 = rocas[7]
r9 = rocas[8]
r10 = rocas[9]
r11 = rocas[10]
r12 = rocas[11]
r13 = rocas[12]
r14 = rocas[13]
r15 = rocas[14]




def movimientoglobal(a,b,c,d,e,f,g,h,i,j,k,l,m,n,o):
    movimiento(a)
    movimiento(b)
    movimiento(c)
    movimiento(d)
    movimiento(e)
    movimiento(f)
    movimiento(g)
    movimiento(h)
    movimiento(i)
    movimiento(j)
    movimiento(k)
    movimiento(l)
    movimiento(m)
    movimiento(n)
    movimiento(o)

speed = 1


def movimiento(movobj):
    if fin:
        global speed
        fondo.move(movobj,0,speed)
        coords = fondo.coords(movobj)
        if coords[1] > 900:
            print("roca parada")
        else:
            game.after(10,lambda: [movimiento(movobj)])

cocheimg = tk.PhotoImage(file="car.png")
coche = fondo.create_image(500, 600, image = cocheimg)

Dp = False

def Dpress(event):
    global Dp 
    Dp = True

def Dout(event):
    global Dp
    Dp = False

def movD():
    if Dp:
        if limitD:
            fondo.move(coche, 0.5, 0)
    if fin:
        game.after(1, movD)

game.bind('<KeyPress-d>', Dpress)
game.bind('<KeyRelease-d>', Dout)

Ap = False

def Apress(event):
    global Ap 
    Ap = True

def Aout(event):
    global Ap
    Ap = False

def movA():
    if Ap:
        if limitA:
            fondo.move(coche, -0.5, 0)
    if fin:
        game.after(1, movA)

game.bind('<KeyPress-a>', Apress)
game.bind('<KeyRelease-a>', Aout)

def detectar_colision(obj):
    global limitA, limitD
    coords_objeto1 = fondo.coords(obj)
    xy_objeto2 = fondo.coords(coche)
    coords_objeto2 = []
    coords_objeto2.append(xy_objeto2[0] - 25)
    coords_objeto2.append(xy_objeto2[1] - 55)
    coords_objeto2.append(xy_objeto2[0] + 25)
    coords_objeto2.append(xy_objeto2[1] + 55)
    print(coords_objeto2)
    if (coords_objeto1[2] >= coords_objeto2[0] and coords_objeto1[0] <= coords_objeto2[2]) and (coords_objeto1[3] >= coords_objeto2[1] and coords_objeto1[1] <= coords_objeto2[3]):
        fin()
    if coords_objeto2[0] < 0:
        limitA = False
    if coords_objeto2[2] > 1000:
        limitD = False
    if (coords_objeto2[0] > 0 and coords_objeto2[2] < 1000 ):
        limitD = True
        limitA = True
    
fin = True
def det():
    if fin:
        detectar_colision(r1)
        detectar_colision(r2)
        detectar_colision(r3)
        detectar_colision(r4)
        detectar_colision(r5)
        detectar_colision(r6)
        detectar_colision(r7)
        detectar_colision(r8)
        detectar_colision(r9)
        detectar_colision(r10)
        detectar_colision(r11)
        detectar_colision(r12)
        detectar_colision(r13)
        detectar_colision(r14)
        detectar_colision(r15)
        game.after(10,det)
    else:
        print("Deteccion finalizada!")

def fin():
    global fin
    fin = False

def round():
    y = fondo.coords(r15)
    if y[1] > 900:
        reround()
        global texto, puntos, ronda, speed
        puntos += ronda * 100
        ronda += 1
        speed += 0.5
        fondo.itemconfig(texto, text="Puntos: "+str(puntos))
    game.after(100, round)
        
def enable():
    boton.config(state="normal")

def reround():
    if round:
        global rocas
        rocas = []
        t = 0
        for t in range(15):
            rand = random.randint(25,975)
            rand0 = rand - 25
            rand2 = rand + 25
            if t < 3:
                altura = 0
            elif t < 6:
                altura = -200
            elif t < 9:
                altura = -400
            elif t < 12:
                altura = -600
            else:
                altura = -800
            create = fondo.create_rectangle(rand0, altura-50, rand2, altura, fill="gray")
            rocas.append(create)
            t += 1
        
        global r1,r2,r3,r4,r5,r6,r7,r8,r9,r10,r11,r12,r13,r14,r15

        r1 = rocas[0]
        r2 = rocas[1]
        r3 = rocas[2]
        r4 = rocas[3]
        r5 = rocas[4]
        r6 = rocas[5]
        r7 = rocas[6]
        r8 = rocas[7]
        r9 = rocas[8]
        r10 = rocas[9]
        r11 = rocas[10]
        r12 = rocas[11]
        r13 = rocas[12]
        r14 = rocas[13]
        r15 = rocas[14]

        print(ronda)
        enable()




round()
movD()
movA()
boton.pack()
fondo.pack()
game.mainloop()