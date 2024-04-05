import math
# ---------- QUESTION 1 ----------

print("""


  
      ___           ___           ___          _____    
     /  /\         /  /\         /  /\        /  /::\   
    /  /:/_       /  /::\       /  /::\      /  /:/\:\  
   /  /:/ /\     /  /:/\:\     /  /:/\:\    /  /:/  \:\ 
  /  /:/ /::\   /  /:/~/::\   /  /:/~/::\  /__/:/ \__\:|
 /__/:/ /:/\:\ /__/:/ /:/\:\ /__/:/ /:/\:\ \  \:\ /  /:/
 \  \:\/:/~/:/ \  \:\/:/__\/ \  \:\/:/__\/  \  \:\  /:/ 
  \  \::/ /:/   \  \::/       \  \::/        \  \:\/:/  
   \__\/ /:/     \  \:\        \  \:\         \  \::/   
     /__/:/       \  \:\        \  \:\         \__\/    
     \__\/         \__\/         \__\/                  






""")

# ---------- QUESTION 2 ----------

import math

SideNumberOne = int(input("Enter the first side of the triangle: "))
SideNumberTwo = int(input("Enter the second side of the triangle: "))
SideNumberThree = int(input("Enter the third side of the triangle: "))
s = (SideNumberOne + SideNumberTwo + SideNumberThree) / 2
x = s * (s - SideNumberOne) * (s - SideNumberTwo) * (s - SideNumberThree)
area = math.sqrt(x)
print("Therefore, the total area of the triangle is", round(area, 2))

# ---------- QUESTION 3 ----------

import math

#####INPUT#####

Budget = int(input("Enter your budget: "))
import random

######PROCESS######
rentvalue = random.uniform(0.25, 0.30)
Rent = round(rentvalue*Budget)

foodvalue = random.uniform(0.15, 0.20)
Food = round(foodvalue * Budget)

clothingvalue = random.uniform(0.10, 0.20)
Clothing = round(clothingvalue * Budget)

entertainmentvalue = 1.00 - (rentvalue+ foodvalue+ clothingvalue)
Entertainment = round(entertainmentvalue * Budget)

print(Rent, Food, Clothing, Entertainment)
print(rentvalue, foodvalue, clothingvalue, entertainmentvalue)


#######OUTPUT#######

print("You should keep a range of", Food, Clothing, Entertainment, Rent, "!")
print("\nBudget Breakdown:")
print(f"Food: ${Food} ({round(Food/Budget*100, 2)}%)")
print(f"Clothing: ${Clothing} ({round(Clothing/Budget*100, 2)}%)")
print(f"Entertainment: ${Entertainment} ({round(Entertainment/Budget*100, 2)}%)")
print(f"Rent: ${Rent} ({round(Rent/Budget*100, 2)}%)")


#double check

print(Food + Clothing + Entertainment + Rent)
print(foodvalue + clothingvalue + entertainmentvalue + rentvalue)
