#2018 Aymaan Shaikh
#

#Variables and Data Types review
#1.create a varible called inVal and assign it an integer value
#2.create a varible called floatVal and assign it a float value
#3.create a varible called booVal and assign it a float value
#4.use print() to display the Boolean value assigned to boolVal in the output of the program
#5.reassign boolVal a diffrent Boolean value than the one assigned in step 3
#6.use print() to display the integer value assigned to floatVal in the output of the program
#7.use print() to display the float value assigned to floatVal in the outpit of the proggrAM
#8.use print() to display the Boolean value reassigned to boolVal in the output of the program


intVal = 5
#1

floatVal = 2.21
#2

boolVal = False
#3

print(boolVal)
#4

boolVal = True
#5

print(intVal)
#6

print(floatVal)
#7

print(boolVal)
#8
#end

#LECT05

add = 3+2
sub = 9-6
div = 10/5
prod = 4*7

operators1 = 2
operators2 = 2
operators3 = 2

operators1 **= 2
operators2//= 0.5
operators3 %= 1

print(add, sub, div, prod)
print(operators1, operators2, operators3)
#endLECT 05

#Lect 06
#Strings and Escape Sequences review
#1.print a string surrounded by single quotes
#2.print a string surrounded by double quotes
#3.use an escape sequence to surroun the "in quotes" from the string
#4.create a varible and assign it the string "Alligator"
#5.access the "a" from the varible you created in step 4
print( 'single quotes')
#1

print( "double quotes")
#2

print("This should be \"in quotes\".")
#3

gator = "Alligator"

print(gator[5])
#4

print(gator[:4])
#5

print(gator[4:7])

print(gator[6:])
#endLect 06

#Lect 07
#print() review

name = input("Please enter your name.")

print("Your name is " + "%s" % (name))
#endLect 7

#Lect 08
#Flow Control and Comparators review

print(8 >8)
print(6<=6)
print(5<5)
print(10 != 10)
print(4 == 5)
print( 7>= 7)
print(7 !=9)
print(5 < 9)

#endLect 08

#Lect 09
#Boolean Operators review
#For this review exercise, guess wehether the statment in the parentheses of print evaluate to True or False

print(7 >6 and 6>= 6)
print(3 !=3 or 4 ==4)
print(not 5 >2)
print(not 5<3 and True or 6 <= 6 and not False)

#end Lect 09

#Lect 10

#If, Else, and Elif review

name = input("Enter your name")

nameLen = len(name)

if nameLen < 4:
    print("Your name is less than 4 characters long.")
elif nameLen <10:
    print("You name is at least 4 characters and less than 10 characters ")
else:
    print("Your name is very long")
#endLect 10

#Lect 11
#Function review

def first():
    print("This is a function")

def intFun(intVal):
    return intval * 2

def takesTwo(int1, int2):
    return int1 * int2

def functionInside(a, b, c):
    print (takesTwo(intFun(a), b) * c)

first()

functionInside(7, 4, 2)
