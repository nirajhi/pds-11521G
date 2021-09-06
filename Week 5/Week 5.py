## Programming for Data Science G (11521 Online & On-campus)
## WEEK 4 Tutorial
## Title: Control Flow and Functions
## Lecturer: Dr. Raul Fernandez-Rojas
## Tutor: Niraj Hirachan
## Date 1st September 2021
## Lab: 6B02/ Online

#Question 1: Create a list of 100 elements like this [0, 1, 2, 3, 4, ..., 99]
list_example = []

for i in range(0,100):
    list_example.append(i)

##alternative

new_list = list(range(0, 100, 1))

# • Question 2: Create a tuple of 100 elements like this (0, 1, 2, 3, 4, ..., 99)
tuple_example = tuple(new_list)


# • Question 3: Change values of input_list from string to number and output as output_list
input_list=['2.1','3.5','4.8','1.1','2.0']
output_list = []
for item in input_list:
    try:
        output_list.append(float(item))
    except:
        output_list.append(0.0)

### alternative solution
output_list_1 = [float(item) for item in input_list]


# • Question 4: Change each element x in a list to x / sum where sum is total of all elements in that list. For example, mylist = [0, 2, 1, 3, 1, 2, 0, 1] and sum =
# 0+2+1+3+1+2+0+1 = 10 and mylist becomes [0.0, 0.2, 0.1, 0.2, 0.3, 0.2, 0.0, 0.1]

mylist = [0, 2, 1, 3, 1, 2, 0, 1]

##Sum of all elements in mylist
mylist_sum = sum(mylist)

for index,item in enumerate(mylist):
    mylist[index] = item / mylist_sum



# • Question 5: Remove the first and last elements from a list. For example,
my_list = ['red', 0, 2, 1, 1, 2, 0, 1, 'blue']

my_list = mylist[1:-1]


# • Question6: Change 0 to 10 in list


my_list = [0,1,0,2,0,1]

for key,items in enumerate(my_list):
    if items == 0:
        my_list[key] = 10

my_list


# • Question 7: Combine list1 and list2 to have list3, list4 and list5 as follows o

list1 = [2,3,1]
list2 = [4,5,2]

list3 = list1 + list2

list4 = [list1,list2]

list5 = [tuple(list1),tuple(list2)]

#Question 8 Write a function (read_multi_dim_data) in io_data_module.py that reads data from
#iris.data file and outputs a list of tuples where each tuple is a data sample.
def read_data_file(filename):
    dataset = []
    f = None
    try:
        f = open(filename, 'r')
        while True:
            line = f.readline()
            if len(line) == 0:#end of file
                break
            print(line + "1")
            line = line.replace('\n', '') #remove end of line \n character
            xystring = line.split(',') #x y coordinates in string format
            dataset.append((float(xystring[0]),float(xystring[1]),float(xystring[2]),float(xystring[3])))

    except Exception as ex:
        print(ex.args)
    finally:
        if f:
            f.close()
    return dataset

iris_data = read_data_file("data/iris.data")
print(iris_data)



#Question 9

import tkinter as tk

top = tk.Tk()

centre_1=(5.1,3.0,1.1,0.5)
centre_2=(4.4, 3.2, 2.8, 0.2)
centre_3 = (5.7, 3.9, 3.9, 0.8)

centers = [centre_1, centre_2, centre_3]

c = tk.Canvas(top, bg="white", height=700, width=700)

## Defining the scaling factor and radius of the circle
s = 90
r = 4

### Ploting the coordinate for iris data.
for x,y,_,_ in iris_data:
    x = x*s
    y = y*s
    c.create_oval(x-r,y-r,x+r,y+r, outline="red", fill="red")


### Plotting the centers for iris data
for x,y,_,_ in centers:
    x = x*s
    y = y*s
    c.create_oval(x-r,y-r,x+r,y+r, outline="black", fill="black")


c.pack()
top.mainloop()





