import random
import time
import threading
from Tkinter import *
import tkMessageBox
window = Tk()
window.wm_title("Arena")
canvas = Canvas(window, width=800, height=780, bg='#cecece')
canvas.pack()

#IMPORT THE NUMBERS THAT REPRESENT THE MAP
op = open('num.txt')
rd = op.read()
x = int(rd)
y=x

op2 = open('wishlist.txt')
rd2 = op2.read()
x2 = int(rd2)
wish=x2

wishlist = []

for i in range(10):
    if wish%10 == 0:
        wishlist.append(int(wish%100))
        wish = wish/100
    else:
        wishlist.append(int(wish%10))
        wish = wish/10

list.reverse(wishlist)


    
with open('pointList.txt') as f:
    lines = f.readlines()


   
#MATRIX'S LISTS
coords1=[]
coords2=[]
coords3=[]
coords4=[]
coords5=[]
coords6=[]
coords7=[]
coords8=[]
coords9=[]
coords10=[]
coords11=[]
coords12=[]
coords13=[]
coords14=[]
coords15=[]
coords16=[]
coords17=[]
coords18=[]
coords19=[]
coords20=[]
coords21=[]
coords22=[]
coords23=[]
coords24=[]
coords25=[]
coords26=[]
coords27=[]
coords28=[]
coords29=[]
coords30=[]
coords31=[]
coords32=[]
coords33=[]
coords34=[]
coords35=[]
coords36=[]
coords37=[]
coords38=[]
coords39=[]

#POPULATE THE LISTS
for i in range(40):
    coords39.append(int(x%10))
    x = x/10

list.reverse(coords39)

for i in range(40):
    coords38.append(int(x%10))
    x = x/10

list.reverse(coords38)

for i in range(40):
    coords37.append(int(x%10))
    x = x/10

list.reverse(coords37)

for i in range(40):
    coords36.append(int(x%10))
    x = x/10

list.reverse(coords36)

for i in range(40):
    coords35.append(int(x%10))
    x = x/10

list.reverse(coords35)

for i in range(40):
    coords34.append(int(x%10))
    x = x/10

list.reverse(coords34)

for i in range(40):
    coords33.append(int(x%10))
    x = x/10

list.reverse(coords33)

for i in range(40):
    coords32.append(int(x%10))
    x = x/10

list.reverse(coords32)

for i in range(40):
    coords31.append(int(x%10))
    x = x/10

list.reverse(coords31)

for i in range(40):
    coords30.append(int(x%10))
    x = x/10

list.reverse(coords30)

for i in range(40):
    coords29.append(int(x%10))
    x = x/10

list.reverse(coords29)

for i in range(40):
    coords28.append(int(x%10))
    x = x/10

list.reverse(coords28)

for i in range(40):
    coords27.append(int(x%10))
    x = x/10

list.reverse(coords27)

for i in range(40):
    coords26.append(int(x%10))
    x = x/10

list.reverse(coords26)

for i in range(40):
    coords25.append(int(x%10))
    x = x/10

list.reverse(coords25)

for i in range(40):
    coords24.append(int(x%10))
    x = x/10

list.reverse(coords24)

for i in range(40):
    coords23.append(int(x%10))
    x = x/10

list.reverse(coords23)

for i in range(40):
    coords22.append(int(x%10))
    x = x/10

list.reverse(coords22)

for i in range(40):
    coords21.append(int(x%10))
    x = x/10

list.reverse(coords21)

for i in range(40):
    coords20.append(int(x%10))
    x = x/10

list.reverse(coords20)

for i in range(40):
    coords19.append(int(x%10))
    x = x/10

list.reverse(coords19)

for i in range(40):
    coords18.append(int(x%10))
    x = x/10

list.reverse(coords18)

for i in range(40):
    coords17.append(int(x%10))
    x = x/10

list.reverse(coords17)

for i in range(40):
    coords16.append(int(x%10))
    x = x/10

list.reverse(coords16)

for i in range(40):
    coords15.append(int(x%10))
    x = x/10

list.reverse(coords15)

for i in range(40):
    coords14.append(int(x%10))
    x = x/10

list.reverse(coords14)

for i in range(40):
    coords13.append(int(x%10))
    x = x/10

list.reverse(coords13)

for i in range(40):
    coords12.append(int(x%10))
    x = x/10

list.reverse(coords12)

for i in range(40):
    coords11.append(int(x%10))
    x = x/10

list.reverse(coords11)

for i in range(40):
    coords10.append(int(x%10))
    x = x/10

