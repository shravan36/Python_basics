# 15 Python Decorators - functions which modify the functionality of another function/Class

'''@decName
def func():
    print("statement")

EQUAL TO

def func():
    print("statement")
    
func = decName(func)'''

#FUNCTION AS OBJECT

def welcome(a):
  print("Hello {0},Welcome to Python basics !!!".format(a))

a = welcome #No paranthesis, if its paranthesis it will call fn. - FUNCTION AS OBJECT
a("basics")

#FUNCTION IN VARIABLE

def lowerCase(text):
  return text.lower()

def upperCase(text):
  return text.upper()

def a(welcome):
  message = welcome("Hello all, Welcome to Python Basics") #FUNCTION IN VARIABLE
  print(message)

a(lowerCase)
a(upperCase)

def lowerCase(text):
  return text.lower()

def a(welcome):
  message = welcome("Hello all, Welcome to Python Basics") #FUNCTION IN VARIABLE
  print(message)

a(lowerCase)

#RETURNING FUNCTION FROM ANOTHER FUNCTION

def addMain(a):#child
  def addSub(b): #parent  = a+b
    print(a,b)
    return a+b #apple
  return addSub #return of parent is return of child now - apple {child = return(parent)}

addition = addMain(100)
print(addition(75))

#DECORATORS in Action

def decoratorFunc (welcome):#2. Decorator
  def a(): #3. can access the outer local functions like in this case "welcome"
    print("Start")
    welcome() #4.calling actual fn.
    print("End")
  return a

def subFunc(): #veg with cheese
  print("Sub fn")

subFunc = decoratorFunc(subFunc) #1. subFunc inside the decorator to control behavior

subFunc()

# 16 Python Generators -  to generate as we go along, instead of holding everything in memory & generator functions will automatically suspend and resume their execution and state around the last point of value generation | n. This feature is known as state suspension

def square(n):
  for i in range (n):
    yield i**2

for n in square(10):
  print(n)

#Builtin Function - next

def square():
  for i in range (n):
    yield i**2

a = square()

print(next(a)) #After yielding all the values next() caused a StopIteration error

#Builtin Function - iter

a = "Basics"
for i in a:
  print(i)

next(a)

iterOper = iter(a)

next(iterOper)
