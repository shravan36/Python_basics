# 17 Python Modules & Libraries

#Accessing one Python program from another program


import main #importing python file
main.welcome() #parathesis (Func)
x = main.a #no paranthesis (variable)
y = main.b
print(x+y)

# Accessing python program from another Python program present in another Folder

from sample_data.demo import main
main.welcome()
x = main.a
y = main.b
print(x+y)

#Try Except Finally

#Base Exception Errors

"""
BaseException
 +-- SystemExit
 +-- KeyboardInterrupt
 +-- GeneratorExit
 +-- Exception
      +-- StopIteration
      +-- StandardError
      |    +-- BufferError
      |    +-- ArithmeticError
      |    |    +-- FloatingPointError
      |    |    +-- OverflowError
      |    |    +-- ZeroDivisionError
      |    +-- AssertionError
      |    +-- AttributeError
      |    +-- EnvironmentError
      |    |    +-- IOError
      |    |    +-- OSError
      |    |         +-- WindowsError (Windows)
      |    |         +-- VMSError (VMS)
      |    +-- EOFError
      |    +-- ImportError
      |    +-- LookupError
      |    |    +-- IndexError
      |    |    +-- KeyError
      |    +-- MemoryError
      |    +-- NameError
      |    |    +-- UnboundLocalError
      |    +-- ReferenceError
      |    +-- RuntimeError
      |    |    +-- NotImplementedError
      |    +-- SyntaxError
      |    |    +-- IndentationError
      |    |         +-- TabError
      |    +-- SystemError
      |    +-- TypeError
      |    +-- ValueError
      |         +-- UnicodeError
      |              +-- UnicodeDecodeError
      |              +-- UnicodeEncodeError
      |              +-- UnicodeTranslateError
      +-- Warning
           +-- DeprecationWarning
           +-- PendingDeprecationWarning
           +-- RuntimeWarning
           +-- SyntaxWarning
           +-- UserWarning
           +-- FutureWarning
       +-- ImportWarning
       +-- UnicodeWarning
       +-- BytesWarning"""

for i in range(3, -3, -1):
    try:
        print(1.0 / i)
    except ZeroDivisionError:
        print("You're trying to divide by zero. U IDIOT")

for i in range(3, -3, -1):
    try:
        print(1.0 / i)
    except ZeroDivisionError as er:
        print('Zero Division Error: ', str(er.args[0]))

def check():
    while True:
        try:
            a = int(input("Please Value of a in numbers: "))
            b = int(input("Please enter value of b in numbers: "))
        except:
            print("You did not entered numbers")
            continue
        else:
            print("Yes its Numbers")
            break
        finally:
            print("Execution Successfull")
            print(a+b)

check()

#Importing Library

import math #import libraryName

#Installing Library

!pip install imutils #pip install libraryName (! only while executing in colab, it is not needed in command window)

#uninstalling Library

!pip uninstall imutils #pip uninstall libraryName

import imutils

#Installing Library based on Version

!pip install imutils==0.5.4 #pip install libraryName==versionNumber

#Checking Installed Library version

import imutils
imutils.__version__

#Playing with Libraries

#Math Library


import math
print(dir(math))
print(math.pi)

import math as mt
print(dir(mt))
print(mt.pi)

#Reduce

from functools import reduce
lst =[47,11,42,13]
reduce(lambda x,y: x+y,lst)

#IPython

from IPython.display import Image
Image('https://venturebeat.com/wp-content/uploads/2018/09/ironman.jpg')

#Filter

def check(num):
    if num%2 ==0:
        return True
lst =range(20)
list(filter(check,lst))

#Counter

from collections import Counter
print(Counter([5,6,8,4,7,5,9,6,2,1,3,5,8,4,5,8,7,2,5,8,6,2,5,4,1,2,6,8,7,4,5,7,5,8,2,2,6])) #Numbers
print(Counter('sdasdasdadasdasdasdassdasdassdasdadasdaasdasdasd')) #String

#Regular Expression

import re
patt = r'\d{2}-\d{2}-\d{4}'
message = "His birthday is 16-11-2016"
re.findall(patt,message)

#Working with Files

f = open("welcome.txt", "r")
print(f.read())
f.close()

f = open("welcome.txt", "r")
print(f.read(5))
f.close()

f = open("welcome.txt", "r")
print(f.readline())
f.close()

f = open("welcome.txt", "r")
for x in f:
  print(x)

#File Handling using Pandas

!pip install pandas

import pandas as pd
data = pd.read_csv('data.csv')
print(data.to_string())

import pandas as pd
data = pd.read_csv('data.csv')
print(data.shape)
print(data.describe())
print(data.head(5))

#Working with Directories

import os
print(os.getcwd()) #current working directory
print(os.listdir())
os.mkdir("Junk")

import shutil
shutil.move('welcome.txt','/content/Junk')

import send2trash
os.listdir()
send2trash.send2trash('Junk/welcome.txt')

os.listdir()

#Time

import time
print(time.time())#time since epoch

import time
print(time.gmtime())

print (time.ctime())

startTime = time.time()
i=0
while(i<5):
  i+=1
  print(".")
  time.sleep(1) #delay 1 second
stopTime = time.time()
diff = stopTime - startTime
diff

#Date & Time

import datetime
x = datetime.datetime.now()
print(x)

import datetime
x = datetime.datetime(2021, 12, 16, 12, 30, 51) #(year, month, date, hour, minute, second, microsecond, tzone)
print(x)

# Commented out IPython magic to ensure Python compatibility.
# '''%a	Weekday, short version	Wed	
# %A	Weekday, full version	Wednesday	
# %w	Weekday as a number 0-6, 0 is Sunday	3	
# %d	Day of month 01-31	31	
# %b	Month name, short version	Dec	
# %B	Month name, full version	December	
# %m	Month as a number 01-12	12	
# %y	Year, short version, without century	18	
# %Y	Year, full version	2018	
# %H	Hour 00-23	17	
# %I	Hour 00-12	05	
# %p	AM/PM	PM	
# %M	Minute 00-59	41	
# %S	Second 00-59	08	
# %f	Microsecond 000000-999999	548513	
# %z	UTC offset	+0100	
# %Z	Timezone	CST	
# %j	Day number of year 001-366	365	
# %U	Week number of year, Sunday as the first day of week, 00-53	52	
# %W	Week number of year, Monday as the first day of week, 00-53	52	
# %c	Local version of date and time	Mon Dec 31 17:41:00 2018	
# %C	Century	20	
# %x	Local version of date	12/31/18	
# %X	Local version of time	17:41:00	
# %%	A % character	%	
# %G	ISO 8601 year	2018	
# %u	ISO 8601 weekday (1-7)	1	
# %V	ISO 8601 weeknumber (01-53)	01'''

import datetime
a = datetime.datetime(2021, 12, 16)
print(a.strftime("%a"))
