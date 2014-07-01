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
		print("\nWhich account would you like to work with?")
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

			# New Deposit
			if(self.command == "nd"):
				os.system("clear")
				name    = input("Enter deposit name: ")

				day     = input("Enter deposit day (dd), or hit ENTER for Today["+ time.strftime("%d") +"]s: ")
				if(day == ""):
					day = time.strftime("%d")
				month   = input("Enter deposit month (mm), or hit ENTER for this Month["+ time.strftime("%m") +"]: ")
				if(month == ""):
					month = time.strftime("%m")
				year    = input("Enter deposit year (yyyy), or hit ENTER for this Year["+ time.strftime("%") +"]: ")
				if(year == ""):
					year =time.strftime("%Y")

				configLoad.cats.printCategories()
				cat     = eval(input("Select deposit category (#): "))
				ammount = eval(input("Enter deposit ammount: "))

				self.currAccount.newDeposit(name, day, month, year, configLoad.cats.list[cat], ammount)

				print("Deposit added to account: ",self.currAccount.name ,".")
				screenPauseClear()


			# New Payment
			if(self.command == "np"):
				os.system("clear")
				name    = input("Enter Payment name: ")

				day     = input("Enter payment day (dd), or hit ENTER for Today["+ time.strftime("%d") +"]s: ")
				if(day == ""):
					day = time.strftime("%d")
				month   = input("Enter payment month (mm), or hit ENTER for this Month["+ time.strftime("%m") +"]: ")
				if(month == ""):
					month = time.strftime("%m")
				year    = input("Enter payment year (yyyy), or hit ENTER for this Year["+ time.strftime("%") +"]: ")
				if(year == ""):
					year =time.strftime("%Y")

				configLoad.cats.printCategories()
				cat     = eval(input("Select payment category (#): "))
				ammount = eval(input("Enter payment ammount: "))

				self.currAccount.newPayment(name, day, month, year, configLoad.cats.list[cat], ammount)

				print("Payment added to account: ",self.currAccount.name ,".")
				screenPauseClear()


			# New Check Payment
			if(self.command == "nc"):
				os.system("clear")
				name    = input("Enter Payment name: ")
				num		= input("Enter Check Number: ")

				day     = input("Enter check day (dd), or hit ENTER for Today["+ time.strftime("%d") +"]s: ")
				if(day == ""):
					day = time.strftime("%d")
				month   = input("Enter check month (mm), or hit ENTER for this Month["+ time.strftime("%m") +"]: ")
				if(month == ""):
					month = time.strftime("%m")
				year    = input("Enter check year (yyyy), or hit ENTER for this Year["+ time.strftime("%") +"]: ")
				if(year == ""):
					year =time.strftime("%Y")

				configLoad.cats.printCategories()
				cat     = eval(input("Select payment category (#): "))
				ammount = eval(input("Enter check ammount: "))

				self.currAccount.newCheck(name, day, month, year, num, configLoad.cats.list[cat], ammount)

				print("Check Payment added to account: ",self.currAccount.name ,".")
				screenPauseClear()


			# Print Accounts
			if(self.command == "pa"):
				os.system("clear")
				self.currAccount.printAccountInfo()

			# Print only uncleared Transactions
			if(self.command == "puc"):
				os.system("clear")
				self.currAccount.printUncleared()

			# Print transactions from last two months
			if(self.command == "p2m"):
				os.system("clear")
				self.currAccount.printTwoMonths()

			# Clear a transaction
			if(self.command == "ct"):
				os.system("clear")
				unclearedList = self.currAccount.printUncleared()

				# get transaction index value
				ctInd = eval(input("What transaction do you want to clear? (enter #): "))

				unclearedList[ctInd].cleared = " C "

				print("Transaction Cleared")
				


			# Select another account
			if(self.command == "sa"):
				os.system("clear")
				configLoad.accountList.printAccountNames()
				accountName = input("Which account would you like to work with? ")
				if(accountName == ""):
					os.system("clear")
					# Create new Account
					print("Create new account")
					newName = input("What would you like to name the new accout? ")
					configLoad.accountList.createNewAccount(newName)
					self.currAccount = configLoad.accountList.accounts[newName]
					accountName = newName
				else:
					self.currAccount = configLoad.accountList.accounts[accountName]
					
				print("Working account switced to ", accountName, ".")
				
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
		print("-- Account Manager --\n")
		configLoad.accountList.printAccountNames()
		print("Current Selected Account: ", self.currAccount.name, "\n")
		print("What you would like to do? \n")
		print("sa  - Select another account")
		print("pa - Print Account Information")

		print("nd - Add new Deposit")
		print("np - Add a new Payment")
		print("nc - Add a new Check Payment")

		print("puc - Print all uncleared transactions")
		print("ct  - Clear transaction")
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
