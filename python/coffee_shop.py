#print("Hello, welcome to The Coffee Shop!!!!!!!!!!!!!!")


#name = input("What is your name?\n")


#Coffee Shop




print ("Welcome to the Coffee Shop!")

name = input("What is your name?\n")

if name == "Ben" or name == "Patricia":
  evil_status = input("Are you evil?\n")
  good_deeds=int(input("How many good deeds have you done today?\n"))
  if evil_status == "Yes" and int(good_deeds) < 5 :
    print("You're not welcome here " + name + " !! Get out!!")
    exit()
  else:
   print("Hello " + name + ", thank you so much for coming in today.\n\n\n")
    
else:
  print("Hello " + name + ", thank you so much for coming in today.\n\n\n")


beard= int(input ("How many inches is your beard?\n\n"))

if beard >= 5:
  print ("That's great, nice beard! You can skip the line and get a free coffee right away!")
  exit()

else:

  menu = "Black Coffee, Espresso, Cappucino, Latte, Frappuccino"

#print ("Hey, "+name + ", what would you like to drink? Here is what we are serving:\n"+menu) 

order =input("Hey, " + name + ", what would you like to drink? Here is what we are serving:\n" + menu + "\n")

number=input("Great! How many of these would you like?\n")

if order=="Frappuccino":
  price = 8
elif order=="Espresso":
  price=5
elif order =="Cappucino":
  price=7
elif order =="Black Coffee":
  price=9
elif order =="Latte":
  cream=input("Would you like to have whipped cream?\n")
  if cream=="Yes" or cream=="yes" or cream =="Y" or cream =="y":
      price = 11
  else:
    price=10
else:
  print("Sorry, we don't have that here.")

total=int(number)*price


print("Sounds good! We will have these "+number +" "+order+"s ready for you in a moment. That will be a total of "+str(total)+" USD.")



#num=input("How many of these would you like?\n")
#price=7
#total= int(num) * price

#print("Great! That will be a total of " + str(total) + " USD."