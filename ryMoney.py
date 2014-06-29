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

		# Select account to work on:
		configLoad.accountList.printAccountNames()
		print("Which account would you like to work with?")
		accountName = input("(Or hit enter to create new account): ")
		if(accountName == ""):
			# Create new Account
			print("crete new account")
			newName = input("What would you like to name the new accout? ")
			configLoad.accountList.createNewAccount(newName)
			print(configLoad.accountList.accounts)
			self.currAccount = configLoad.accountList.accounts[newName]

		else:
			self.currAccount = configLoad.accountList.accounts[accountName]
		os.system("clear")
		
		# Category Manager Run Loop
		while(self.command != "q"):
			self.printOptions()
			self.command = input("input: ")


			# Print Accounts
			if(self.command == "pa"):
				os.system("clear")
				self.currAccount.printAccountInfo()


			# Select another account
			if(self.command == "sa"):
				os.system("clear")
				configLoad.accountList.printAccountNames()
				accountName = input("Which account would you like to work with? ")
				self.currAccount = configLoad.accountList.accounts[accountName]
				print("Working account switced to ", currAccount.name, ".")
				screenPauseClear()

			# Help Menu
			if(self.command == "h"):
				os.system("clear")
				print("Help Menu to be written...")
				screenPauseClear()

			#os.system("clear")
		configLoad.accountList.saveAccountList()
		print("Accounts Saved...")
		screenPauseClear()


	def printOptions(self):
		print("-- Account Manager --")
		configLoad.accountList.printAccountNames()
		print("Current Selected Account: ", self.currAccount.name, "\n")
		print("What you would like to do? \n")
		print("pa - Print Account Information")
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
