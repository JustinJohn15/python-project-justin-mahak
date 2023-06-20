DESCRIPTION-
The program represents an ATM (Automated Teller Machine) system. In this program we are performing basic functions of ATM such as accessing account information, changing the PIN, checking the account balance, withdrawing money, and depositing money. All performed in this user defined function program.
To run the program user defined functions are used and looping functions such as if, while and for statements. Switch case is all used for the following options such as withdraw money and depositing it. Basic syntax and logical errors were there which are solved.

 	List of Functionalities-
1.	__init__(self, name):
•	This is the constructor function of the ATM class. It initializes the object and assigns the provided name to the self.name attribute.
2.	acc_info(self):
•	This function displays the account information for the given name. It prints the name, account number, and phone number associated with the name from the info dictionary.
3.	pin_change(self):
•	This function allows the user to change their PIN number. It prompts the user to enter the original PIN, and if it matches the PIN associated with the name in the info dictionary, it prompts for a new PIN and updates it in the dictionary.
•	The user has three attempts to enter the correct original PIN. After three unsuccessful attempts, the account is removed from the info dictionary, and the message "Account Blocked!" is displayed.
4.	acc_balance(self):
•	This function displays the account balance associated with the given name. It retrieves the balance from the info dictionary and prints it.
5.	withdraw(self):
•	This function allows the user to withdraw money from their account. It prompts the user to enter the amount to be withdrawn. If the amount is less than or equal to the account balance, it subtracts the amount from the balance in the info dictionary and displays the updated balance. Otherwise, it prints the message "Insufficient Balance in Account!"
6.	deposit(self):
•	This function allows the user to deposit money into their account. It prompts the user to enter the amount to be deposited and adds that amount to the balance associated with the name in the info dictionary. It then displays the updated balance.

 	HOW TO RUN THE PROGRAM
The program starts by defining a class named atm and declaring several methods within it. These methods are used to define various functionalities of the ATM system, such as accessing account information, changing the PIN, checking the account balance, withdrawing money, and depositing money.
Next, the program defines a dictionary named info that holds the account information of different users. Each user's information is stored as a list of values which are associated with their name.
Then the program enters a while loop, which is the main program loop. This loop allows the user to perform multiple operations such as depositing money, changing pin, etc.
Inside the loop, the program prompts the user to enter their name. If the entered name is found in the info dictionary, the program proceeds to validate the PIN. The user is prompted to enter their PIN, and the program checks if the entered PIN matches the PIN associated with the provided name in the info dictionary. If the PIN is correct, an instance of the atm class is created, and the user is presented with a menu of operations they can perform. The user selects an operation by entering the corresponding number. Based on the selected operation, the program calls the corresponding method of the atm class to perform the desired action.
After each operation, the user is prompted to either exit or continue performing operations. If the user chooses to exit, the program breaks out of the innermost while loop. If the user chooses to continue, the program repeats the process allowing the user to select another operation.
Also, if the user fails to enter the correct PIN within three attempts, their account is removed from the info dictionary, and a message stating "Account Blocked!" is displayed. If the entered name is not found in the info dictionary, the user is prompted to enter the name again.
The program continues to loop until the user decides to exit by entering 'Y' or 'y' when prompted to exit.

