"""
A budget manager program that can instantiate objects based on different 
budget categories like food, clothing, and entertainment. These objects 
allow for depositing and withdrawing funds from each category, as well 
computing category balances and transferring balance amounts between categories
"""


class Account:
    def __init__(self, user_name, password, bal, pin):
        self.user_name = user_name
        self.password = password
        self.bal = bal
        self.pin = pin

    def __str__(self):
        return f""
    
    def withdraw(self):
        withdraw_amount = input("Enter withdraw amount: ")
        withdraw_amount = check_numb(withdraw_amount, float)
        if self.bal >= withdraw_amount:
            self.bal -= withdraw_amount
            print(f"You withdrew ${numb_format(withdraw_amount)}, current balance sits at: ${numb_format(self.bal)}")
        else:
            return "Insufficient fund, deposit more or withdraw less"
    
    def deposit(self, deposit_amount):
        self.bal += deposit_amount
        print("You deposited ${deposit_amount}, current balance sits at: ${self.bal}")
    
    def numb_format(self, numb):
        """
        Format int into readable string (e.g: $123302 -> $123,302.00)
        """
        return "{:,.2f}".format(numb)
        

def check_numb(user_input, check_type = int):
    # Check if user input is correct type, return desired type if correct, otherwise keep prompting 
    flag = False
    while flag == False:
        try:
            user_input = check_type(user_input)
        except ValueError:
            user_input = input("Please enter a number: ")
        else:
            flag = True

    return check_type(user_input)


def main():
    current_bal = input("Enter current amount in balance: ")
    current_bal = check_numb(current_bal)
    allocation = input("How many categories do you want to split your budget into: ")
    allocation = check_numb(allocation)


if __name__ == "__main__":
    main()
