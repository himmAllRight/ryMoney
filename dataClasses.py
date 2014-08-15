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

	def newDeposit(self, name, date, category, amount):
		""" Adds a new deposit to account. """
		self.balance = self.balance + amount

		# Adds new Deposit to Account
		tempTrans = Transaction(name, date, "DEP", category, " - ", amount, self.balance)
		self.transactions.append(tempTrans)

	def newPayment(self, name, date, category, amount):
		""" Takes a new new Withdrawl from the account """
		self.balance = self.balance - amount
		self.transactions.append(Transaction(name, date, "PAY", category, " - ", amount*(-1), 
								 self.balance))

	def addInterest(self, date, interest):
		""" Takes a new new Withdrawl from the account """
		self.balance = self.balance + interest
		self.transactions.append(Transaction("-- Interest --", date, "INT", "Interest", " C ", interest, 
								 self.balance))

	def newCheck(self, name, date, num, category, amount):
		""" Takes a new new Withdrawl from the account """
		self.balance = self.balance - amount
		self.transactions.append(Transaction(name, date, num, category, " - ", amount*(-1), 
								 self.balance))

	def newBudgetTransfer(self, budgetName, date, category, amount):
		self.balance = self.balance - amount
		configLoad.budgets.budgets[budgetName].newTransfer(self.name, amount)
		budgetTitle = "-- Budget Transfer (" + budgetName + ") --"
		self.transactions.append(Transaction(budgetTitle, date, "BT ", category, "BT ", amount, self.balance))

	def newCreditTransfer(self, creditName, name, date, category, amount):
		self.balance = self.balance - amount
		configLoad.budgets.budgets[creditName].newTransfer(self.name, amount)
		budgetTitle = name + " [Credit: " + creditName + "] - " + name
		self.transactions.append(Transaction(budgetTitle, date, "CT ", category, "CT ", amount, self.balance))

	def newBudgetPayment(self, budgetName, date, category, amount):
		budgetTitle = " -- Budget Payed (" + budgetName + "[" + str(amount) + "]) --"
		self.transactions.append(Transaction(budgetTitle, date,  "BP ", category, "BP ", amount, self.balance ))


	def importTransaction(self, date, num, name, cat, cleared, amount, balance):
		tempTrans = Transaction(name, date, num, cat, cleared, amount, balance)
		self.transactions.append(tempTrans)

	def saveTransactions(self):
		outTest = open(configLoad.transRegName, 'w+')
		print('Date,num,Description,Category,Cleared,Amount,Balance', 
		       file=outTest)
		for trans in self.transactions:
			trans.printTransaction(outTest)

	def recalculateBalance(self):
		balance = 0
		for trans in self.transactions:
			trans.balance = float(trans.amount) + float(balance)
			balance = trans.balance
		self.balance = balance

	def balanceAccount(self, endDate, balanceList, unclearedList, startAmount, endAmount):
		print("In balance account...")

		balanceListAmount = 0
		unlistedAmount    = 0

		# Find Sum of balanceList transactions
		for trans in balanceList:
			balanceListAmount = balanceListAmount + trans.amount

		# Get the sum of the uncleared deposits and Pays NOT on the statement.
		for trans in unclearedList:
			unlistedAmount = unlistedAmount + trans.amount

		amountCheck = startAmount + balanceListAmount + unlistedAmount


		print("Check: ", amountCheck == self.balance )

		interest = float( endAmount - (startAmount + balanceListAmount) )
		print("%.2f" % interest)

		interestCheck = ""
		while(interestCheck != "y" and interestCheck != "n"):
			interestCheck = input("Is the interest correct(y/n): ")
			# If correct, marked as cleared and exit
			if(interestCheck == "y"):
				self.addInterest(endDate, interest)
				for trans in balanceList:
					trans.cleared = " C "

			# If it isn't correct, changed cleared status of transactions
			elif(interestCheck == "n"):
				for trans in balanceList:
					trans.cleared = " - "

			else:
				print("Please enter 'y' or 'n'.")



	def makeTransList(self, startDate, endDate):
		print("Making TransList...")
		print(isinstance(startDate, datetime.date))
		print(isinstance(endDate, datetime.date))

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
			if(trans.cleared != " C "):
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
				if(trans.cleared == " - "):
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
		print("Account Balance: $", "%.2f" % self.balance, "\n")

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
						dateString = row[0].split("-")
						date = datetime.date(int(dateString[0]), int(dateString[1]), int(dateString[2]))

						tempAccount.importTransaction(date, row[1], row[2], row[3], row[4], float(row[5]), float(row[6]))

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
		self.date     = inDate
		self.name 	  = name
		self.num	  = num
		self.category = category
		self.cleared  = cleared
		self.amount	  = amount
		self.balance  = balance

	def printTransaction(self, outputFile):
		print(self.date, self.num, self.name, self.category, self.cleared, 
			  "%.2f" %self.amount, "%.2f" % self.balance, sep=",", file=outputFile)

	def printT(self):
		print(self.date, self.num, self.name, self.category, self.cleared, 
			  "%.2f" % self.amount,  "%.2f" % self.balance, sep="\t\t")