list.reverse(coords10)

for i in range(40):
    coords9.append(int(x%10))
    x = x/10

list.reverse(coords9)

for i in range(40):
    coords8.append(int(x%10))
    x = x/10

list.reverse(coords8)

for i in range(40):
    coords7.append(int(x%10))
    x = x/10

list.reverse(coords7)

for i in range(40):
    coords6.append(int(x%10))
    x = x/10

list.reverse(coords6)

for i in range(40):
    coords5.append(int(x%10))
    x = x/10

list.reverse(coords5)

for i in range(40):
    coords4.append(int(x%10))
    x = x/10

list.reverse(coords4)

for i in range(40):
    coords3.append(int(x%10))
    x = x/10

list.reverse(coords3)

for i in range(40):
    coords2.append(int(x%10))
    x = x/10

list.reverse(coords2)

for i in range(40):
    coords1.append(int(x%10))
    x = x/10

list.reverse(coords1)

#CREATE MATRIX
matrix = [coords1, coords2, coords3, coords4, coords5, coords6, coords7, coords8, coords9, coords10, coords11, coords12, coords13, coords14, coords15, coords16, coords17, coords18, coords19, coords20, coords21, coords22, coords23, coords24, coords25, coords26, coords27, coords28, coords29, coords30, coords31, coords32, coords33, coords34, coords35, coords36, coords37, coords38, coords39]

#OBSTACLES PLACED
h = 180
i = 1
while i <= h:
    w1 = random.randrange(2,38)
    w2 = random.randrange(2,37)
    if matrix[w2][w1] == 1:
        k = 1
        if matrix[w2-1][w1] != 1:
            k = 0
        if matrix[w2+1][w1] != 1:
            k = 0
        if matrix[w2][w1-1] != 1:
            k = 0
        if matrix[w2][w1+1] != 1:
            k = 0
        if matrix[w2-1][w1-1] != 1:
            k = 0
        if matrix[w2+1][w1-1] != 1:
            k = 0
        if matrix[w2-1][w1+1] != 1:
            k = 0
        if matrix[w2+1][w1+1] != 1:
            k = 0
        if k == 1:
            matrix[w2][w1] = 2
            i = i + 1
            
#TRAPS PLACED
h = int(lines[10])
for i in range (h):
    w1 = random.randrange(1,30)
    w2 = random.randrange(1,30)
    if matrix[w2][w1] != 1:
        h = h + 1
    else:
        matrix[w2][w1] = 6

#BATTERIES PLACED
h = 8
for i in range (h):
    w1 = random.randrange(1,30)
    w2 = random.randrange(1,30)
    if matrix[w2][w1] != 1:
        h = h + 1
    else:
        matrix[w2][w1] = random.randrange(7,9)
        
#CLASSES
class treasure:
    def __init__(self, xco, yco, ty, points, name, var):
        self.xco = xco
        self.yco = yco
        self.ty = ty
        self.points = points
        self.name = name
        self.var = var

class robot:
    def __init__(self, xco, yco, points):
        self.xco = xco
        self.yco = yco
        self. points = points


robot1 = robot(20, 180, 0)

#ARENA BORDERS
for i in range(39):
    if matrix[i][0] == 1:
        matrix[i][0] = 2

for i in range(39):
    if matrix[i][39] == 1:
        matrix[i][39] = 2

for i in range(40):
    if matrix[0][i] == 1:
        matrix[0][i] = 2

for i in range(40):
    if matrix[38][i] == 1:
        matrix[38][i] = 2
        
