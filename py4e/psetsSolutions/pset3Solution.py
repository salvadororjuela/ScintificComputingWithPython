class Category:
    categoryName = ""
    amount = 0
    description = ""
    ledger = list()

    # Method to assign the name of each category when an instance is created
    def __init__(self, nameOfCategory):
        self.categoryName = nameOfCategory

    # Method to register the deposits
    def deposit(self, amount, description=""):
        # Variable to store movements
        self.ledger = list()
        # Appends to the ledger() list each deposit as a dictionary
        self.ledger.append({"amount": amount, "description": description})

    # Method to register the withdraws
    def withdraw(self, amount, description=""):
        # The nature of the withdraw movements is to subtract, thus the amount is converted to a negative number
        amount = amount * -1
        # Verify if the withdraw movement returns a positive balance, if not don't add it to ledger()
        validation = self.check_funds(amount)
        
        if validation == True:
            self.ledger.append({"amount": amount, "description": description})
            return True
        else:
            return False

    def get_balance(self):
        dictionaries = self.ledger
        # List to store only the values of each dictionary
        value = list()
        values = list()
        # Store in value() each dictionary value
        for dictionary in dictionaries:
            for i in dictionary.values():
                value.append(i)

        # Select the numeric values and stores them in values()
        for i in value:
            if type(i) == int or type(i) == float:
                values.append(i)

        return sum(values)

    def transfer(self, amount, budgetCategory):
        # Read the budget
        budget = self.get_balance()
        # Variable that gets the name of the budget category to where the funds are transfer to
        transferCategoryName = budgetCategory.categoryName
        
        # Determine if there are enough funds in the budget category 
        if budget - amount < 0:
            return False
        # If enough funds, withdraw them from the source category and register in the Category.ledger variable
        else:
            # As the amount is a withdraw, it has to be converted into a negative amount
            amount = amount * -1
            # Add to the ledger of the origin of the funds the amount and the description
            self.ledger.append({"amount": amount, "description": f"Transfer to {transferCategoryName}"})

            # To transfer to the destination budget category, turn the value again in a positive value
            # because funds are added to this budget category.
            amount = amount * -1
            # Add to the ledger of the budget 
            # catagory where the funds are destinated the value and description of the tranfer
            budgetCategory.deposit(amount, f"Transfer from {self.categoryName}")
          
            return True

        # Add to the destination ledger the amount and the description 
        # If not enough funds only return False and don't add funds to any of the 

    def check_funds(self, withdraw):
        dictionaries = self.ledger
        # List to store only the values of each dictionary
        value = list()
        values = list()
        # Store in value() each dictionary value
        for dictionary in dictionaries:
            for i in dictionary.values():
                value.append(i)
        # Select the numeric values and stores them in values()
        for i in value:
            if type(i) == int or type(i) == float:
                values.append(i)
        
        # Append the withdraw movement to values()
        values.append(withdraw)
        
        if sum(values) < 0:
            return False
        else:
            return True

    # Method to print the budget object
    def __str__(self):
        # Print the name in the center of 30 characters
        name = f"{self.categoryName:*^30}\n"
        dictionaries = self.ledger
        element = ""
        # loop trhough each dictionary in the ledger of the budget category
        for dictionary in dictionaries:
            # Concatenate each dictionary in the format required
            element += f"{dictionary['description'][0:23]:23}" + f"{dictionary['amount']:>7.2f}\n" 
        
        return name + element + "Total: " + str(self.get_balance())
        

def create_spend_chart(categories):
    pass

food = Category("Food")
food.deposit(1000, "initial deposit")
food.withdraw(10.15, "groceries")
food.withdraw(15.89, "restaurant and more food for dessert")
print(food.get_balance())
clothing = Category("Clothing")
food.transfer(50, clothing)
print(food.get_balance())
print(food.ledger)
print(clothing.ledger)
clothing.withdraw(25.55)
print(clothing.get_balance())
clothing.withdraw(100)
print(clothing.get_balance())
auto = Category("Auto")
auto.deposit(1000, "initial deposit")
auto.withdraw(15)
print(auto.ledger)
print(auto.get_balance())

print(food)
print(clothing)