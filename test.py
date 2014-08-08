# testing for if statements

x = ""

while(x != "y" and x != "n"):
	x = input("Enter an option (y/n): ")
	if(x == "y"):
		print("yes")
	elif(x == "n"):
		print("no")
	else:
		print ("Please enter 'y' or 'n'.")