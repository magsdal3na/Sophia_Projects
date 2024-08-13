import locations

#Defining variables
technician = ""
in_out = ""
location = ""
after_hours = ""
emergency = ""

in_out = input("Is the issue inside or outside?").lower()

if in_out == "inside":
  building = locations.building_select()
elif in_out == "outside":
  outdoors = input("Where is the issue located? ").strip()
else:
  print("Sorry, that's an invalid input. Please try again.")
