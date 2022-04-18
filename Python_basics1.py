#2. STRINGS

#Create String

a = 'Python'
b = "Basics"
print(a+b)

#Length of String

a="Faster"
print(len(a))

a="S"
b=a*5
print(b)

#String Index

a="Learning"
print(a[3]) #identifing the element based on index
print(a[2:]) #Grab the remaing elements except upto the Index
print(a[:2]) #Grab the elements upto the Index
print(a[-1]) #Grab the Last element
print(a[:-1]) #Grab the elements except last element
print(a[::2]) #Grab everything with 2 steps
print(a[::-1]) #Print string backwards

#String Functions

a="Strings in python"
print(a.upper()) #Changing to Upper case
print(a.lower()) #Changing to Lowerb= a.split() case

b= a.split() #Splitting String
print(b)
print(b[1]) #Printing the splitting string based on Index

c="Ironman,Flash,CaptainAmerica"
d=c.split(",") #Splitting string based on Delimitter
print(d)
print(d[1])

a="Python Strings"
print(f"Welcome to {a} !") #Formatting string Literals
