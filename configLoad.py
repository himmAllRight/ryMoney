import os
import datetime
import csv
import dataClasses



# Loads all the Configuratoins
def loadCategories(loadFileName):
	c = dataClasses.Categories()

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





## Global Directories ##
DIR        = "/home/ryan/scripts/ryMoney"
CONFIGDIR  = DIR + "/configurations"
ACCOUNTDIR = DIR + "/accounts"

## Globale File Names
catSaveName  = "categories.txt"
transRegName = 'transactionReg.csv'	


# Checks directories and makes them if not there.
if not os.path.exists(CONFIGDIR):
	os.makedirs(CONFIGDIR)

if not os.path.exists(ACCOUNTDIR):
	os.makedirs(ACCOUNTDIR)



accountList = dataClasses.AccountList()
cats 		= loadCategories(catSaveName)

# Load accounts
accountList.loadAccounts()




