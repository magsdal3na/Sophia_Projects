drinkDetails=""
drink = input('What type of drink would you like to order?\nWater\nCoffee\nTea\nEnter your choice: ')

#water selection
if drink == "Water" or drink == "water":
  drinkDetails=drink
  temperature = input("Would you like your water? Hot or Cold: ")
  if temperature == "Hot" or "hot":
      drinkDetails += ", " + temperature
  elif temperature == "Cold" or temperature == "cold":
      drinkDetails += ", " + temperature
  ice = input("Would you like ice? Yes or No: ")
  if ice == "Yes" or "yes":
        drinkDetails += ", Ice"
  elif ice == "No" or "no":
        drinkDetails += ", No Ice"
  else:
      drinkDetails += ", unknown temperature entered."
    
#coffee selection
elif drink == "Coffee" or drink == "coffee":
  drinkDetails=drink
  decaf = input("Would you like decaf? Yes or No: ")
  if decaf == "Yes" or decaf == "yes":
      drinkDetails += ", Decaf"
  milkCream = input("Would you like Milk, Cream or None: ")
  if milkCream == "Milk" or milkCream == "yes":
      drinkDetails += ", Milk"
  elif milkCream == "Cream" or milkCream == "cream":
      drinkDetails += ", Cream"
  sugar = input("Would you like sugar? Yes or No: ")
  if sugar == "Yes" or sugar == "yes":
      drinkDetails += ", Sugar"
  
#tea selection
elif drink == "Tea" or drink == "tea":
  drinkDetails=drink
  teaType = input("What type of tea would you like? Black or Green: ")
  if teaType == "Black" or teaType == "black":
      drinkDetails += ", " + teaType
  elif teaType == "Green" or teaType == "green":
      drinkDetails += ", " + teaType
else:
  print("Sorry, we did not have that drink available for you.")
print("Your drink selection: ",drinkDetails)