#SPRITES IMPORT
sprite1 = PhotoImage(file = 'sprites/floorSprite.gif')
sprite2 = PhotoImage(file = 'sprites/wallSprite.gif')
sprite3 = PhotoImage(file = 'sprites/treasure1.gif')
sprite4 = PhotoImage(file = 'sprites/treasure2.gif')
sprite5 = PhotoImage(file = 'sprites/treasure3.gif')
sprite8 = PhotoImage(file = 'sprites/trap.gif')
r1 = PhotoImage(file = 'sprites/robot_r.gif')
r2 = PhotoImage(file = 'sprites/robot_l.gif')
r3 = PhotoImage(file = 'sprites/robot_u.gif')
r4 = PhotoImage(file = 'sprites/robot_d.gif')
sprite10 = PhotoImage(file = 'sprites/treasure4.gif')
sprite11 = PhotoImage(file = 'sprites/treasure5.gif')
sprite12 = PhotoImage(file = 'sprites/treasure6.gif')
sprite13 = PhotoImage(file = 'sprites/treasure7.gif')
sprite14 = PhotoImage(file = 'sprites/treasure8.gif')
sprite15 = PhotoImage(file = 'sprites/treasure9.gif')
sprite16 = PhotoImage(file = 'sprites/treasure10.gif')
sprite17 = PhotoImage(file = 'sprites/treasure11.gif')
heading1 = PhotoImage(file = 'sprites/i1.gif')
heading2 = PhotoImage(file = 'sprites/i2.gif')
heading3 = PhotoImage(file = 'sprites/i3.gif')
heading4 = PhotoImage(file = 'sprites/i4.gif')
heading5 = PhotoImage(file = 'sprites/i5.gif')
heading6 = PhotoImage(file = 'sprites/i6.gif')
heading7 = PhotoImage(file = 'sprites/i7.gif')
heading8 = PhotoImage(file = 'sprites/i8.gif')
heading9 = PhotoImage(file = 'sprites/i9.gif')
heading10 = PhotoImage(file = 'sprites/i10.gif')
bat1 = PhotoImage(file = 'sprites/bat1.gif')
bat2 = PhotoImage(file = 'sprites/bat2.gif')
headings = [heading1, heading2, heading3, heading4, heading5, heading6, heading7, heading8, heading9, heading10]

#TREASURE SPRITES LISTS
T1=[sprite3, sprite4, sprite5, sprite16, sprite17]
T2=[sprite10, sprite11, sprite12]
T3=[sprite13, sprite14, sprite15]

#TREASURE CLASS INSTANCES
treasure1, treasure2, treasure3, treasure4, treasure5, treasure6, treasure7, treasure8, treasure9, treasure10 = treasure(0, 0, 0, 0, 'n', '1'), treasure(0, 0, 0, 0, 'n', '2'), treasure(0, 0, 0, 0, 'n', '3'), treasure(0, 0, 0, 0, 'n', '4'), treasure(0, 0, 0, 0, 'n', '5'), treasure(0, 0, 0, 0, 'n', '6'), treasure(0, 0, 0, 0, 'n', '7'), treasure(0, 0, 0, 0, 'n', '8'), treasure(0, 0, 0, 0, 'n', '9'), treasure(0, 0, 0, 0, 'n', '10')

#TREASURE LIST
tlist = [treasure1, treasure2, treasure3, treasure4, treasure5, treasure6, treasure7, treasure8, treasure9, treasure10]

#TREASURE LIST INDEX
k = 0

#FLOOR, OBSTACLES AND TREASURES DISPLAY




for i in range(40):
    l = 0
    for j in range(39):
        if matrix[j][i] == 1:
            cox =i*20
            coy =j*20
            canvas.create_image(cox, coy, image=sprite1, anchor = NW)

        if matrix[j][i] == 2:
            cox =i*20
            coy =j*20
            canvas.create_image(cox, coy, image=sprite2, anchor = NW)

        if matrix[j][i] == 6:
            cox =i*20
            coy =j*20
            canvas.create_image(cox, coy, image=sprite8, anchor = NW)

        if matrix[j][i] == 7:
            cox =i*20
            coy =j*20
            canvas.create_image(cox, coy, image=bat1, anchor = NW)

        if matrix[j][i] == 8:
            cox =i*20
            coy =j*20
            canvas.create_image(cox, coy, image=bat2, anchor = NW)

for i in range(39):
    for j in range(40):
        if matrix[i][j] == 3:
            cox = j*20
            coy = i*20
            tlist[k].xco = j
            tlist[k].yco = i
            k = k + 1
            t = random.randrange(3)
            canvas.create_image(cox, coy, image=T1[t], anchor = NW)
            
        if matrix[i][j] == 4:
            cox = j*20
            coy = i*20
            tlist[k].xco = j
            tlist[k].yco = i
            k = k + 1
            t = random.randrange(3)
            canvas.create_image(cox, coy, image=T2[t], anchor = NW)
            
        if matrix[i][j] == 5:
            cox = j*20
            coy = i*20
            tlist[k].xco = j
            tlist[k].yco = i
            k = k + 1
            t = random.randrange(3)
            canvas.create_image(cox, coy, image=T3[t], anchor = NW)
            
