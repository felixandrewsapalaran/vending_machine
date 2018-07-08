soda  = ["Pepsi","Cherry Coke Zero", "Sprite"]
chips = ["Doritos", "Fritos"] 
candy = ["Snickers", "M&Ms", "Twizzlers"]

while True:
  #We will lower whatever they put in.
  choice = input("Would you like a SODA, some CHIPS, or a CANDY? ").lower()
  #Here is the solution for that traceback error. We can fix with try and accept error. 
  try: 
    if choice  == 'soda':
    #They get whatever the last thing is there on the list.
      snack =  soda.pop()
    elif choice == 'chips':
      snack = chips.pop()
    elif choice == 'candy':
      snack = candy.pop()
    #If they didn't give any of the above then we do this task below.
    else:
      print("Sorry, I didn't understand that")
      #And we'll continue, so it will just print out the stuff again.
      continue
  except IndexError: 
    #Let's format that with the choice that they put in.
    print("We're all out of {}! Sorry!".format(choice))
  #Otherwise when that's all done. The we format that with the choice that they put in and the snack that they were given.
  #Otherwise if still everythign still good then we can print that below.
  else:  
    print("Here's your {}: {}".format(choice,snack))
  
  
  #Please note: that we only have 1 stock of each choices in the list. It could run out if you keep asking for snacks. For instance chips we only have 2 chips in our machine after askig three times it will give you an trace error. That means the list is now empty. We need to fix this with a try and except.