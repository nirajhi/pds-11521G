## Programming for Data Science G (11521 Online & On-campus)
## WEEK 2 Tutorial
## Lecturer: Dr. Raul Fernandez-Rojas
## Tutor: Niraj Hirachan
## Date 9th August 2021
## Lab: 6B02/ Online

###Example 1
### Print function and input function

### Triple quote allows you to write code in multiple line.
"""
Programming for Data Science
Week 2 Tutorial
"""

#Output
print("Hello, World!")
#Input
x = input("Enter a number: ")
print("You have entered " + x)



###Example 2
### Datatypes in python

x = 5 #x is of type int
print(type(x)) #output type of x

###Example 3
### Datatypes in python
y = 7.9 #y is of type float
print(type(y))
z = 1 + 3j #z is of type complex and j is imaginary
print(type(z))
u = "Data Science" #u is of type str (string)
print(type(u))
v = 'Data Science' #v is of type str (string), too
print(type(u))
t = True #t is of type bool
print(type(t))

###Example 4
### Defining a variable
a, b = 'data', 'science'
print("a = " + a)
print("b = " + b)
c = d = 'python'
print('c = ' + c + ' and d = ' + d)


###Example 5
### Conversion of datatypes
a = 5 #a = 5
print(a)
b = float(a) #b = 5.0
print(b)
c = bool(b) #c = True
print(c)
d = str(c) #d = 'True'
print(d)
e = complex(a) #e = 5 + 0j
print(e)

###Example 6
###Output Formatting
name = 'Data Science'
print("Unit name = " + name)
myId = 123456
print('My ID is ' + str(myId))
print(f'My ID is {myId}')

###Example 7
### Multiline output.
print('Programming for Data Science\nWeek 2 Tutorial')
print("""Programming for Data Science
Week 2 Tutorial
""")

###Example 8
### Basic operations
s1 = 'abc'
s2 = 'def'
print(f's1 = {s1}')
print(f's2 = {s2}')
print(f's1 + s2 = {s1 + s2}')
print(f's1 * 2 = {s1 * 2}')
print('\n')
x1 = 5
x2 = 2
print(f'x1 = {x1}, x2 = {x2}')
x3 = x1 + x2
print(f'x1 + x2 = {x3}')
x3 = x1 - x2
print(f'x1 - x2 = {x3}')
x3 = x1 * x2
print(f'x1 * x2 = {x3}')
x3 = x1 ** x2 #power
print(f'x1 ** x2 = {x3}')
x3 = x1 / x2
print(f'x1 / x2 = {x3}')
x3 = x1 // x2 #divide and floor
print(f'x1 // x2 = {x3}')
x3 = x1 % x2 #modulo
print(f'x1 % x2 = {x3}')

###Example 9
### Assignment Operation
w=5
print(f'w = {w}')
w += 2
print(f'w += 2 -> w = {w}')
w -= 2
print(f'w -= 2 -> w = {w}')
w *= 2
print(f'w *= 2 -> w = {w}')
w /= 2
print(f'w /= 2 -> w = {w}')
w %= 2
print(f'w %= 2 -> w = {w}')


### Practice Question

###The base salary is $1200 a week. For every door that the carpenter sells, he/she will get $15 extra as bonus. In addition, at the end of each month, the carpenter gets 2% commission on the month’s sale.
base_salary = 1200
flat_bonus_per_sell = 15
commision_rate = 0.02

##he/she sells 35 doors and each door costs $150.
total_door_sold_count = 35
cost_per_door = 150

35* 150 * .02


##Calculate the carpenter’s total earnings in this month
total_earning = base_salary * 4  + flat_bonus_per_sell*total_door_sold_count + commision_rate*cost_per_door*total_door_sold_count
print(f"The carpenter’s total earnings in this month if he/she sells {total_door_sold_count} doors and each door costs ${cost_per_door} is {total_earning}.")