co1, co2, co3, co4, co5, co6, co7, co8, co9, co10, co11, co12, co13, co14, co15, co16, co17, co18 = canvas.create_image(cox, coy, image=sprite1, anchor = NW), canvas.create_image(cox, coy, image=sprite1, anchor = NW), canvas.create_image(cox, coy, image=sprite1, anchor = NW), canvas.create_image(cox, coy, image=sprite1, anchor = NW), canvas.create_image(cox, coy, image=sprite1, anchor = NW), canvas.create_image(cox, coy, image=sprite1, anchor = NW), canvas.create_image(cox, coy, image=sprite1, anchor = NW), canvas.create_image(cox, coy, image=sprite1, anchor = NW), canvas.create_image(cox, coy, image=sprite1, anchor = NW), canvas.create_image(cox, coy, image=sprite1, anchor = NW), canvas.create_image(cox, coy, image=sprite1, anchor = NW), canvas.create_image(cox, coy, image=sprite1, anchor = NW), canvas.create_image(cox, coy, image=sprite1, anchor = NW), canvas.create_image(cox, coy, image=sprite1, anchor = NW), canvas.create_image(cox, coy, image=sprite1, anchor = NW), canvas.create_image(cox, coy, image=sprite1, anchor = NW), canvas.create_image(cox, coy, image=sprite1, anchor = NW), canvas.create_image(cox, coy, image=sprite1, anchor = NW)
cover1 = [co1, co2, co3, co4, co5, co6, co7, co8, co9, co10]
cover2 = [co11, co12, co13, co14, co15, co16, co17, co18]
ci = 0
bot1 = canvas.create_image(robot1.xco, robot1.yco, image=r1, anchor = NW)

#WISHLIST
path = []

for i in range(10):
    for j in range(10):
        if str(wishlist[i]) == str(tlist[j].var):
            path.append(tlist[j])

for i in range(10):
    print path[i].var

#POINTS
for i in range(10):
    tlist[i].points = int(lines[i])

#MOVEMENT
def movement(ntreasure):
    while robot1.xco != ntreasure.xco*20 or robot1.yco != ntreasure.yco*20:
        #RIGHT
        if robot1.xco < ntreasure.xco*20 and matrix[robot1.yco/20][(robot1.xco + 20)/20] != 2:
            r_right(20)
        if robot1.yco == ntreasure.yco*20 and matrix[robot1.yco/20][(robot1.xco + 20)/20] == 2 and robot1.xco < ntreasure.xco*20:
            r_up(20)
            r_right(20)
        #LEFT
        if robot1.xco > ntreasure.xco*20 and matrix[robot1.yco/20][(robot1.xco - 20)/20] != 2:
            r_left(20)
        if robot1.yco == ntreasure.yco*20 and matrix[robot1.yco/20][(robot1.xco - 20)/20] == 2 and robot1.xco > ntreasure.xco*20:
            r_up(20)
            r_left(20)
        #DOWN
        if robot1.yco < ntreasure.yco*20 and matrix[(robot1.yco + 20)/20][robot1.xco/20] != 2:
            r_down(20)
        if robot1.xco == ntreasure.xco*20 and matrix[(robot1.yco + 20)/20][robot1.xco/20] == 2 and robot1.yco < ntreasure.yco*20:
            r_right(20)
            r_down(20)
        #UP
        if robot1.yco > ntreasure.yco*20 and matrix[(robot1.yco - 20)/20][robot1.xco/20] != 2:
            r_up(20)
        if robot1.xco == ntreasure.xco*20 and matrix[(robot1.yco - 20)/20][robot1.xco/20] == 2 and robot1.yco > ntreasure.yco*20:
            r_right(20)
            r_up(20)

def r_right(finish):
    global bot1
    global ci
    v = 1
    s = robot1.xco
    canvas.itemconfig(bot1, image = r1)
    while v == 1:
        robot1.xco = robot1.xco + 1
        time.sleep(0.01)
        canvas.coords(bot1, robot1.xco, robot1.yco)
        canvas.update()
        if robot1.xco == s + finish:
            v = 0
    if matrix[robot1.yco/20][robot1.xco/20]==6 and len(taken) != 0:
        print 'Robot1 lost the last treasure worth', taken[len(taken)-1].points, "points. The robot's current score is", robot1.points - taken[len(taken)-1].points
        robot1.points = robot1.points - taken[len(taken)-1].points
        taken.remove(taken[len(taken)-1])
    if matrix[robot1.yco/20][robot1.xco/20]==7:
        robot1.points = robot1.points + 10
        print "Robot1 found a half charged battery on it's way and received 10 points."
        canvas.coords(cover2[ci], robot1.xco, robot1.yco)
        ci = ci + 1
        matrix[robot1.yco/20][robot1.xco/20] = 1
    if matrix[robot1.yco/20][robot1.xco/20]==8:
        robot1.points = robot1.points + 20
        print "Robot1 found a fully charged battery on it's way and received 20 points."
        canvas.coords(cover2[ci], robot1.xco, robot1.yco)
        ci = ci + 1
        matrix[robot1.yco/20][robot1.xco/20] = 1

