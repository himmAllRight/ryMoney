import time
import datetime
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
		accountSelected = False

		while(accountSelected == False):
			# Select account to work on:
			configLoad.accountList.printAccountNames()
			print("\nWhich account would you like to work with?")
			accountName = input("(Or hit enter to create new account): ")
			if(accountName == ""):
				# Create new Account
				print("Create New Account:")
				newName = input("What would you like to name the new accout? (or q to cancle): ")

				if(newName == "q"):
					""" returns to account selection """
				
				else:
					configLoad.accountList.createNewAccount(newName)
					self.currAccount = configLoad.accountList.accounts[newName]
					accountSelected = True

			elif(accountName in configLoad.accountList.accounts):
				self.currAccount = configLoad.accountList.accounts[accountName]
				accountSelected = True

			else:
				print("Account '",accountName, "', not found. Please Try Again.")
				screenPauseClear()
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
				year    = input("Enter deposit year (yyyy), or hit ENTER for this Year["+ time.strftime("%Y") +"]: ")
				if(year == ""):
					year =time.strftime("%Y")

				configLoad.cats.printCategories()

				# Checks to make sure value is in bounds
				cat     = eval(input("Select deposit category (#): "))
				while(cat >= len(configLoad.cats.list)):
					print("Index Value is too large. Please choose a number less than ", len(configLoad.cats.list), ".")
					cat     = eval(input("Select deposit category (#): "))

				ammount = eval(input("Enter deposit ammount: "))

				date = datetime.date(int(year), int(month), int(day))

				self.currAccount.newDeposit(name, date, configLoad.cats.list[cat], ammount)

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
				year    = input("Enter payment year (yyyy), or hit ENTER for this Year["+ time.strftime("%Y") +"]: ")
				if(year == ""):
					year =time.strftime("%Y")

				configLoad.cats.printCategories()
				cat     = eval(input("Select payment category (#): "))
				ammount = eval(input("Enter payment ammount: "))

				date = datetime.date(int(year), int(month), int(day))

				self.currAccount.newPayment(name, date, configLoad.cats.list[cat], ammount)

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
				year    = input("Enter check year (yyyy), or hit ENTER for this Year["+ time.strftime("%Y") +"]: ")
				if(year == ""):
					year =time.strftime("%Y")

				configLoad.cats.printCategories()
				cat     = eval(input("Select payment category (#): "))
				ammount = eval(input("Enter check ammount: "))

				date = datetime.date(int(year), int(month), int(day))

				self.currAccount.newCheck(name, date, num, configLoad.cats.list[cat], ammount)

				print("Check Payment added to account: ",self.currAccount.name ,".")
				screenPauseClear()


			# New Budget Transfer
			if(self.command == "nbt"):
				os.system("clear")
				budgetName = ""

				while(budgetName not in configLoad.budgets.budgets):
					configLoad.budgets.printBudgetNames()
					budgetName    = input("Enter Budget name: ")

					if(budgetName not in configLoad.budgets.budgets):
						print(budgetName, " is not a budget. Please try again.")

				day     = input("Enter transfer day (dd), or hit ENTER for Today["+ time.strftime("%d") +"]s: ")
				if(day == ""):
					day = time.strftime("%d")
				month   = input("Enter transfer month (mm), or hit ENTER for this Month["+ time.strftime("%m") +"]: ")
				if(month == ""):
					month = time.strftime("%m")
				year    = input("Enter transfer year (yyyy), or hit ENTER for this Year["+ time.strftime("%Y") +"]: ")
				if(year == ""):
					year =time.strftime("%Y")

				configLoad.cats.printCategories()
				cat     = eval(input("Select payment category (#): "))
				ammount = eval(input("Enter transfer ammount: "))

				date = datetime.date(int(year), int(month), int(day))

				self.currAccount.newBudgetTransfer(budgetName, date, configLoad.cats.list[cat], ammount)

				print("Amount transferred to budget: ",self.currAccount.name ,".")
				screenPauseClear()


			# New Credit Transfer
			if(self.command == "ncp"):
				os.system("clear")
				creditName = ""

				while(creditName not in configLoad.budgets.budgets):
					configLoad.budgets.printBudgetNames()
					creditName    = input("Enter Credit name: ")

					if(creditName not in configLoad.budgets.budgets):
						print(creditName, " is not a budget or Credit name. Please try again.")

				name 	= input("Enter payment name: ")
				day     = input("Enter transfer day (dd), or hit ENTER for Today["+ time.strftime("%d") +"]s: ")
				if(day == ""):
					day = time.strftime("%d")
				month   = input("Enter transfer month (mm), or hit ENTER for this Month["+ time.strftime("%m") +"]: ")
				if(month == ""):
					month = time.strftime("%m")
				year    = input("Enter transfer year (yyyy), or hit ENTER for this Year["+ time.strftime("%Y") +"]: ")
				if(year == ""):
					year =time.strftime("%Y")

				configLoad.cats.printCategories()
				cat     = eval(input("Select payment category (#): "))
				ammount = eval(input("Enter transfer ammount: "))

				date = datetime.date(int(year), int(month), int(day))

				self.currAccount.newCreditTransfer(creditName, name, date, configLoad.cats.list[cat], ammount)

				print("Amount transferred to Dredit: ",self.currAccount.name ,".")
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
				self.currAccount.printTwoMonths(True)

			# Print uncleared transactions from last two months
			if(self.command == "p2mu"):
				os.system("clear")
				self.currAccount.printTwoMonths(False)

			# Clear a transaction
			if(self.command == "ct"):
				os.system("clear")
				unclearedList = self.currAccount.printUncleared()

				# get transaction index value
				ctInd = eval(input("What transaction do you want to clear? (enter #): "))

				unclearedList[ctInd].cleared = " C "

				print("Transaction Cleared")


			# Edit a transaction
			if(self.command == "et"):
				os.system("clear")
				transList = self.currAccount.printAllTrans()

				# get transaction index value
				edit = ""
				editInd = input("What transaction do you want to edit? (enter #, or 'q' to exit): ")
				if(editInd == "q"):
					edit = "q"
				else:
					editInd = int(editInd)
					editTrans = transList[editInd]
				os.system("clear")

				
				while(edit != "q"):
					print("Transaction selected:\n----------------")
					self.currAccount.printHeader()
					print(editInd, ": ", end="")
					editTrans.printT()

					print("\nEdit Options: \n--------------------")
					options = "1: Day  2: Month  3: Year  4: Num  5: Name/Description  6: Category  7.Cleared/Uncleared  8.Amount "
					edit = input(options + "\n\nWhat would you like to change in the transaction? (edit #, or 'q' to quit): ")	

					# Edit Transaction Day
					if(edit == "1"):
						newDay = input("What should the day be changed to? (dd): ")
						editTrans.date = editTrans.date.replace(day= int(newDay))
						print("Day changed.")

					# Edit Transaction Month
					if(edit == "2"):
						newMonth = input("What should the month be changed to? (mm): ")
						editTrans.month = newMonth
						editTrans.date = editTrans.date.replace(month= int(newMonth))
						print("Month Changed.")

					# Edit Transaction Year
					if(edit == "3"):
						newYear = input("What should the year be changed to? (yyyy): ")
						editTrans.year = newYear
						editTrans.date = editTrans.date.replace(year = int(newYear))
						print("Year Changed.")

					# Edit the Check number, if the transacion isn't a Payment or Deposist
					if(edit == "4"):
						if(editTrans.num != "PAY" and editTrans.num != "DEP"):
							newNum = input("What would you like to change the check number to: ")
							editTrans.num = newNum
							print("Check Number Changed.")

						else:
							print("Check number can only be changed for checks!")

					# Edit transaction name/description
					if(edit == "5"):
						newName = input("What would you like to change the Name/Description to: ")
						editTrans.name = newName
						print("Name/Description changed.")

					# Change the category of a transaction
					if(edit == "6"):
						configLoad.cats.printCategories()
						newCatInd = eval(input("Select new category (#): "))
						editTrans.category = configLoad.cats.list[newCatInd]
						print("Category Changed.")

					# Clear or unclear a transaction, depending on current state
					if(edit == "7"):
						if(editTrans.cleared == " C "):
							editTrans.cleared = " - "
							print("Transaction uncleared.")
						elif(editTrans.cleared == " - "):
							editTrans.cleared = " C "
							print("Transaction cleared.")

					# Change the amount of a transaction and recalculate all the 
					if(edit == "8"):
						newAmount = eval(input("Enter new amount: "))
						if(editTrans.num != "DEP"):
							newAmount = newAmount * (-1)
						editTrans.amount = newAmount
						self.currAccount.recalculateBalance()
						print("Transaction amount changed and balance recalculated.")


					screenPauseClear()

				print("Done Editing Transaction")
				

			# Balance Acount
			if(self.command == "ba"):
				
				startDateInput = input("Enter starting date (mm-dd-yyyy): ")
				startAmount    = eval(input("Enter starting amount: "))
				endDateInput	= input("Enter ending date (mm-dd-yyyy): ")
				endAmount	= eval(input("Enter ending amount: "))

				startDateInput = startDateInput.split("-")
				endDateInput   = endDateInput.split("-")

				startDate = datetime.date(int(startDateInput[2]), int(startDateInput[0]) ,int(startDateInput[1]))
				endDate   = datetime.date(int(endDateInput[2]), int(endDateInput[0]), int(endDateInput[1]))


				os.system("clear")

				# Print list of uncleared transactions
				def printUnclearedList():
					i = 0
					print("Uncleared Transactions:")
					for trans in unclearedList:
						print(i, ":  ", end="")
						trans.printT()
						i = i + 1

				# Print the list of transactions when balancing check book
				def printBalanceList():
					j = 0
					print("Transactions for balance: ")
					for trans in balanceTransactions:
						print(j, ":  ", end="")
						trans.printT()
						j = j + 1



				## Select transactions Section
				balanceTransactions = []
				unclearedList = [] 

				preList = self.currAccount.makeTransList(startDate, endDate)
				for trans in preList:
					if( trans.cleared != " C "):
						unclearedList.append(trans)
			
				select = ""
				while(select != "d"):
					printUnclearedList()
					printBalanceList()
					select = input("Select a transaction number to add it to balance ('d' when done): ")
					
					# If Done selecting
					if( select == "d"):
						os.system("clear")
						print("\nThese are the transactions on the statement, correct?")

						printBalanceList()

						check = input("(y/n): ")

						if(check == "y"):
							print("Total for this statement:")
							# Run actual calculation
							self.currAccount.balanceAccount(endDate, balanceTransactions, unclearedList, startAmount, endAmount)


						else:
							select = ""
						

					# Otherwise, continue
					else:
						select = int(select)
						# Cleared selected Transaction
						unclearedList[select].cleared = " T "
						# Move transaction from uncleared to balance List.
						balanceTransactions.append(unclearedList.pop(select))
						os.system("clear")



				screenPauseClear()


			# Select another account
			if(self.command == "sa"):
				os.system("clear")
				accountSelected = False
				while(accountSelected == False):
					configLoad.accountList.printAccountNames()
					accountName = input("Which account would you like to work with?\n(Or hit enter to create a new account): ")
					if(accountName == ""):
						# Create new Account
						print("Create New Account:")
						newName = input("What would you like to name the new accout? (or q to cancle): ")

						if(newName == "q"):
							""" returns to account selection """
					
						else:
							configLoad.accountList.createNewAccount(newName)
							self.currAccount = configLoad.accountList.accounts[newName]
							accountSelected = True
							print("Working account switced to ", newName, ".")
							screenPauseClear()

					elif(accountName in configLoad.accountList.accounts):
						print("Account in list")
						self.currAccount = configLoad.accountList.accounts[accountName]

						accountSelected = True
						print("Working account switced to ", accountName, ".")

					else:
						print("Account '",accountName, "', not found. Please Try Again.")
						screenPauseClear()
					os.system("clear")
				

			# Help Menu
			if(self.command == "h"):
				os.system("clear")
				print("Help Menu to be written...")
				screenPauseClear()

			#os.system("clear")
		configLoad.accountList.saveAccountList()
		print("Accounts Saved...")
		screenPauseClear()


	# Print account Manager options
	def printOptions(self):
		print("-- Account Manager --\n")
		configLoad.accountList.printAccountNames()
		print("\nCurrent Selected Account: ", self.currAccount.name)
		print("Current Account Balance: ", self.currAccount.balance, "\n")
		print("What you would like to do? \n")
		print("sa  - Select another account")
		print("et  - Edit transaction")
		print("ct  - Clear transaction")
		print("ba  - Balance Account")

		print("\nnd - Add new Deposit")
		print("np  - Add a new Payment")
		print("nc  - Add a new Check Payment")
		print("nbt - Add a new Transfer to Budget")

		print("\npa - Print Account Information")
		print("puc - Print all uncleared transactions")
		print("p2m  - Print Transactions form last 2 months")
		print("p2mu  - Print uncleared Transactions form last 2 months")
		print("\nq  - Return to Main Menu")


