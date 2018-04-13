#1
name = raw_input("What is your name? ")
print "Hello, " + name + "!"

#2 
name = raw_input("WHAT IS YOUR NAME? ")
new_string = "HELLO, "+ name + "!"
print new_string.upper()
print "YOUR NAME HAS " + str(len(name)) + " LETTERS IN IT!"

#3
name= raw_input("Give me a name. ")
job= raw_input("Give me a job. ")
job2= raw_input("Give me another job. ")
print "%s is a %s trying to become an %s" % (name, job, job2)

#4
day = int(input('Day (0-6)? '))
if day == 0:
  print "Sunday"
elif day == 1:
   print "Monday"
elif day == 2:
   print "Tuesday"
elif day == 3:
   print "Wednesday"
elif day == 4:
   print "Thursday"
elif day == 5:
   print "Friday"
elif day == 6:
   print "Saturday"
else:
   print "That number is not between 0 and 6"

#5
while True:
    day = int(input('Day(0-6)? '))
    if 0 <= day <= 6:
        break
    else:
        print("Please input a number between 0~6!")
        continue
if 1 <= day <= 5:
    print("Go to work")
else:
    print("Sleep in")

#6
cel = int(input("Temperature in Celsius? "))
far = cel * 1.8 + 32
print str(cel) + " degrees Celsius is equal to "+ str(far) +" degrees Fahrenheit."

#7
total = int(input("What was your total bill amount? "))
service = raw_input("Was the service Great, Decent, or Terrible? ")
service = service.lower()
if service == "great":
   tip = (.20 * total)+total
   print "With a 20% tip you will pay " + "$" + str("%.2f"%tip)+"."
elif service == "decent":
   tip = (.15 * total)+total
   print "With a 15% tip you will pay " + "$" + str("%.2f"%tip)+"."
elif service == "terrible":
   tip = (.10 * total)+total
   print "With a 10% tip you will pay " + "$" + str("%.2f"%tip)+"."

#8
total = int(input("What was your total bill amount? "))
split = int(input("How many ways would you like to split the bill? "))
total = total/split
service = raw_input("Was the service Great, Decent, or Terrible? ")
service = service.lower()
if service == "great":
   tip = (.20 * total)+total
   print "With a 20% tip you will each pay " + "$" + str("%.2f"%tip)+"."
elif service == "decent":
   tip = (.15 * total)+total
   print "With a 15% tip you will each pay " + "$" + str("%.2f"%tip)+"."
elif service == "terrible":
   tip = (.10 * total)+total
   print "With a 10% tip you will each pay " + "$" + str("%.2f"%tip)+"."

#9
x = 0
while x < 10:
    x += 1
    print (x)

#10
coins = 0 
more = raw_input("Would you like a coin? ")
while more == "yes":
     coins += 1
     print "You have " + str(coins) + " coins."
     more = raw_input("Would you like another coin? ")
else:
    print "You have " + str(coins) + " coins thank you and goodbye!"