def r_left(finish):
    global bot1
    global ci
    v = 1
    s = robot1.xco
    canvas.itemconfig(bot1, image = r2)
    while v == 1:
        robot1.xco = robot1.xco - 1
        time.sleep(0.01)
        canvas.coords(bot1, robot1.xco, robot1.yco)
        canvas.update()
        if robot1.xco == s - finish:
            v = 0
    if matrix[robot1.yco/20][robot1.xco/20]==6 and len(taken) != 0:
        print 'Robot1 lost the last treasure worth', taken[len(taken)-1].points, "points. The robot's current score is", robot1.points - taken[len(taken)-1].points
        robot1.points = robot1.points - taken[len(taken)-1].points
        taken.remove(taken[len(taken)-1])
    if matrix[robot1.yco/20][robot1.xco/20]==7:
        robot1.points = robot1.points + 10
        print "Robot1 found a half charged battery on it's way and received 10 points."
        canvas.coords(cover2[ci], robot1.xco, robot1.yco)
        ci = ci + 1
        matrix[robot1.yco/20][robot1.xco/20] = 1
    if matrix[robot1.yco/20][robot1.xco/20]==8:
        robot1.points = robot1.points + 20
        print "Robot1 found a fully charged battery on it's way and received 20 points."
        canvas.coords(cover2[ci], robot1.xco, robot1.yco)
        ci = ci + 1
        matrix[robot1.yco/20][robot1.xco/20] = 1

def r_up(finish):
    global bot1
    global ci
    v = 1
    s = robot1.yco
    canvas.itemconfig(bot1, image = r3)
    while v == 1:
        robot1.yco = robot1.yco - 1
        time.sleep(0.01)
        canvas.coords(bot1, robot1.xco, robot1.yco)
        canvas.update()
        if robot1.yco == s - finish:
            v = 0
    if matrix[robot1.yco/20][robot1.xco/20]==6 and len(taken) != 0:
        print 'Robot1 lost the last treasure worth', taken[len(taken)-1].points, "points. The robot's current score is", robot1.points - taken[len(taken)-1].points
        robot1.points = robot1.points - taken[len(taken)-1].points
        taken.remove(taken[len(taken)-1])
    if matrix[robot1.yco/20][robot1.xco/20]==7:
        robot1.points = robot1.points + 10
        print "Robot1 found a half charged battery on it's way and received 10 points."
        canvas.coords(cover2[ci], robot1.xco, robot1.yco)
        ci = ci + 1
        matrix[robot1.yco/20][robot1.xco/20] = 1
    if matrix[robot1.yco/20][robot1.xco/20]==8:
        robot1.points = robot1.points + 20
        print "Robot1 found a fully charged battery on it's way and received 20 points."
        canvas.coords(cover2[ci], robot1.xco, robot1.yco)
        ci = ci + 1
        matrix[robot1.yco/20][robot1.xco/20] = 1

def r_down(finish):
    global bot1
    global ci
    v = 1
    s = robot1.yco
    canvas.itemconfig(bot1, image = r4)
    while v == 1:
        robot1.yco = robot1.yco + 1
        time.sleep(0.01)
        canvas.coords(bot1, robot1.xco, robot1.yco)
        canvas.update()
        if robot1.yco == s + finish:
            v = 0
    if matrix[robot1.yco/20][robot1.xco/20]==6 and len(taken) != 0:
        print 'Robot1 lost the last treasure worth', taken[len(taken)-1].points, "points. The robot's current score is", robot1.points - taken[len(taken)-1].points
        robot1.points = robot1.points - taken[len(taken)-1].points
        taken.remove(taken[len(taken)-1])
    if matrix[robot1.yco/20][robot1.xco/20]==7:
        robot1.points = robot1.points + 10
        print "Robot1 found a half charged battery on it's way and received 10 points."
        canvas.coords(cover2[ci], robot1.xco, robot1.yco)
        ci = ci + 1
        matrix[robot1.yco/20][robot1.xco/20] = 1
    if matrix[robot1.yco/20][robot1.xco/20]==8:
        robot1.points = robot1.points + 20
        print "Robot1 found a fully charged battery on it's way and received 20 points."
        canvas.coords(cover2[ci], robot1.xco, robot1.yco)
        ci = ci + 1
        matrix[robot1.yco/20][robot1.xco/20] = 1

