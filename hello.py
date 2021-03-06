# 1st Code
# print ('Hello World')

# 2nd Code
# x = y = z = 50
# a = int(x) + int (y) * int (z)
# print(a)

# 3rd Code
# a,b,c = 5,10,20
# print(a)
# print(b)
# print(c)

# 4th Code 
# adarsh = ('Adarsh is Hero')
# print(adarsh)

#5th Code
# for x in range(100):
#   print(x) 

# 6th Code
# a  = "Hello, World"
# print (a[-5:-2])

# 7th Code

# age  = 37
# txt = "My name is Adarsh , my age is {}"
# print(txt.format(age))

# 8th Code
# quantity = 3
"""itemnp  = 567
price = 49.5
myorder = "I Want {0} piece of Wine"
print(myorder.format(quantity))"""

# 9th Code
# txt = "ADARSH"
# print(txt.casefold())

# 10th Code
# from requests import requests
# import requests
# import json
# response = requests.get("http://api.open-notify.org/astros.json")
# response = response.json()
# print(response)

# 1st Code
"""x = input ('Please Enter Your First Number: ')
y = input ('Please Enter The Second Number: ')

temp = x
x = y 
y = temp

print('The value of First Number after Swapping: {}'.format(x))
print('The Value of Second Number after Swapping: {}'.format(y))"""

# 2nd Code
"""import random

a = [1,2,3,]
print(a.randint()"""

# 3rd Code

# kilometer = float(input('Please Enter kilometer: '))
# convertFormula = 0.62137
# miles = kilometer * convertFormula 

# print(miles)

# 4th Code

"""celsius = float(input('Please Enter Celsius: '))
fehrenheitFormula = 1.8

fehrenheit = (celsius * fehrenheitFormula) + 32

print(fehrenheit)"""

# 5th Code
#  x=["apple","banana","cherry"]
#  print(x)

# 1st Quiz
# print(36/4)
# print(10-4*2)
# a = 4 
# b = 11
# print(a | b)
# print(a>>2)
# print(2%6)
# print (2*3**3*4)
"""x = 6 
y = 2
print(x**y)
print(x//y)"""
"""str = "pynative"
print(str[1:3])"""

"""valueOne = 5**2
valueTwo = 5**3
print(valueOne , valueTwo)"""

# x = 36 /4 *(3+2)*4+2
# print(x)

# quadratic equations

"""import cmath

a = float(input('Please Enter First Number'))
b = float(input('Please Enter Second Number'))
c = float(input('Please Enter Third Number'))

d = (b**2) - (4*a*c)
print("Discriminant = {0}".format(d))
first = (-b-cmath.sqrt(d))/(2*a)
second = (-b+cmath.sqrt(d))/(2*a)
print("The solutions are {0} and {1}".format(first,second))"""

"""import calendar

yy = int(input("Enter Year: "))
mm = int(input("Enter Month: "))

print(calendar.month(yy,mm))"""

"""praveen = int(input("Enter the Number"))
if praveen % 2 == 0:
  print("Praveen is even")
else:
  print("Praveen is not even")"""

"""mm = "Praveen"

for element in range(100, len(mm)): 
    print(mm[element]) """


"""counter = 0

while counter <= 5:
    print("Inside loop")
    counter = counter + 1"""

"""n = 5
while n > 10:
    n -= 1
    if n == 2:
        continue
    print(n)
print('Loop ended.')"""

"""i = 1
while i<=10:
   print(i)
   i = i+ 1"""


"""num = 7


factorial = 1

# check if the number is negative, positive or zero
if num < 0:
   print("Sorry, factorial does not exist for negative numbers")
elif num == 0:
   print("The factorial of 0 is 1")
else:
   for i in range(1,num + 1):
       factorial = factorial*i
   print("The factorial of",num,"is",factorial)"""

