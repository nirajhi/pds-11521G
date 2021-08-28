
### Programing in Data Science
### Lab

import io_module as io
import tkinter as tk

ellipse_1= io.read_file("ellipse1.txt")
ellipse_2 = io.read_file("ellipse2.txt")



window = tk.Tk()

c = tk.Canvas(window, bg="white", height=400, width=400)

unknown_point = (2.23,2.89)


# equidelian  distance


r = 4
s=100

for x,y in ellipse_1:
    x = x * s + 150
    y = y  * s +150
    c.create_oval(x-r,y-r,x+r,y+r, color="red", fill="red")
    

x1 = unknown_point[0]
y1 = unknown_point[1]

c.create_oval(x1-r,y1-r,x1+r,y1+r)

c.pack()

window.mainloop()




