import tkinter as tk
import math

arcs = input("give a amount of arcs ")
arcDistance = input("give a base distance for the arcs ")
defiation = (2*math.pi)/float(arcs)
main = tk.Tk()

canvasSize = [int(800),int(800)]

canvas = tk.Canvas(main,width=canvasSize[0],height=canvasSize[1])
canvas.pack()
lastPositions = []
recursed = 0
first = True

def recurse():
    
    for i in range(arcs):
        if first:
            canvas.create_arc(canvasSize[0]/2,canvasSize[1]/2,
                              (canvasSize[0]/2)+(math.acos(defiation*i)*arcDistance),
                              (canvassize[1]/2)+(math.asin(defiation*i)*arcDistance))
            lastPositions.append([(canvasSize[0]/2)+(math.acos(defiation*i)*arcDistance),(canvassize[1]/2)+(math.asin(defiation*i)*arcDistance)])
        else:
            canvas.create_arc(canvasSize[0]/2,canvasSize[1]/2,
                              (canvasSize[0]/2)+(math.acos(defiation*i)*arcDistance),
                              (canvassize[1]/2)+(math.asin(defiation*i)*arcDistance))
            lastPositions.append([lastPositions*(recursed-1)+(math.acos(defiation*i)*arcDistance),(canvassize[1]/2)+(math.asin(defiation*i)*arcDistance)])
    recursed += 1
    first = False
    recurse()