"""n = int(input("Enter The Number"))
f = 1
i = 1
while i<=n:
  f = f*i 
print("Factorial is {}:".format(f))

n = input("Enter a number: ")
factorial = 1
if int(n) >= 1:
for i in range (1,int(n)+1):
   factorial = factorial * i
print("Factorail of ",n , " is : ",factorial)"""


"""number = int(input("Enter number:"))
factorial = 1
while number>0:
    factorial = factorial * number
    number = number - 1
print(factorial)"""

"""num = int(input("Enter The Number"))

for i in range(1,11):
  print(num,'x',i,'=',num*i)"""

"""num = int(input("Enter the number"))
sum = 0
temp = num 
while temp>0:
  digit = temp%10
  sum += digit**3
  temp//=10
if num == sum:
  print(num, "is an armstrong number")
else:
  print(num, "is not an armstrong number")"""

"""num = int(input("Enter the Number"))
sum = 0
for i in range(num+1):
  sum = sum + i
print(sum)"""

# thisList = ["apple", "banana", "cherry","orange","kiwi"]
# thisList1 = [1,2,3,4,5,6]

# for x in thisList1:
#   thisList.append(x)
# print(thisList)

# mohit = [
#   "NAME": "Mohit Kumar",
#   "AUID": "AGS19ABCA011",
#   "TYPE": "Student", 
#   "Course": "BCA"
# ]

# print(mohit["AUID"])

# MOHIT = {
#  "gold": 1271,
#  "silver": 1284,
#  "platinum": 1270
# }

# print(MOHIT.gold)


"""myNumber = int(input("Enter the number"))
for i in range(myNumber):
  if myNumber%3 == 0 and myNumber%5 == 0:
    print('FizzzzzBuzzzz')
    continue
  elif myNumber%3 == 0:
    print('Fizzz')
    continue
  elif myNumber%5 == 0:
    print('buzz')
  continue
  else:
  print(i)"""

# firstMark = int(input("Enter the first mark"))
# secondMark = int(input("Enter the Second mark"))
# thirdMark = int(input("Enter the Third mark"))
# fourtMark = int(input("Enter the Forth Mark"))

# totalMarks = firstMark + secondMark + thirdMark + fourtMark
# print("Total Marks = {}".format(totalMarks))

# average = totalMarks / 4
# print(average)

# sum = 0
# for i in range(4):
#   x = int(input("Enter the {} ".format(i)))
#   sum = sum + x
# print("Marks:{}".format(sum))
# average = sum / (i+1)
# print(average)
# n = int(input("Enter number"))
# d = dict()
# for i in range(1,n+1):
#   d[i]=i*i
# print(d)

# def mohitAdd(a,b):
#   print("Your Sum : ", a+b)

# x = int(input("Enter One Number "))
# y = int(input("Enter Two Number "))
# mohitAdd(x,y)


# def factorial(n): 
#   f = 1
#   for i in range(1,n+1):
#     f = f*i 
#   print("Factorial:", f)
# n = int(input("Enter The Number "))
# factorial(n)

# def mohitFunction(kids,kids1,kids2):
#   print("My Youngest child is " + kids)
# mohitFunction(kids = "Praveen", kids1 = "Amrut", kids2 = "Mohit")

# myList = ["apple", "banana", "cherry"]

# def myFunction(myList):
#   print(mylist)

# myFunction()

# double = lambda x:x**3
# print(double(5))
# class myClass:
#   myList = [1,5,6,8,11,17]
# classssss = myClass()
# print(classssss.myList[2])
# newList = list(map(lambda x:(x*2),myList))
# print(newList)

"""class Person:
  def __init__(self,name,age):
    self.name = name
    self.age = age
p1 = Person("John",36)
dataP1 = f"My name is {p1.name} and age is {p1.age}"
print(dataP1)"""

class Employee:
  def __init__(self,name,id):
    self.name = name
    self.id = id
  def display(self):
    print(self.id,self.name)
emp1 = Employee("Mohit", 20)
emp2 = Employee("Raj",32)

emp1.display()
emp2.display()
