ryMoney
=======

My simple Money App


Object Types:
-------------

Account - Keeps track of the transactions of a given checking account. 
          Essentially a list of Transaction Objects. Also maintains the 
          ballance of the transactions within the account.

Budget Account - Another type of account that allows for the budgeting of money.
                 A simple holding account that money is transfered to to budget
                 ahead. STILL IN DESIGN/DEVELOPMENT.

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


    
