ryMoney
=======

My simple command-line Money Apps.

Files:
------
ryMoney.py     - The main run environment script.
configLoad.py  - The script that contains the path locations for ryMoney to run
dataClasses.py - The script that contains all the class objects and functions.


Object Types:
-------------

Account - Keeps track of the transactions of a given bank account. 
          Basically put, a list of Transaction Objects. Also maintains the
          ballance of the transactions within the account.

Account List - An object that holds all of the accounts, and contains the
               functions that handle all of the account options.

Budget  - An object that allows for the budgeting of money. Each budget item 
          acts as a simple holding account that money is transfered to from 
          one or more accounts in order to plan and track budgets. 

    name       - name of the budget item.
    fixed      - If the budget is a fixed number each month.
    total      - The total of a fixed budget.
    amount     - A dictonary of amount of money put towards the budget. Each 
                 key is the name of the account that the budgeted money came 
                 from.
    cummAmount - The cumulative amount of money towards the budget from each
                 account.
    memo       - The date the budget item needs to be paid.


Budget List - An object that holds all of the budget items and contains the 
              functions to handle the all of the budget items.
    

Credit  - An object that allows users to keep track of their credit cards. 

    name       - name of the Credit item.
    amount     - A dictonary of amount of money put towards the credit card. 
                 Each key is the name of the account that the budgeted money 
                 came from.
    cummAmount - The cumulative amount of money towards the credit from each
                 account.


Credit List - An object that holds all of the credit items and contains the 
              functions to handle the all of the credit items.

Transaction - An object that holds all the data items of a Transaction. Theses
              data items consist of:
    
    name      - The name/description of the transaction made.
    date      - The date of the transaction.
    num       - The check number or type of transaction (Deposit, withdrawl,
                etc).
    category  - The category the transaction is filed under.
    cleared   - If the Tnsaction has been cleared or not while ballanced.
    amount    - The value of the transaction.
    balance   - The new account balance after the transaction is added.


Category - A category that transactions can  be filed under. Used for looking at
           spending patterns later.


- Setup and Running -

- Config -
Before using ryMoney, the user should first check the configLoad.py script to
make sure that the defined file pathways are correct. In the configLoad.py 
file, the global directory variables DIR, CONFIGDIR, and ACCOUNTDIR are defined.
DIR is the top directory where the scripts are all located, and the directory's
path should be defined in DIR. by default, the CONFIGDIR and ACCOUNTDIR point 
to two subdirectories within DIR that hold the configuration files and account
directories. However, if desired, the CONFIGDIR and ACCOUNTDIR can point to
any location where the configuration files (categories, budget, etc. saves) and
account directories are each located. This is useful if for example, the user 
wants to keep the run scripts in a build folder, but maintain the save files
in another location that can be synced across computers such as a shared 
network folder or dropbox folder.

If the user's saved accounts, budgets, or categories are not loading properly,
it is most likely due to the paths not being defined properly in the
configDIr.py file.

In addition to the directories where the settings are saved, the filenames for
the files that save the categories, budgets, and account transaction regsitry
are defined here under the global name variables catSaveName, budgetSaveName,
and transRegName respectively.


- Use -

In order to run ryMoney, simply execute the python script, ryMoney.py 
(python ryMoney.py).

    
