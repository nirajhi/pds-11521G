## Programming for Data Science G (11521 Online & On-campus)
## WEEK 3 Tutorial
## Title: Control Flow and Functions
## Lecturer: Dr. Raul Fernandez-Rojas
## Tutor: Niraj Hirachan
## Date 17th August 2021
## Lab: 6B02/ Online

#Example 1
## Conditional Statements
x1 = 5
print(f'x1 = {x1}')
x2 = 2
print(f'x2 = {x2}')
if x1 == x2:
	print('x1 equals x2')
elif x1 < x2:
	print('x1 is less than x2')
else:
	print('x1 is greater than x2')


# print(x1 if x1 > x2 else x2)


##Example 2
## While loop
x=5
while x <= 10:
	x += 1
else:
    print(f'x = {x}')

##Example 3
x=0
while x <= 3:
	x += 2
	print(f'x = {x}')
5
##Example 4
assessments = ['tutorials', 'assignments', 'exams']
for assessment in assessments:
	print(assessment)


##Example 5
for c in 'data': #string data is a sequence of characters
	print(c)

##Example 6
while True:
	x = int(input('Enter a number : '))
	if x == 0:
		break
	print('The number is', x)
print('Done')

##Example 7
while True:
	x = int(input('Enter a positive number : '))
	if x == 0:
	    break
	elif x < 0:
		print('The number must be positive')
		continue
	print('The number is', x)
print('Done')

##Questions-1
while True:
	x = int(input('Enter a number : '))

	print(f"The square of {x} is {x*x}")

	question = input('Continue? (y/n)')
	if question == 'y':
		continue

	print('Done')
	break

#Example 8
#defining function
def welcome():
	print("Welcome to python function")

welcome()

##Example 9
#define function
def square(x):
	print('Square of ' + str(x) + ' is ' + str(x*x)) #end of function
   #call function
square(5)

##Example 10
def square(x):
	return x * x
#end of function
#call function
s = square(5)
print('Square of 5 is ' + str(s))


##Example 11
def distance(x1, y1, x2, y2):
       d = ((x2-x1)*(x2-x1) + (y2-y1)*(y2-y1))**0.5
       return d
x1 = 3
y1 = 0
x2 = 0
y2 = 4
dist = distance(x1, y1, x2, y2)
print('Distance between (3, 0) and (0, 4) is ' + str(dist))

##Example 12
def distance(p1, p2):
	d=0
	for i in range(len(p1)):
		d += (p2[i] - p1[i]) * (p2[i] - p1[i])
		d = d**0.5
		return d
   #end function
#call function
#Two points are two tuples (x, y)
p1 = (3, 0)
p2 = (0, 4)
dist = distance(p1, p2)
print('Distance between p1 and p2 is ' + str(dist))



########################## Questions  ########################

###Question 1
def calculate_grade(total_marks):
	'''Function to print the grade'''
	if total_marks >= 85:
		return('HD')
	elif total_marks >= 75:
		return('DI')
	elif total_marks >= 65:
		return('CR')
	elif total_marks >= 50:
		return('P')
	else:
		return('Fail')



###Question 2
total_marks = int(input('Enter total marks : '))
print(f'Your grade is {calculate_grade(total_marks)}')


## Question 3
while True:
	total_marks = int(input('Enter total marks : '))
	if total_marks <= 0:
		break
	print(f'Your grade is {calculate_grade(total_marks)}')


##Question 4
def find_max(*args):
	temp = 0
	for i in args:
		if i > temp:
			temp = i
	return temp

max_number = find_max(2, 4, 8, 3, 1, 33, 25, 65)
print(f"Maximun value {max_number}")

max = find_max(36, 52, 65)
print(f"Maximun value {max_number}")




##Drawing
from tkinter import *
top = Tk()

C = Canvas(top, bg="white", height=700, width=700)

x1 = 100
y1 = 100
x2 = 200
y2 = 300
C.create_line(x1, y1, x2, y2, fill = "blue")

C.create_oval(x1-2, y1-2, x1+2, y1+2, outline = "red", fill="red")
C.create_oval(x2-2, y2-2, x2+2, y2+2, outline = "red", fill="red")

C.pack()
top.mainloop()


