# class Bank:
#     bank_name = "My account "
    
#     def __init__(self, account_number, balance, account_type):
#         self.account_number = account_number
#         self.balance = balance
#         self.account_type = account_type
# def my_work():
#     return f"The {self.account_number} above this is my bank account{self.balance}"
class Account :
    def __init__(self, account_name,account_number,balance):
         self.account_name = account_name
         self.balance=0
    def deiposit(self,amount):
        self.balance+=amount
        return f"You have deposited {amount}your new balance is{self.balance}"  
    def withdraw(self,amount):
        if self.balance <=amount:
            self.balance -=amount
            return f"You have withdraw {amount} your new balance is{self.balance}"
        else:
            f"Your balance is{self.balance} you cannot withdraw {amount}"

