import os
import time

import configLoad

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
		os.chdir(configLoad.CONFIGDIR) # Enter Saves Directory
		catOutFile = open(saveFileName, "w+")
		
		for category in self.list:
			print(category, file= catOutFile, sep="\n")
		
		catOutFile.close()
		os.chdir(configLoad.DIR)	# Return to program DIR


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

	def newDeposit(self, name, catInd, amount):
		""" Adds a new deposit to account. """
		self.balance = self.balance + amount

		# Adds new Deposit to Account
		self.transactions.append(Transaction(name, " DEP ", configLoad.cats.list[catInd] ," _ ", amount, 
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
