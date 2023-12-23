# Names: Patrick Mc Grath & Julianna De Joya
# Date: 11/13/2023
# Desc: The user adds food to their paper plate without going over the weigh or area 
# limit. The user can select between two plates and five food options

import check_input
import smallplate
import largeplate
import turkey
import stuffing
import potatoes
import greenbeans
import pie

def examine_plate(p):
  '''displays hint of how much more food the plate can hold;
  sturdiness and space availability'''
  
  print(p.description())

  weight = False
  area = False
  
  if p.weight() >= 1 and p.weight() <= 6:
    weight = True
    if p.area() > 0:
      print("Sturdiness: Bending")
    
  elif p.weight() >= 7 and p.weight() <= 12:
    weight = True
    if p.area() > 0:
      print("Sturdiness: Weak")

  elif p.weight() >= 13:
    weight = True
    if p.area() > 0:
      print("Sturdiness: Strong")

  if p.area() >= 1 and p.area() <= 20:
    area = True
    if p.weight() > 0:
      print("Space avalilable: A tiny bit")

  elif p.area() >= 21 and p.area() <= 40:
    area = True
    if p.weight() > 0:
      print("Space avalilable: Some")

  elif p.area() >= 41:
    area = True
    if p.weight() > 0:
      print("Space avalilable: Plenty")

  if weight == True and area == True:
    return False

  elif weight == True and area == False:
    print("Your plate isn't big enough for this much food! Your food spills over the edge.")
    return True

  elif weight == False and area == True:
    print("Your plate isn't strong enough for this much food! Your food spills over the edge.")
    return True
  
  elif weight == False and area == False:
    print("Your plate isn't big enough or strong enough for this much food! Your food spills over the edge.")
    return True



def main():

  # title & description
  print("- Thanksgiving Dinner -")
  print("Serve yourself as much food as you like from the buffet, but make sure that your plate will hold without spilling everywhere!")

  # plate menu options
  print("Choose a plate:")
  print("1. Small Sturdy Plate")
  print("2. Large Flimsy Plate")
  user_choose_plate = check_input.get_int_range("", 1, 2)
  if user_choose_plate == 1:
    plate = smallplate.SmallPlate()
  else:
    plate = largeplate.LargePlate()

  user_choose_option = 0
  overflow = False

  while user_choose_option != 6 and overflow == False:

    
    # food menu options
    print("1. Turkey")
    print("2. Stuffing")
    print("3. Potatoes")
    print("4. Green Beans")
    print("5. Pie")
    print("6. Quit")
    user_choose_option = check_input.get_int_range("", 1, 6)


    # selected food option is added to plate
    if user_choose_option == 1:
      plate = turkey.Turkey(plate)

    elif user_choose_option == 2:
      plate = stuffing.Stuffing(plate)

    elif user_choose_option == 3:
      plate = potatoes.Potatoes(plate)

    elif user_choose_option == 4:
      plate = greenbeans.GreenBeans(plate)

    elif user_choose_option == 5:
      plate = pie.Pie(plate)

    # if user quits, display area and weight that wasn't used up
    else:
      print(plate.description())
      print(f"Good job! You made it to the table with {plate.count()} items.")
      print(f"There was still {plate.area()} square inches left on your plate.")
      print(f"Your plate could have held {plate.weight()} more ounces of food.")
      print("Don't worry, you can always go back for more. Happy Thanksgiving!")


    # if user doesn't quite, examine plate sturdiness and space available
    if user_choose_option != 6:
      overflow = examine_plate(plate)




main()