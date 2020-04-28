#!/usr/bin/python
# -*- coding: utf-8 -*-

from math import *
import numpy as np
import matplotlib as mlp
import matplotlib.pyplot as plt
from pdb import set_trace as bp
import code

ECKEN=5
ANGLE=2*pi/ECKEN

STRETCHING=50    #mm
CENTER=[200,100]
GAP=7 #mm


def calcstar(stretch):
    star=[]
    pentagon=[]
    for i in range(5):
        x= round(sin((radians(72)*i))*stretch,2)
        y= round(cos((radians(72)*i))*stretch,2)
        pentagon.append([x,y])
    print(pentagon)

    X=np.array(pentagon)
    A0=X[0]
    B0=X[1]
    b=B0-A0
    babs=np.linalg.norm(b)
    # r = kreisradiuis des inneren Kreises
    r=tan(radians(54))*babs/2-tan(radians(36))*babs/2

    #cabs=np.linalg.norm(b) * sin(radians(36)) / sin(radians(108))
    #y=sin(radians(36))*cabs
    #x=cos(radians(36))*cabs
    #c=np.array([x,y])
    #code.interact(local=locals())

    for i in range(ECKEN):
        x= round(sin(radians(72)*i+radians(36))*r,2)
        y= round(cos(radians(72)*i+radians(36))*r,2)
        star.append([pentagon[i][0], pentagon[i][1]]) #pentagon array an stern anhängen
        star.append([x,y])
    return star

def calcledpos(star):
    starshape=np.array(star)
    leds=[]
    for i in range(10):
        starp1      = starshape[i]           # erster eckpunkt
        starp2      = starshape[(i+1)%10]    # zweiter eckpunkt
        vricht      = starp2 - starp1        # richtungsvektor ledpositionen
        led1        = starp1 + 1/3*vricht    #
        led2        = starp1 + 2/3*vricht    #

        leds.append([starp1[0], starp1[1]])  # erster eckpunkt, schlussendlich sind alle eckpunkte vorhanden
        leds.append([led1[0], led1[1]])
        leds.append([led2[0], led2[1]])

    return leds

def calcledangle(led):
    ledpos=np.array(led)
    ledangles=[]

    return 0



def outlinefileoperations(star):
    layer = 'layer Margin'

    pcb = open("../hardware/movingstar/movingstar.kicad_pcb",'r+')
    #pcb = open("../hardware/movingstar/pcb",'r+')
    x=0
    offset=0
    tstamp=0
    for num, line in enumerate(pcb,1):
        if layer in line:
            x=num
            print(num)
            #x2=line.find("tstamp")
            #print(x2)
            #tstamp=line[(x2+7):-3]
            #print(tstamp)
            break
        offset+=len(line)


    pcb.seek(offset)

    tstamp="5E76F76E"

    for i in range(10):
        pcb.write("(gr_line (start %.2f %.2f ) (end %.2f %.2f) (%s) (width 0.15)" %
            (CENTER[0]+star[i][0], CENTER[1]-star[i][1],
             CENTER[0]+star[(i+1)%10][0], CENTER[1]-star[(i+1)%10][1] ,layer))

        if i==9:
            pcb.write(" (tstamp %s)" % tstamp)
        pcb.write(")\n")

      #(tstamp 5E76F76E))
    pcb.write("\n")
    pcb.close()

def ledfileoperations(leds):
    LINEOFFSET=4

    pcb = open("../hardware/movingstar/movingstar.kicad_pcb",'r+')
    #pcb = open("../hardware/movingstar/pcb",'r+')

    x=0
    offset=0
    tstamp=0
    for num, line in enumerate(pcb,1):
        if layer in line:
            x=num
            print(num)
            x2=line.find("tstamp")
            print(x2)
            tstamp=line[(x2+7):-3]
            print(tstamp)
            break
        offset+=len(line)





def plot(starout,starin, leds):

    ax = plt.axes()

   # plt.scatter(*zip(*pentagon))
    plt.plot(*zip(*starout))
    plt.plot(*zip(*starin))

    plt.scatter(*zip(*leds))

    plt.axis([-STRETCHING , STRETCHING , -STRETCHING , STRETCHING])
    plt.grid=(True)

    ax.set_aspect(1)
    theta = np.linspace(-np.pi, np.pi, 200)
    plt.plot(np.sin(theta), np.cos(theta))

    plt.show()

if __name__ == "__main__":
    outlinestar=[]
    placingstar=[]

    outlinestar=calcstar(STRETCHING)
    placingstar=calcstar(STRETCHING-GAP)
    ledpos=calcledpos(placingstar)

    print("LED Positionen")

    for x in range(30):
        print( "%.2f , %.2F" %(CENTER[0]+ledpos[x][0], CENTER[1]-ledpos[x][1] ))
        #print( "%.2f , %.2F" %(x[0], x[1] ))

    print("Inlinecutout")
    cutouts=calcstar(36)

    for x in range(10):
        print( "%.2f , %.2F" %(CENTER[0]+cutouts[x][0], CENTER[1]-cutouts[x][1] ))



    plot(outlinestar,placingstar, ledpos)
    #outlinefileoperations(outlinestar)
