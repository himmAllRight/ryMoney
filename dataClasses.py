import os
import time
import csv

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
			print(id, ": ", cat, "  ", end="")
			id = id + 1
		print("\n")

class Account:
	""" Bank Account Class """
	def __init__(self, accountName):
		self.name 	      = accountName
		self.balance      = 0
		self.transactions = []

	def newDeposit(self, name, day, month, year, category, amount):
		""" Adds a new deposit to account. """
		self.balance = self.balance + amount

		# Adds new Deposit to Account
		tempTrans = Transaction(name, day, month, year, "DEP", category, " _ ", amount, self.balance)
		self.transactions.append(tempTrans)

	def newPayment(self, name, day, month, year, category, amount):
		""" Takes a new new Withdrawl from the account """
		self.balance = self.balance - amount
		self.transactions.append(Transaction(name, day, month, year, "PAY", category, " _ ", amount*(-1), 
								 self.balance))

	def newCheck(self, name, day, month, year, num, category, amount):
		""" Takes a new new Withdrawl from the account """
		self.balance = self.balance - amount
		self.transactions.append(Transaction(name, day, month, year, num, category, " _ ", amount*(-1), 
								 self.balance))

	def importTransaction(self, date, num, name, cat, cleared, amount, balance):
		dates     = date.split("/")
		tempTrans = Transaction(name, dates[1], dates[0], dates[2], "DEP", cat, " _ ", amount, balance)
		self.transactions.append(tempTrans)

	def saveTransactions(self):
		outTest = open(configLoad.transRegName, 'w+')
		print('Date,num,Description,Category,Cleared,Amount,Balance', 
		       file=outTest)
		for trans in self.transactions:
			trans.printTransaction(outTest)

	def printUncleared(self):
		ind = 0
		print("Uncleared Transactions: \n------------------------")

		for trans in self.transactions:
			if(trans.cleared == " _ "):
				print(ind, ":   ",  sep="", end="")
				trans.printT()
				ind = ind + 1
		print("\n")

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
		print("\n")

class AccountList:
	""" An object that holds all the account objects and contains the functions
		to edit all of the accounts (load, print, etcs) """
	def __init__(self):
		self.accounts = {}

	def createNewAccount(self, newName):
		newAccount = Account(newName)
		self.accounts[newName] = newAccount
		print("Account ", newName, " created.")

	def loadAccounts(self):
		os.chdir(configLoad.ACCOUNTDIR)

		accountNames =[d for d in os.listdir(os.getcwd()) if os.path.isdir(d)]

		for accountName in accountNames:
			tempAccount = Account(accountName)

			os.chdir(accountName)
			# Load Transactions
			with open(configLoad.transRegName, 'r', newline='') as trans:
				reader = csv.reader(trans)
				i = 0
				for row in reader:
					if(i < 1):
						header = row
					else:

						tempAccount.importTransaction(row[0], row[1], row[2], row[3], row[4], float(row[5]), float(row[6]))

					i = i + 1
				
				if( (len(tempAccount.transactions)) > 0):
					loadBalance = tempAccount.transactions[  len(tempAccount.transactions) - 1  ].balance
					tempAccount.balance = loadBalance

			self.accounts[tempAccount.name] = tempAccount
			os.chdir(configLoad.ACCOUNTDIR)


		os.chdir(configLoad.DIR)

	def containsAccount(self, searchName):
		for tempAccountName in self.accounts:
			if(tempAccountName == searchName):
				return(True)
		print("There is no account named ", searchName, "!")
		return(False)


	# Saves accounts info to files
	def saveAccountList(self):
		os.chdir(configLoad.ACCOUNTDIR)
		for account in self.accounts:
			if not os.path.exists(account):
				os.makedirs(account)
			
			os.chdir(account)
			self.accounts[account].saveTransactions()
			os.chdir("..")

		os.chdir(configLoad.DIR)

	# Prints out each account name
	def printAccountNames(self):
		print("Accounts:")
		for name in self.accounts:
			print(name, "  ", end="")
		print("")




class Transaction:
	""" Transaction for accounts """
	def __init__(self, name, day, month, year, num, category, cleared, amount, balance ):

		self.name 	  = name
		self.day	  = day
		self.month	  = month
		self.year	  = year
		self.date     = month + "/" + day + "/" + year
		self.num	  = num
		self.category = category
		self.cleared  = cleared
		self.amount	  = amount
		self.balance  = balance

	def printTransaction(self, outputFile):
		print(self.date, self.num, self.name, self.category, self.cleared, 
			  self.amount, self.balance, sep=",", file=outputFile)

	def printT(self):
		print(self.date, self.num, self.name, self.category, self.cleared, 
			  self.amount, self.balance, sep="\t\t")
