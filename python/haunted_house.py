#Bonus Lab Task
#Figure out a way to allow kids under 12 years old to enter the haunted house if they have a parent with them.



required_age = 12
print("Welcome to the haunted house!")
age = int(input("How old are you?" + "\n-->:"))


if age >= required_age:
  print("Go on in!")
  
elif age < required_age:
  parent=input("Do you have a parent with you?\n")
  if parent == "Yes":
   print("You are allowed to enter the haunted house.")
  else:
   print("You are not allowed to enter the haunted house.")







