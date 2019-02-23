
#Aymaan Shaikh
#@2019
#Introduction
import sys
#Reboot

print("Hello my name is AI, I am a meal tax and gratuity calculator!")
print(" ")

#User Input
user_name  = input("What is your name?")

print("It is very nice to meat you" + user_name)

def askYesNoQuestion(question):
  YesNoAnswer = input(question).upper()
  if YesNoAnswer == "YES" or YesNoAnswer == "NO":
     return YesNoAnswer  
  else:
     return askYesNoQuestion(question)
 
answer = askYesNoQuestion("Would you like to use this calculator? (Yes or No)")
if answer == "YES":
  print("Okay, then I will give you a series of questons in which you can answer with numbers.")
elif answer == "NO":
    print("Oh well, sorry to dissapoint" + user_name)
    print("I guess I will see you next time!")
    sys.exit()


meal = float(input("How much was the total price of your meal, " +  user_name + "?" ))
print(" ")
gratuity = float(input("How much gratuity would you like to give, " +  user_name + "?" ))
print(" ")
sales_tax = float(input("How much sales tax would you like to apply, "  +  user_name + "?" ))
print(" ")

#Formula 1
fake_total_cost = meal + (meal * sales_tax) + (meal * gratuity)

#Final User Input
deduction = float(input("Do you have any price deductions {Do not put a neagtive sign}, " +  user_name + "?" ))

#Formula 2
total_costz = fake_total_cost - deduction

#Finished AI Output
print("The total cost of your meal is: $ %.2f" % total_costz )
