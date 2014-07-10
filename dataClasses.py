import os
import time
import datetime
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
		tempTrans = Transaction(name, date, num, cat, cleared, amount, balance)
		self.transactions.append(tempTrans)

	def saveTransactions(self):
		outTest = open(configLoad.transRegName, 'w+')
		print('Date,num,Description,Category,Cleared,Amount,Balance', 
		       file=outTest)
		for trans in self.transactions:
			trans.printTransaction(outTest)

	def recalculateBallance(self):
		balance = 0
		for trans in self.transactions:
			trans.balance = float(trans.amount) + float(balance)
			balance = trans.balance
		self.balance = balance

	def ballanceAccount(self):
		print("In ballance account...")

	def makeTransList(self, inStartDate, inEndDate):
		startDateString = inStartDate.split("/")
		endDateString   = inEndDate.split("/")

		startDateString = [ int(date) for date in startDateString ]
		endDateString   = [ int(date) for date in endDateString ]

		startDate = datetime.date(startDateString[2],startDateString[0],startDateString[1])
		endDate   = datetime.date(endDateString[2], endDateString[0], endDateString[1])

		print(startDate)
		print(endDate)

		transList = []

		for trans in self.transactions:
			#print(trans.name, trans.year, trans.month, trans.day, sep = "\t")
			if(trans.date >= startDate and trans.date <= endDate):
				transList.append(trans)

		return(transList)


	def printHeader(self):
		print("Date", "Num", "Description", "Category", "Cleared", "Amount", 
		  "Balance", sep="\t\t")


	def printAllTrans(self):
		print("Transactions: \n-------------------")

		ind 	  = 0
		transList = []

		self.printHeader()
		for trans in self.transactions:
			transList.append(trans)
			print(ind, ":  ", sep="", end="")
			trans.printT()
			ind = ind + 1
		print("\n")

		return(transList)

	def printUncleared(self):
		print("Uncleared Transactions: \n------------------------")

		ind 		  = 0
		unclearedList = []
		
		self.printHeader()
		for trans in self.transactions:
			if(trans.cleared == " _ "):
				unclearedList.append(trans)
				print(ind, ":   ",  sep="", end="")
				trans.printT()
				ind = ind + 1
		print("\n")

		return(unclearedList)

	def printTwoMonths(self, printCleared):
		print("Transactions from Last Two Months: \n------------------------")

		ind		  = 0
		monthList = []

		currMonth = int(time.strftime("%m"))
		currYear  = int(time.strftime("%Y"))

		if(printCleared == True):
			transactionList = self.transactions
		else:
			transactionList = []
			for trans in self.transactions:
				if(trans.cleared == " _ "):
					transactionList.append(trans)
					


		self.printHeader()
		for trans in transactionList:
			tranMonth = trans.date.month
			tranYear  = trans.date.year
			valid = False
		#	print(trans.month, trans.year, sep="\t")
			# If Feb-Dec
			if( currMonth > 1):
				if( tranYear == currYear and tranMonth == currMonth ):
					valid = True
				elif( tranYear == currYear and tranMonth == (currMonth - 1)):
					valid = True
			# If Jan
			elif(currMonth == 1):
				if(tranYear == currYear and tranMonth == currMonth):
					valid = True
				elif(tranYear == (currYear - 1) and tranMonth == 12 ):
					valid = True

			# If valid, add to list
			if(valid):
				monthList.append(trans)
				print(ind, ":   ",  sep="", end="")
				trans.printT()
				ind = ind + 1
		print("\n")

		return(monthList)

	def printAccountInfo(self):
		""" Prints out the account information """
		print("Account Name: ", self.name)
		print("Account Balance: $", self.balance, "\n")

		print("Transactions:", "\n---------------",)

		print("Date", "Num", "Description", "Category", "Cleared", "Amount", 
			  "Balance", sep="\t\t")
		
		for transaction in self.transactions:
			transaction.printT()
			#print(transaction.date, "\t\t", transaction.num, "\t\t", 
			#	  transaction.name, "\t\t", transaction.category ,"\t\t",
		#		  transaction.cleared, "\t\t", "$", transaction.amount,"\t\t",
		#		  "$", transaction.balance, 
		#		sep="")
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
	def __init__(self, name, inDate, num, category, cleared, amount, balance ):
		self.inDate     = inDate.split("/")
		#self.inDate   =  int(date) for date in self.inDate 
		self.date     = datetime.date(self.inDate[1],self.inDate[0],self.inDate[1])
		#self.date 	  = self.date.strftime("%m/%d/%y")
		self.name 	  = name
		self.num	  = num
		self.category = category
		self.cleared  = cleared
		self.amount	  = amount
		self.balance  = balance

	def updateDate(self):
		self.date = self.month + "/" + self.day + "/" + self.year

	def printTransaction(self, outputFile):
		print(self.date, self.num, self.name, self.category, self.cleared, 
			  "%.2f" %self.amount, "%.2f" % self.balance, sep=",", file=outputFile)

	def printT(self):
		print(self.date, self.num, self.name, self.category, self.cleared, 
			  "%.2f" % self.amount,  "%.2f" % self.balance, sep="\t\t")
