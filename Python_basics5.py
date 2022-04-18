#9. Function

#Initializing & Calling basic function

def welcome():
  print("Hello guyz Welcome to Python Bootcamp !!!")

welcome()

#Initializing & Calling basic function - With Argument

def welcome(a):
  print("Hello {0},Welcome to Python Bootcamp !!!".format(a))

welcome("Champ")

#Print & Return

def add(a,b):
  add = a+b
  print("Sum of {0} and {1} is {2}".format(a,b,add))

def addR(a,b):
  add = a+b
  return add

ans = addR(45,5)
final = ans*500
final

# Practice Project - Extracting Prime no.

def check(numbers):
    primeNumber = []
    for number in numbers:
      if number>1:
        for i in range(2, int(number/2)+1):
          if (number % i) == 0:#If number is divisible by any number between 2 and number / 2, it is not prime
              print(number, "is not a prime number")
              break
        else:
          print(number, "is a prime number")
          primeNumber.append(number)
      else:
        pass
    return primeNumber

check([2,3,4,5,6,7,8,9])

# 10 Map Function - Map a function to an iterable object

def cubeFn(num):
    return num**3

a = [1,2,3,4,5]
list(map(cubeFn,a))

#11. Filter Functions - Yields items of iterable in which function is true

def evenFn(num):
    return num % 2 == 0

a = [0,1,2,3,4,5,6,7,8,9,10]
print(list(map(evenFn,a)))
print(list(filter(evenFn,a)))

# 12. Lambda Fn - To create anonymous functions, without using def

#Normal Fn
def cubeFn(num):
    return num**3
cubeFn(6)

# LAMBDA
cubefn = lambda num: num**3
cubefn(5)

#13. *args and **kwargs

#Normal Fn. with Arguements
def addR(a,b,c,d):
  add = a+b+c
  return add
addR(10,20,30,40)

#Purpose of args
def addR(*argg):
  return sum(argg)
addR(10,20,30,40,52,75,8,5,26,15)

# **Kwargs - dictionary of key/value pairs

def func(**kwargs):
    if 'name' in kwargs:
        print("My Name is {0}".format(kwargs['name']))
    if 'age' in kwargs:
        print("My Age is {0}".format(kwargs['age']))
    else:
        print("No Key Found")
        
func(name='champ',age=24,marks=99)
