import time
import os

import configLoad
import dataClasses

# Clears the screen after a short pause.
def screenPauseClear():
	os.system("sleep 1")
	os.system("clear")


class CategoryManager:
	""" Used for managing Categories. """

	def __init__(self):
		self.command = ""

		# Category Manager Run Loop
		while(self.command != "q"):
			self.printOptions()
			self.command = input("input: ")

			# Categories
			# Add new category
			if(self.command == "ac"):
				os.system("clear")
				configLoad.cats.printCategories()
				newCatName = input("Enter New Category Name: ")
				configLoad.cats.addCategory(newCatName, True)
				screenPauseClear()				
				configLoad.cats.saveCategories(configLoad.catSaveName)

			# Delete Category
			if(self.command == "dc"):
				os.system("clear")
				configLoad.cats.printCategories()
				deleteCatName = input("Enter name of Category to delete: ")
				configLoad.cats.removeCategory(deleteCatName)
				screenPauseClear()
				configLoad.cats.saveCategories(configLoad.catSaveName)

			# Help Menu
			if(self.command == "h"):
				os.system("clear")
				print("Help Menu to be written...")
				screenPauseClear()

			os.system("clear")


	def printOptions(self):
		print("-- Category Manager --\n")
		configLoad.cats.printCategories()
		print("What you would like to do? \n")
		print("ac - Add new Category")
		print("dc - Delete a Category")
		print("\nq  - Return to Main Menu")


class AccountManager:
	""" Used for managing Accounts. """

	def __init__(self):
		self.command = ""

		# Category Manager Run Loop
		while(self.command != "q"):
			self.printOptions()
			self.command = input("input: ")

			# Accounts


			# Print Accounts
			if(self.command == "la"):
				os.system("clear")
				
				for acc in configLoad.accounts:
					print(acc.name)


			# Help Menu
			if(self.command == "h"):
				os.system("clear")
				print("Help Menu to be written...")
				screenPauseClear()

			#os.system("clear")


	def printOptions(self):
		print("-- Account Manager --\n")
		configLoad.cats.printCategories()
		print("What you would like to do? \n")
		print("la - List Accounts")
		print("\nq  - Return to Main Menu")


class CLI:
	""" The command line User Run environment """
	def __init__(self):

		# load accounts function to be written
		
		#######################
		#### Main Run Loop ####
		#######################
		self.command = ""
		# Main Run Loop
		while(self.command != "q"):
			self.printOptions()
			self.command = input("input: ")

			""" Potential Selection Options"""
			# Test Creen Clearing
			if(self.command == "cm"):
				os.system("clear")
				CategoryManager()


			if(self.command == "am"):
				os.system("clear")
				AccountManager()

			if(self.command == "q"):
				print("Have a good day! Good-bye.")
				screenPauseClear()
			
			os.system("clear")

		# Ask to save on logout.


	def printOptions(self):
		print("ryMoney -- Main Menu\n")
		print("Please select what you would like to do:")
		print("cm  - Category Manager")
		print("am  - Account Manager (Not Yet)")
		print("bm  - Budget Manager (Not Yet)")

		print("\nh - help")
		print("q - Quit ryMoney")



class __main__:
	""" The Main Class """
	print("Main Class")

	# Runs UI
	main = CLI()



# sum(DICTNAME.values())
