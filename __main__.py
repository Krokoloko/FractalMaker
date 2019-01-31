import tkinter as tk
from math import cos, sin, sqrt, atan2,pi 

arcs = int(input("give a amount of arcs "))
arcDistance = float(input("give a base distance for the arcs "))
maxRecursion = int(input("how many times do you want the circles to be drawn? "))

recursed = 0
first = True
defiation = (2*pi)/arcs

main = tk.Tk()

canvasSize = [int(800),int(800)]

canvas = tk.Canvas(main,width=canvasSize[0],height=canvasSize[1])
canvas.pack()
lastPositions = []

def distance(x0,y0,x1,y1):
    return sqrt((x0-x1)**2 + (y0-y1)**2)

def recurse():
    global recursed
    for i in range(arcs):
        if first:
            canvas.create_arc(canvasSize[0]/2,canvasSize[1]/2,
                              (canvasSize[0]/2)+(cos(defiation*i)*arcDistance),
                              (canvasSize[1]/2)+(sin(defiation*i)*arcDistance),style=tk.ARC,start=90+(360/(2*pi)*i),extent=(cos(defiation*i)*arcDistance))
            
            lastPositions.append([(canvasSize[0]/2)+(cos(defiation*i)*arcDistance),(canvasSize[1]/2)+(sin(defiation*i)*arcDistance)])
        else:
            canvas.create_arc(lastPositions[i*recursed][0],lastPositions[i*recursed][1],
                              lastPositions[i*recursed][0]+(cos(defiation*i)*arcDistance),
                              lastPositions[i*recursed][1]+(sin(defiation*i)*arcDistance),
                              style=tk.ARC,start=90+(360/(2*pi)*i),
                              extent=distance(lastPositions[i*recursed][0],lastPositions[i*recursed][1],
                              lastPositions[i*recursed][0]+(cos(defiation*i)*arcDistance),
                              lastPositions[i*recursed][1]+(sin(defiation*i)*arcDistance))/2)
            
            lastPositions.append([lastPositions[i*recursed][0]+(cos(defiation*i)*arcDistance),lastPositions[i*recursed][1]+(sin(defiation*i)*arcDistance)])
    recursed += 1
    '''if recursed is maxRecursion:
        recurse()'''


canvas.create_arc(-canvasSize[0],400,canvasSize[0],500,style=tk.ARC)
