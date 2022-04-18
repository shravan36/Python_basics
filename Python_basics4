#8.Python Statements

#If

a = True
if a:
  print("Positive")
else:
  print("negative")

a=10
b=6
c=6

if a<b:
  print("a less than b")
elif c==b:
  print("a is equal to b")
  print("a is not less than b")
  if c<a:
    print("c is less than b")
else:
  print("a is not less than b")

#For

a = [1,2,3,4,5,6,7,8,9,10]
for i in a:
  print(i)

a = [i for i in 'Champ']
a

#Odd & Even Number

a = [1,2,3,4,5,6,7,8,9,10]
for i in a:
  if i % 2 == 0:
    print(i,"Even Number")
  else:
    print(i,"Odd Number")

#String - For

for a in "Hello all":
  print(a)

#Dictionary - For

a = {"Name":"Elon","Age":50,"Company":["SpaceX","Tesla"]}
for k,v in a.items():
  print(k)
  print(v)

#While

a=0
while a <11:
  print(a)
  a+=1 #a=a+1

# While - Break & Continue

a=0
while a < 10:
  print(a)
  a+=1
  if a==5:
    print("a is equal to 5")
    break
  else:
    print("Continueeee")
    continue

#Range

for a in range (6):
  print(a)

for a in range (1,10,1):
  print(a)

for a in range (10,0,-3):
  print(a)

a = [i**2 for i in range(0,5)]
a

a = [i for i in range(10) if i % 2 == 0]
a

# Enumerate - To track no. of iteration in the loop, without working with variable increament

a=0
for i,a in enumerate("Hello Champ"):
  print(i,a)

# Zip - Creating a tuples by zipping 2 list

a = ["Name","Age","Country"]
b = ["Champ",27,"India"]
list(zip(a,b))
