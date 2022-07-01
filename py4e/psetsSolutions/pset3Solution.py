class Category:
    # Variable to store movements
    ledger = list()
    # Other variables
    categoryName = ""
    amount = 0
    description = ""

    # Method to assign the name of each category when an instance is created
    def __init__(self, nameOfCategory):
        self.categoryName = nameOfCategory
        print(self.categoryName)

    # Method to register the deposits
    def deposit(self, amount, description=""):
        self.depositAmount = amount
        self.depositDescription = description
        # Appends to the ledger() list each deposit as a dictionary
        Category.ledger.append({"amount": self.depositAmount, "description": self.depositDescription})

    # Method to register the withdraws
    def withdraw(self, amount, description=""):
        # The nature of the withdraw movements is to subtract, thus the amount is converted to a negative number
        self.withdrawAmount = amount * -1
        self.withdrawDescription = description
        # Verify if the withdraw movement returns a positive balance, if not don't add it to ledger()
        validation = Category.verifyPositiveBalance(self, self.withdrawAmount)
        
        if validation == True:
            Category.ledger.append({"amount": self.withdrawAmount, "description": self.withdrawDescription})
            return True
        else:
            return False

    def get_balance(self, amount):
        pass

    def transfer(self):
        pass

    def check_funds(self):
        pass

    def verifyPositiveBalance(self, withdraw):
        dictionaries = Category.ledger
        # List to store only the values of each dictionary
        value = list()
        values = list()
        # Store in value() each dictionary value
        for dictionary in dictionaries:
            for i in dictionary.values():
                value.append(i)
        # Select the numeric values and stores them in values()
        for i in value:
            if type(i) == int:
                values.append(i)
        
        # Append the withdraw movement to values()
        values.append(withdraw)
        
        if sum(values) < 0:
            return False
        else:
            return True

def create_spend_chart(categories):
    pass

food = Category("Food")
food.deposit(1000, "initial deposit")
food.deposit(500, "Second deposit")
print(food.withdraw(1500.15, "groceries"))