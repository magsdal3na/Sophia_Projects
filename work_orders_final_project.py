import locations
import technicians

#Defining variables
technician = ""
in_out = ""
location = ""
after_hours = ""
emergency = ""
ah_tech = "John White"

#Inside vs. Outside
while True:
  in_out = input("Is the issue inside or outside?").lower()

  if in_out == "inside":
    building = locations.building_select()
    break
  elif in_out == "outside":
    outdoors = input("Where is the issue located? ").strip()
    break
  else:
    print("Sorry, that's an invalid input. Please try again.")

#Buildings and their techs
while True: 
  if building == 1:
    technician = "Jane Doe"
    after_hours = input("Is it after hours? Yes or no.")
    break
  elif building == 2:
    technician = "John Smith"
    after_hours = input("Is it after hours? Yes or no.")
    break
  elif building == 3:
    technician = "Jackie Jones"
    after_hours = input("Is it after hours? Yes or no.")
    break
  elif building == 4:
    technician = "Jill Brown"
    after_hours = input("Is it after hours? Yes or no.")
    break
  elif building == 5:
    technician = "Jacob Taylor"
    after_hours = input("Is it after hours? Yes or no.")
    break
  elif building == 6:
    technician = "Jessica White"
    after_hours = input("Is it after hours? Yes or no.")
    break
  else:
    print("Sorry, that's an invalid input. Please try again.")

#After hours questions
while True:
  if after_hours == "yes":
    emergency = input("Is it an emergency? Yes or no.")
    break
  elif after_hours == "no":
    print("Please contact " + technician + ".")
    print("Thank you for using our work order system. The program will now close.")
    exit()
  else:
    print("Sorry, that's an invalid input. Please try again.")

#Emergency stipulations
while True:
  if emergency == "yes" and after_hours == "yes":
    print("Please contact " + ah_tech + " immediately.")
    print("Thank you for using our work order system. The program will now close.")
    break
  elif emergency == "yes" and after_hours == "no":
    print("Please contact " + technician + " immediately.")
    print("Thank you for using our work order system. The program will now close.")
    break
  elif emergency == "no" and after_hours == "no":
    print("Please contact " + technician + ".")
    print("Thank you for using our work order system. The program will now close.")
    break
  else:
    print("Sorry, that's an invalid input. Please try again.")

exit()
