#2018 Aymaan Shaikh


#Imports

from datetime import datetime

#Var
odds = [ 1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49, 51, 53, 55, 57, 59 ]

#String
right_the_min = datetime.today().minute

#Check Engine Light
#Basically the if statement
if right_the_min in odds:
  print("This miunte is odd!")
else:
  print("Ha you thought this was an odd minute!")
