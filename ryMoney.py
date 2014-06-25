import time
import os

# Directories
DIR        = "/home/ryan/scripts/ryMoney/"
CONFIGDIR  = DIR + "/configs"
ACCOUNTDIR = DIR + "/accounts"

class Categories:
	""" A payment category """
	def __init__(self):
		self.list = []

	def addCategory(self, categoryName, message):
		## Adds new Category if it  does not exist
		if(self.list.count(categoryName) == 0):
			self.list.append(categoryName)
			if(message):
				print(categoryName, " added to categories.")
		else:
			print("Category ", categoryName, " already exists!", sep="")

	def containsCategory(self, searchName):
		""" Returns the index of a searched category, otherwise returns -1 """
		if(self.list.count(searchName) > 0):
			return(self.list.index(searchName))
		else:
			return(-1)

	def removeCategory(self, deleteName):
		if(self.list.count(deleteName) > 0):
			self.list.remove(deleteName)
			print(deleteName, " has been delted.")
		else:
			print("No category with the name ", deleteName, ".")

	def saveCategories(self, saveFileName):
		os.chdir(CONFIGDIR) # Enter Saves Directory
		catOutFile = open(saveFileName, "w+")
		
		for category in self.list:
			print(category, file= catOutFile, sep="\n")
		
		catOutFile.close()
		os.chdir(DIR)	# Return to program DIR

	def loadCategories(self,loadFileName):
		os.chdir(CONFIGDIR)

		# Load File
		try:
			catInFile = open(loadFileName, "r")
		except:
			# Make File if Doesn't exit
			open(loadFileName, "w+")

			# The Load it again.
			catInFile = open(loadFileName, "r")

		# Adds categories from save file, if they do not currently exist.
		for line in catInFile:
			self.addCategory(line.strip(), False)

		catInFile.close()
		os.chdir(DIR)


	def printCategories(self):
		print("Categories:")
		id = 0
		for cat in self.list:
			print(id, ":", cat, "  ", end="")
			id = id + 1
		print("\n")

class Account:
	""" Bank Account Class """
	def __init__(self, accountName, catList):
		self.name 	      = accountName
		self.balance      = 0
		self.transactions = []
		self.categories   = catList

	def newDeposit(self, name, catInd, amount):
		""" Adds a new deposit to account. """
		self.balance = self.balance + amount

		# Adds new Deposit to Account
		self.transactions.append(Transaction(name, " DEP ", self.categories.list[catInd] ," _ ", amount, 
								 self.balance))

	def newWithdrawl(self, name, catInd, num, amount):
		""" Takes a new new Withdrawl from the account """
		self.balance = self.balance - amount
		self.transactions.append(Transaction(name, num, self.categories.list[catInd], " _ ", amount*(-1), 
								 self.balance))

	def printAccountInfo(self):
		""" Prints out the account information """
		print("Account Name: ", self.name)
		print("Account Balance: $", self.balance, "\n")

		print("Transactions:", "\n---------------",)

		print("Date", "Num", "Payee", "Category", "Cleared", "Amount", 
			  "Balance", sep="\t\t")
		
		for transaction in self.transactions:
			print(transaction.date, "\t\t", transaction.num, "\t\t", 
				  transaction.name, "\t\t", transaction.category ,"\t\t",
				  transaction.cleared, "\t\t", "$", transaction.amount,"\t\t",
				  "$", transaction.balance, 
				sep="")


class Transaction:
	""" Transaction for accounts """
	def __init__(self, transactionName, transactionNum, transactionCatigory,
				 transactionCleared, transactionAmount, newBalance):

		self.name 	  = transactionName
		self.date     = time.strftime("%d/%m/%Y")
		self.num	  = transactionNum
		self.category = transactionCatigory
		self.cleared  = transactionCleared
		self.amount	  = transactionAmount
		self.balance  = newBalance


class CLI:
	""" The command line User Run environment """

	def __init__(self):
		print(CONFIGDIR)
		print("Hello! Welcome to ryMoney. \n")
		catSaveName = "categories.txt"


		#######################
		# Auto-load functions #
		#######################
		cats = Categories()
		cats.loadCategories(catSaveName)

		accounts = []
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
			if(self.command == "c"):
				os.system("clear")

			# Accounts

			#Create New Account
			if(self.command == "ca"):
				os.system("clear")
				newName = input("Enter new account name: ")
				accounts.append(Account(newName, cats))
				print("Account " + newName + " created.")
				self.screenPauseClear()

			#Create New Account
			if(self.command == "la"):
				os.system("clear")
				
				for acc in accounts:
					print(acc.name)
				self.screenPauseClear()



			# Categories
			# Print Loaded Categories
			if(self.command == "sc"):
				os.system("clear")
				cats.printCategories()

			# Add new category
			if(self.command == "ac"):
				os.system("clear")
				cats.printCategories()
				newCatName = input("Enter New Category Name: ")
				cats.addCategory(newCatName, True)
				self.screenPauseClear()				
				cats.saveCategories(catSaveName)

			# Delete Category
			if(self.command == "dc"):
				os.system("clear")
				cats.printCategories()
				deleteCatName = input("Enter name of Category to delete: ")
				cats.removeCategory(deleteCatName)
				self.screenPauseClear()
				cats.saveCategories(catSaveName)

			# Help Menu
			if(self.command == "h"):
				os.system("clear")
				print("Help Menu to be written...")
				self.screenPauseClear()



		# Ask to save on logout.
		askSave = input("Would you like to save before quitting? (y/n): ")
		if(askSave == "y"):
			print("Saving file...")
			# Save command
			print("File Saved!")

		print("Have a good day! Good-bye.")
		self.screenPauseClear()

	def printOptions(self):
		print("Please select what you would like to do:")
		print("c  - Create New Account")
		print("l  - Load Saved Account")

		print("\nCategories:")
		print("sc - Show saved Categories")
		print("ac - Add new Category")
		print("dc - Delete a Category")

		print("\nh - help")

	def screenPauseClear(self):
		os.system("sleep 1")
		os.system("clear")

class __main__:
	""" The Main Class """
	print("Main Class")

	# Checks directories and makes them if not there.
	if not os.path.exists(CONFIGDIR):
		os.makedirs(CONFIGDIR)


	# Runs UI
	main = CLI()
