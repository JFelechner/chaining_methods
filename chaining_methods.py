
#Assignment: User
#If you've been following along, you're going to utilize the User class we've been discussing for this assignment.

#For this assignment, we'll add some functionality to the User class:
    #make_withdrawal(self, amount) - have this method decrease the user's balance by the amount specified
    #display_user_balance(self) - have this method print the user's name and account balance to the terminal
        #eg. "User: Guido van Rossum, Balance: $150
    #BONUS: transfer_money(self, other_user, amount) - have this method decrease the user's balance by the amount and add that amount to other other_user's balance

class User:

    def __init__(self , name):
        self.name = name
        self.account_balance = 0

    def make_deposit(self, amount):
        self.account_balance += amount
        return self

    def make_withdrawl(self, amount):
        self.account_balance -= amount
        return self

    def display_user_balance(self):
        print(f"User: {self.name}, Balance: {self.account_balance}")
        return self

robert = User("Robert")
mike = User("Mike")
tanner = User("Tanner")

robert.make_deposit(2000).make_deposit(1300).make_withdrawl(325).display_user_balance()

mike.make_deposit(2500).make_deposit(3200).make_withdrawl(400).make_withdrawl(175).display_user_balance()

tanner.make_deposit(1750).make_withdrawl(75).make_withdrawl(20).make_withdrawl(30).display_user_balance()



