#Copyright ® 2018 Aymaan Shaikh
#Please Contact Before Using Code

from datetime import datetime
now = datetime.now()

 
#__________________________________________________________

def checkName(name):  
    checkName = input("Is your name " + name + "? ") 
    
    if checkName.lower() == "yes":    
      print("Hello,", name)
      print("Booting up Server", name)
    else:    
      print("We're sorry about that.")
checkName("Aymaan")

print("Next Code File!")

def checkNamet(namet):
    checkNamet = input("What is the " + namet + "? ")
    
    if checkNamet.lower() == "password":
      print("Access Granted Master!", namet)
    else:
      print("Database Locked, Access Deined!")
checkNamet("password")
print("Server Database booted.")
print("Running file 00001.....")  

print("Animals that are in secret zoo project being listed!")
animals = ["aardvark", "badger", "duck", "emu", "fennec fox"]
duck_index = animals.index("duck")# Use index() to find "duck"

# Your code here!
animals.insert(duck_index,"cobra")

print (animals)
#Next
print("Booting project 00002....")
menu = {} # Empty dictionary
menu['Chicken Alfredo'] = 14.50 # Adding new key-value pair
print (menu)

# Your code here: Add some dish-price pairs to menu!
menu['Hamburger'] = 8.50
menu['Pizza Slice'] = 3.50
menu['Salad'] = 10.00

print ("There are " + str(len(menu)) + " items on the menu.")
print (menu)
print("Booting Next project 00003....")
print("Spy Locater,finding spys in the area of 50 feet or less ")
print("Identifying.....")
namesa = ["Adam Ali","Alex","Mariah","Martine","Columbus"]

for namea in namesa:
  print (name)
print("Next Project Running....00004")


