class BudgetManager:
	""" Used for managing Budgets """

	def __init__(self):
		self.command = ""

		# Category Manager Run Loop
		while(self.command != "q"):
			self.printOptions()
			self.command = input("input: ")

			if(self.command == "nb"):
				name  = input("Enter Budget Name: ")
				fixed = eval(input("Enter Fixed Budget amount (0 if not fixed): "))
				memo  = input("Enter a memo about how often the budget item must be payed: ")

				# add new budget to budgetList
				configLoad.budgets.addBudget(name, fixed, memo)

				screenPauseClear()

			# Need to add functions that transfer money to and from accounts first.
			if(self.command == "db"):
			 	os.system("clear")

			 	configLoad.budgets.printBudgetNames()
			 	deleteName = input("What Item  do you want to delete?")
			 	day   = time.strftime("%d")
			 	month = time.strftime("%m")
			 	year  = time.strftime("%Y")

			 	date  = datetime.date(int(year), int(month), int(day))
			 	configLoad.cats.printCategories()

			 	cat = eval(input("Select what category to put transaction in: "))

			 	configLoad.budgets.removeBudget(deleteName, date, configLoad.cats.list[cat])


			# Print the information for a budget
			if(self.command == "pbi"):
				os.system("clear")
				configLoad.budgets.printBudgetNames()
				name = input("What Budget do you want to print? ")
				os.system("clear")
				configLoad.budgets.budgets[name].printBudgetInfo()

			# Pay Budget
			if(self.command == "pb"):
				os.system("clear")
				configLoad.budgets.printBudgetNames()
				name = input("What Budget do you want to pay off? ")
				os.system("clear")

				if( configLoad.budgets.budgets[name].amount > 0):

					day     = input("Enter budget transfer day (dd), or hit ENTER for Today["+ time.strftime("%d") +"]s: ")
					if(day == ""):
						day = time.strftime("%d")
					month   = input("Enter budget transfer month (mm), or hit ENTER for this Month["+ time.strftime("%m") +"]: ")
					if(month == ""):
						month = time.strftime("%m")
					year    = input("Enter budget transfer year (yyyy), or hit ENTER for this Year["+ time.strftime("%Y") +"]: ")
					if(year == ""):
						year =time.strftime("%Y")

					configLoad.cats.printCategories()
					cat     = eval(input("Select budget category (#): "))

					configLoad.budgets.budgets[name].printBudgetContribution()

					payAll = ""
					while(payAll != "y" and payAll != "n"):
						payAll = input("Do you want to pay the entire budgeted amount from each account listed [y/n]?")

						# If simple pay budget
						if(payAll == "y"):
							amount = configLoad.budgets.budgets[name].amount
							date = datetime.date(int(year), int(month), int(day))
							configLoad.budgets.budgets[name].payBudget(name, date, configLoad.cats.list[cat])
							print("All budgeted money payed off.")
							screenPauseClear()

						# If Advanced pay budget
						elif(payAll == "n"):
							selectContributor = ""
							payments = {}
							possible = {}

							# Makes list of possible transfers accounts to pull money from
							for pos in configLoad.budgets.budgets[name].transfers:
								possible[pos] = configLoad.budgets.budgets[name].transfers[pos]


							while( selectContributor != "d"):
								os.system("clear")
								# Print out each possible transfer account to pay budget
								for pos in possible:
									if(pos in payments):
										print(pos, ":  ", possible[pos], "  [", payments[pos], "] ")
									else:
										print(pos, ":  ", possible[pos])

								print("Selected contributions from each account to budget payment:")
								
								# If payments has items in it, printt them out
								if(len(payments) > 0 ):
									for contributor in payments:
										print(contributor, ":  ", payments[contributor] )

									print("------\nTotal: ", sum(payments.values()))

								selectContributor = input("Select contributor to select money from:")

								if(selectContributor in configLoad.budgets.budgets[name].transfers):
									tempAmount = eval(input("How much money do you want to pay the budget from this account? "))
									if( tempAmount <= possible[selectContributor]):
										payments[selectContributor] = tempAmount

									else: 
										print("The amount specified exceeds the amount transfered to the budget for this account.\nPlease try again and select a value less than", configLoad.budgets.budgets[selectContributor].amount, ".")
								else:
									print("There hasn't been any money contributed to this budget from the account ",selectContributor,".\nPlease select again.")




							# If done selecting contributors for advanced pay budget
							if(selectContributor == "d"):
								amount = configLoad.budgets.budgets[name].amount
								date = datetime.date(int(year), int(month), int(day))

								configLoad.budgets.budgets[name].payBudgetAdv(name, date, configLoad.cats.list[cat], payments)

							os.system("clear")


						else:
							print("Please enter y or n")

				else:
					print("Cannot pay off budget: No money transfered to budget yet.")

				screenPauseClear()


			# Edit a transaction
			if(self.command == "eb"):
				os.system("clear")
				configLoad.budgets.printBudgetNames()

				# get transaction index value
				edit = ""
				editName = input("What budget do you want to edit? ('q' to exit): ")
				if(editName == "q"):
					edit = "q"
				else:
					editBudget = configLoad.budgets.budgets[editName]
				os.system("clear")

				
				while(edit != "q"):
					print("Budget selected:", editBudget.name,"\n----------------")
					editBudget.printBudgetInfo()
					

					print("\nEdit Options: \n--------------------")
					options = "1: change Name  2: Change Memo  3: change fixed value "
					edit = input(options + "\n\nWhat would you like to change in the transaction? (edit #, or 'q' to quit): ")	

					if(edit == "1"):
						inputName = input("What would you like to rename the budget item to: ")
						editBudget.changeBudgetName(inputName)

					if(edit == "2"):
						inputMemo = input("Please enter new memo for budget: ")
						editBudget.changeBudgetMemo(inputMemo)

					if(edit == "3"):
						inputFixed = input("Enter new budget fixed value ('0' for no set value): ")
						editBudget.changeFixed(inputFixed)

					screenPauseClear()

				print("Done Editing Budget")




			# Save Budget
			if(self.command == "sb"):
				configLoad.budgets.saveBudgets(configLoad.budgetSaveName)
				print("Budgets saved.")

				screenPauseClear()

		configLoad.budgets.saveBudgets(configLoad.budgetSaveName)
		print("Budgets saved.")
		screenPauseClear()
				

	# Print budget manager options
	def printOptions(self):
		print("-- Budget Manager --\n")
		print("What you would like to do? \n")
		print("nb  - Add new Budget Item")
		print("db  - Delete Budget Item")
		print("eb  - Edit a Budget Item.\n")
		print("pb  - Pay off Budget")
		print("pbi - Print a Budget's information")
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

			if(self.command == "bm"):
				os.system("clear")
				BudgetManager()

			if(self.command == "q"):
				print("Have a good day! Good-bye.")
				screenPauseClear()
			
			os.system("clear")

		# Ask to save on logout.


	def printOptions(self):
		print("ryMoney -- Main Menu\n")
		print("Please select what you would like to do:")
		print("cm  - Category Manager")
		print("am  - Account Manager)")
		print("bm  - Budget Manager")

		print("\nh - help")
		print("q - Quit ryMoney")



class __main__:
	""" The Main Class """
	print("Main Class")

	# Runs UI
	main = CLI()
