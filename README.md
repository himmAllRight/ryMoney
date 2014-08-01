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
    dueDate    - The date the budget item needs to be paid.


Budget List - An object that holds all of the budget items and contains the 
              functions to handle the all of the budget items.
    


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


    