def ascendingFun():
    window = Toplevel()
    window.wm_title("Sorting")
    canvas = Canvas(window, width=800, height=780, bg='#cecece')
    canvas.pack()
    n = 1
    hisc = taken
    hasc = headings
    while(n == 1):
        n = 0
        for i in range(1,len(hisc)):
            if hisc[i-1].points > hisc[i].points:
                canvas.delete("all")
                j = 0
                while j < len(hisc):
                    if i == j or i == j + 1:
                        canvas.create_rectangle(j*70+40, (300-hisc[j].points/10), j*70+85, 780, fill='#fb4444', outline='#fb4444')
                        canvas.create_image(j*70+40, (250-hisc[j].points/10), image=hasc[j], anchor = NW)
                    else:
                        canvas.create_rectangle(j*70+40, (300-hisc[j].points/10), j*70+85, 780, fill='#5753ff', outline='#5753ff')
                        canvas.create_image(j*70+40, (250-hisc[j].points/10), image=hasc[j], anchor = NW)
                    time.sleep(0.3)
                    canvas.update()
                    j = j + 1
                aux = hisc[i-1]
                aux2 = hasc[i-1]
                hasc[i-1] = hasc[i]
                hisc[i-1] = hisc[i]
                hasc[i] = aux2
                hisc[i] = aux
                n = 1

    canvas.delete("all")
    j = 0
    while j < len(hisc):
        canvas.create_rectangle(j*70+40, (300-hisc[j].points/10), j*70+85, 780, fill='#5753ff', outline='#5753ff')
        canvas.create_image(j*70+40, (250-hisc[j].points/10), image=hasc[j], anchor = NW)
        time.sleep(0.3)
        canvas.update()
        j = j + 1

def descendingFun():
    window = Toplevel()
    window.wm_title("Sorting")
    canvas = Canvas(window, width=800, height=780, bg='#cecece')
    canvas.pack()
    n = 1
    disc = taken
    dasc = headings
    while(n == 1):
        n = 0
        for i in range(1,len(disc)):
            if disc[i-1].points < disc[i].points:
                canvas.delete("all")
                j = 0
                while j < len(disc):
                    if i == j or i == j + 1:
                        canvas.create_rectangle(j*70+40, (300-disc[j].points/10), j*70+85, 780, fill='#fb4444', outline='#fb4444')
                        canvas.create_image(j*70+40, (250-disc[j].points/10), image=dasc[j], anchor = NW)
                    else:
                        canvas.create_rectangle(j*70+40, (300-disc[j].points/10), j*70+85, 780, fill='#5753ff', outline='#5753ff')
                        canvas.create_image(j*70+40, (250-disc[j].points/10), image=dasc[j], anchor = NW)
                    time.sleep(0.3)
                    canvas.update()
                    j = j + 1
                aux = taken[i-1]
                aux2 = dasc[i-1]
                taken[i-1] = taken[i]
                dasc[i-1] = dasc[i]
                taken[i] = aux
                dasc[i] = aux2
                n = 1

    canvas.delete("all")
    j = 0
    while j < len(disc):
        canvas.create_rectangle(j*70+40, (300-disc[j].points/10), j*70+85, 780, fill='#5753ff', outline='#5753ff')
        canvas.create_image(j*70+40, (250-disc[j].points/10), image=dasc[j], anchor = NW)
        time.sleep(0.3)
        canvas.update()
        j = j + 1

def messageWindow():
    win = Toplevel()
    win.title('Treasure Sort')
    message = "Would you like the treasure to be sorted in ascending or descending order?"
    Label(win, text=message).pack()
    Button(win, text='Ascending', command=ascendingFun).pack()
    Button(win, text='Descending', command=descendingFun).pack()

taken = []

for i in range (len(path)):
    if robot1.points < 700:
        movement(path[i])
        print "Robot1 earned", path[i].points, "points. The robot's current score is", robot1.points + path[i].points, "."
        robot1.points = robot1.points + path[i].points
        taken.append(path[i])
        canvas.coords(cover1[i], robot1.xco, robot1.yco)
        matrix[robot1.yco/20][robot1.xco/20] = 1
    if robot1.points >= 700:
        messageWindow()
        break
            
window.mainloop()
