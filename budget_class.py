#budget class that can instantiate for a given category
#have methods like deposit, withdraw, transfer, get balance etc.


class Budget:
    def __init__ (self, givenCategory, balance):
        self.givenCategory = givenCategory
        self.balance = balance
    def deposit(self):
        amount = int(input('How much would you like to deposit to ' + self.givenCategory + ' ? \n'))
        self.balance += amount
        print("Your " + self.givenCategory, " budget balance is now " + str(self.balance))
    def withdrawal(self):
        memo = input('State the purpose of your withdrawal from ' + self.givenCategory + ' balance \n')
        withdrawalAmount = int(input('How much would you like to withdraw from your ' + self.givenCategory + ' balance today? \n'))
        self.balance -= withdrawalAmount
        print('Your remaining balance is ' + str(self.balance) )
    def transfer(self):
        receivingAccount = input('Which category would you like to transfer to from ' + self.givenCategory + '? \n')
        transferAmount = int(input('How much would you like to transfer from ' + self.givenCategory + ' to ' + receivingAccount+ ' ? \n'))
        self.balance -= transferAmount
        print('You have successfully transferred ' + str(transferAmount) + ' from ' + self.givenCategory + ' to ' + receivingAccount + 'Your balance is now ' + str(self.balance))


#Testing with an instance of the class for food category.
foodBudget = Budget('food', 0)
foodBudget.deposit()
foodBudget.withdrawal()
foodBudget.transfer()






