import time
import os

################################################################################
############################### Global Section #################################
################################################################################

## Global Directories ##
DIR        = "/home/ryan/scripts/ryMoney/"
CONFIGDIR  = DIR + "/configs"
ACCOUNTDIR = DIR + "/accounts"

## Globale File Names
catSaveName = "categories.txt"



## Global Functions ##

# Clears the screen after a short pause.
def screenPauseClear():
	os.system("sleep 1")
	os.system("clear")

# Loads all the Configuratoins
def loadCategories(loadFileName):
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
		c.addCategory(line.strip(), False)

	catInFile.close()
	os.chdir(DIR)

	return(c)

# Loads all the Accounts
def loadAccounts():
	os.chdir(ACCOUNTDIR)

	accountNames =[d for d in os.listdir(os.getcwd()) if os.path.isdir(d)]

	for accountName in accountNames:
		tempAccount = Account(accountName)

		os.chdir(accountName)
		# Load Transactions



		os.chdir(ACCOUNTDIR)


	os.chdir(DIR)

	return(accounts)


## Global Variables
cats = loadCategories(catSaveName)
accounts = loadAccounts()


################################################################################
################################### Classes ####################################
################################################################################

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

		# Resorts List			
		self.list = sorted(self.list)

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


	def printCategories(self):
		print("Categories:")
		id = 0
		for cat in self.list:
			print(cat, "  ", end="")
			id = id + 1
		print("\n")

class Account:
	""" Bank Account Class """
	def __init__(self, accountName):
		self.name 	      = accountName
		self.balance      = 0
		self.transactions = []
		self.categories   = cats

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

		print("Date", "Num", "Description", "Category", "Cleared", "Amount", 
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
		self.date     = time.strftime("%m/%d/%Y")
		self.day	  = time.strftime("%d")
		self.month	  = time.strftime("%m")
		self.year	  = time.strftime("%Y")
		self.num	  = transactionNum
		self.category = transactionCatigory
		self.cleared  = transactionCleared
		self.amount	  = transactionAmount
		self.balance  = newBalance

class CategoryManager:
	""" Used for managing Categories. """

	def __init__(self):
		self.command = ""

		# Category Manager Run Loop
		while(self.command != "q"):
			self.printOptions(cats)
			self.command = input("input: ")

			# Categories
			# Add new category
			if(self.command == "ac"):
				os.system("clear")
				cats.printCategories()
				newCatName = input("Enter New Category Name: ")
				cats.addCategory(newCatName, True)
				screenPauseClear()				
				cats.saveCategories(catSaveName)

			# Delete Category
			if(self.command == "dc"):
				os.system("clear")
				cats.printCategories()
				deleteCatName = input("Enter name of Category to delete: ")
				cats.removeCategory(deleteCatName)
				screenPauseClear()
				cats.saveCategories(catSaveName)

			# Help Menu
			if(self.command == "h"):
				os.system("clear")
				print("Help Menu to be written...")
				screenPauseClear()

			os.system("clear")


	def printOptions(self, cats):
		print("-- Category Manager --\n")
		cats.printCategories()
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
				
				for acc in accounts:
					print(acc.name)
				screenPauseClear()

			# Help Menu
			if(self.command == "h"):
				os.system("clear")
				print("Help Menu to be written...")
				screenPauseClear()

			os.system("clear")


	def printOptions(self):
		print("-- Account Manager --\n")
		cats.printCategories()
		print("What you would like to do? \n")
		print("la - List Accounts")
		print("\nq  - Return to Main Menu")


class CLI:
	""" The command line User Run environment """
	def __init__(self, cats, accounts):

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

	# Checks directories and makes them if not there.
	if not os.path.exists(CONFIGDIR):
		os.makedirs(CONFIGDIR)

	if not os.path.exists(ACCOUNTDIR):
		os.makedirs(ACCOUNTDIR)


	# Runs UI
	main = CLI(cats, accounts)



# sum(DICTNAME.values())
