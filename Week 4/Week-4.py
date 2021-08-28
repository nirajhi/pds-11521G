## Programming for Data Science G (11521 Online & On-campus)
## WEEK 4 Tutorial
## Title: Control Flow and Functions
## Lecturer: Dr. Raul Fernandez-Rojas
## Tutor: Niraj Hirachan
## Date 25th August 2021
## Lab: 6B02/ Online



import io_data_module as iodata
from tkinter import *


data_list = iodata.read_data_file('ellipse1.txt')

unknown_sample = (2.236779, 2.896883)

nearest_point = iodata.find_neared_neighbour(unknown_sample, data_list)

top = Tk()

c = Canvas(top, bg="white", height=700, width=700)


s = 90
r = 4

for x,y in data_list:
    x = x*s + 150
    y = y*s + 150
    c.create_oval(x-r,y-r,x+r,y+r, outline="red", fill="red")




x = unknown_sample[0]*s + 150
y = unknown_sample[1]*s + 150
c.create_oval(x-r,y-r,x+r,y+r, outline="grey", fill="grey")



x1 = nearest_point[0]*s + 150
y1 = nearest_point[1]*s + 150


c.create_line(x,y,x1,y1, fill = "blue")


c.pack()
top.mainloop()
ll