class Budget:
	""" A budget Item """
	def __init__(self, name, fixed, memo):
		self.name     	  = name
		self.fixed    	  = fixed
		self.amount   	  = 0
		self.transfers    = {}
		self.memo  		  = memo.strip("\n")

	def setAmount(self):
		self.amount = sum(self.transfers.values())

	def newTransfer(self, accountName, amount):
		# If the account has already transfered money
		if( accountName in self.transfers):
			self.transfers[accountName] = self.transfers.get(accountName) + amount

		# If a new account is contributing money to the budget.
		else:
			self.transfers[accountName] = amount

		# Set new Budge amount
		self.setAmount()

	def payBudget(self, budgetName, date, category):
		# Write account transaction that it is paid.
		for payAccount in self.transfers:
			configLoad.accountList.accounts[payAccount].newBudgetPayment(budgetName, date, category, self.transfers[payAccount] )


		print("Budget paid and noted in account transactions.")

		# Essentially clears the budget...
		self.amount     = 0
		self.transfers  = {} 
	def payBudgetAdv(self, budgetName, date, category, payments):
		for payAccount in payments:
			configLoad.accountList.accounts[payAccount].newBudgetPayment(budgetName, date, category, payments[payAccount] )

			newAmount = self.amount - payments[payAccount]
			if(newAmount == 0):
				del self.transfers[payAccount]



	def changeBudgetName(self, newName):
		oldname = self.name
		configLoad.budgets.budgets[newName] = configLoad.budgets.budgets.pop(oldname)
		self.name = newName
		print("Budget name changed from ", oldname, " to ", self.name, ".")

	def changeBudgetMemo(self, newMemo):
		self.memo = newMemo
		print("Budget memo changed to ", newMemo)

	def changeFixed(self, newFixedValue):
		self.fixed = newFixedValue
		print("Budget memo chaned to ", newFixedValue)


	def printBudgetInfo(self):
		# Print out information of accounts contributing to Budget
		print("Budget Contribution for", self.name , ":\nMemo: ", self.memo, "\n-----------------------")


		if(len(self.transfers) == 0):
			print("No money transfered to budget yet.")
		else:
			for account in self.transfers:
				print(account, ":  $", self.transfers[account], sep="")

		if(self.fixed > 0):
			print("----------------------------\nTotal:  $", self.amount, "/", self.fixed,"\n")
		else:
			print("----------------------------\nTotal:  $", self.amount, "\n")

	def printBudgetContribution(self):
		print("Budget Contribution for", self.name)

		if(len(self.transfers) == 0):
			print("No money transfered to budget yet.")
		else:
			for account in self.transfers:
				print(account, ":  $", self.transfers[account], sep="")




class BudgetList:
	def __init__(self):
		self.budgets = {}

	def addBudget(self, name, fixed, memo):
		# Check to see if budget exists, and if not, add a new one.
		if( name in self.budgets):
			print("The budget '", name, "' is already created.")
		else:
			self.budgets[name] = Budget(name, int(fixed), memo)

	
# Need to make it so that it can re-add the money back to the accounts before deleteing first.
	def removeBudget(self, budgetName, date, category):
		for payAccount in self.budgets[budgetName].transfers:
			configLoad.accountList.accounts[payAccount].newBudgetPayment(budgetName, date, category, self.transfers[payAccount] )

		del self.budgets[budgetName]
		print("Budget item '", budgetName, "' deleted.")

	def saveBudgets(self, saveFileName):
		os.chdir(configLoad.CONFIGDIR) # Enter Saves Directory
		budgetOutFile = open(saveFileName, "w+")

		for budgetName in self.budgets:
			# Create a temp budget item to easily reference variables.
			tempBudget = self.budgets[budgetName]
			# Print Budget Info
			print(budgetName, tempBudget.fixed, tempBudget.memo, sep="|", file= budgetOutFile)
			
			# make string containing Budget's saved payments
			if(len(tempBudget.transfers) == 0):
				transfersSaveString = "No money transfered."
			else:
				transfersSaveString = ""
				for transfer in tempBudget.transfers:
					transfersSaveString = transfersSaveString + transfer + ":" + str(tempBudget.transfers[transfer]) + "|"
					
				transfersSaveString = transfersSaveString[:-1]	# Remove last "|"
			
			# Write string to file
			print(transfersSaveString, file= budgetOutFile)
		
		budgetOutFile.close()
		os.chdir(configLoad.DIR)	# Return to program DIR

	def loadBudgets(self):

		os.chdir(configLoad.CONFIGDIR)
		# Load Transactions
		budgets =  open(configLoad.budgetSaveName, 'r')
		reader = csv.reader(budgets)
		i = 0
		currName = ""
		for row in budgets:
			# First of two lines per budget pair
			if(i % 2 == 0):
				firstLine = row.split("|")
				currName = firstLine[0]
				self.addBudget(firstLine[0], firstLine[1], firstLine[2])

			else:
				if(row.strip("\n") == "No money transfered."):
					pass
					# Don't need to do anything if there are no transfers for budget.
				
				else:
					payments = row.split("|")

					for payment in payments:
						paymentInfo = payment.split(":")
						self.budgets[currName].transfers[paymentInfo[0]] = int(paymentInfo[1])
				self.budgets[currName].setAmount()

			i = i + 1


		os.chdir(configLoad.DIR)



	def printBudgetNames(self):
		i = 0
		names =""
		for budgetName in self.budgets:
			names = names + budgetName + "   "
			i = i + 1
		print(names)

