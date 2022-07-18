class Category:
    # Method to assign the name of each category when an instance is created and attributes
    def __init__(self, nameOfCategory):
        self.categoryName = nameOfCategory
        self.ledger = list()

    # Method to register the deposits
    def deposit(self, amount, description=""):
        # Appends to the ledger() list each deposit as a dictionary
        self.ledger.append({"amount": amount, "description": description})

    # Method to register the withdrawals
    def withdraw(self, amount, description=""):
        # Verify if the withdrawal movement returns a positive balance, if not don't add it to ledger()
        validation = self.check_funds(amount)

        # The nature of the withdrawal movements is to subtract, thus the amount is converted to a negative number
        amount = amount * -1
        
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
        if amount > budget:
            return False
        # If enough funds, withdraw them from the source category and register in the Category.ledger variable
        else:
            # As the amount correspond to a withdrawal, it has to be converted into a negative amount
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
        # Check if the amount in ledger is enough to make a withdrawal
        ledger = self.get_balance()
        
        if withdraw > ledger:
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
    # Dictionary to capture the category name and the percentage of withdrawals of each category
    percentageCategory = dict()
    # Variables to get the withdrawals percentage per category
    percentage = 0
    charCount = 0
    categoryList = list()
    percentageList = list()
    space = ""
    totalWithdrawals = 0

    # Get names and percentages of each category passed in as a parameter
    for cat in categories:
        # Get the withdrawals values
        withdrawals = list()
        # Get the percentages
        for key in cat.ledger:
            # Use the values() method to get only the numeric values.
            for value in key.values():
                if type(value) == int or type(value) == float:
                    if value < 0:
                        value *= -1 # Convert the values into positive to get the correct percentage
                        withdrawals.append(value)
        percentage = sum(withdrawals)
        # Calculate the total value of all withdrawals of all categories
        totalWithdrawals += percentage
        # Add each new key value pair to the percentageCategory dictionary
        percentageCategory[percentage] = cat.categoryName
    
    # Add the key and values to the list that are necessary to print the chart
    for key, value in percentageCategory.items():
        # Get the value of percentage of withdrawals for each category
        key = (key / totalWithdrawals) * 100
        percentageList.append(key)
        categoryList.append(value)

    # Get the category with the name with the most characters and store the categories into a list
    # for later printing configuring
    for category in categories:
        if len(category.categoryName) > charCount:
            charCount = len(category.categoryName)
    
    # Convert the value of the elements in percentageList into the number of 'o' to print in the graphic
    numberOfOs = 0
    whitespace = " "
    for i in percentageList:   
        numberOfOs = round(i/10)
        # Update the item in the corresponding index using index() funcition and passing the number of i
        # The blank spaces are necessary to add to print vertically correctly
        if numberOfOs == 0:
            percentageList[percentageList.index(i)] = "          o"
        elif numberOfOs == 1:
            percentageList[percentageList.index(i)] = "          o"
        else:
            numberOfOs += 1
            whitespace = (11 - numberOfOs) * whitespace
            percentageList[percentageList.index(i)] = whitespace + numberOfOs * "o"
            whitespace = " "

    # Make the categories the same len in characters as the largest one. The difference is filled with blank spaces
    for i in categoryList:
        if len(i) < charCount:
            space = " " * (charCount - len(i))
            # Update the item in the corresponding index using index() funcition and passing the name of the category i
            categoryList[categoryList.index(f"{i}")] = i + space
    
    # Configure the vertical printing of the categoryList list.
    categoriesToPrint = ""
    divisoryLine = "    " + (len(categoryList) * "---") + "-" + "\n"
    graphicsTitle = "Percentage spent by category" + "\n"
    yAxis = list()
    meassurement = ""
    meassurementList = list()
    preGraphics = []
    graphics = ""

    # Vertical graphic
    for i in range(100, -10, -10):
        # Store the vertical numbers
        yAxis.append(f"{i:>3}| ")
        
    # Put the 'o's into a string variable then convert the string into a list
    # with the 'o's and spaces in the proper order for later printing
    stripFinal = ""
    for i in range(11):
        for o in percentageList:
            if i == 10:
                stripFinal = f"{o[i]:<}  "
                meassurement += stripFinal
            else:
                meassurement += f"{o[i]}  "
    meassurement = meassurement
  
    # split the meassurement list every number of categories and append i to meassurementList
    length = len(categoryList)
    while meassurement:
        meassurementList.append(meassurement[:length * length])
        meassurement = meassurement[length * length:]

    # Use zip() to join the yAxis and meassurementList lists into one
    preGraphics = [x for y in zip(yAxis, meassurementList) for x in y]
    
    # Join each two pair of elements in preGraphics and concatenate them in the variable
    # to be passed as the first part of the graphics
    odd = ""
    even = ""

    for i in range(len(preGraphics)):
        if i % 2 != 0:
            preGraphics[i] = f"{preGraphics[i]}"
            even = f"{preGraphics[i]}"
        elif i % 2 == 0:
            odd = preGraphics[i]
            if odd == odd:
                continue
          
        graphics += f"{odd}{even}\n"
      
    # Vertical categories
    for i in range(charCount):
        for horizontal in categoryList: 
            # Print like this if the category is the first one
            if  horizontal == categoryList[0]:
                categoriesToPrint += f"     {horizontal[i]} "
            # Print like this if it is the last one
            elif horizontal == categoryList[-1]:
                categoriesToPrint += f" {horizontal[i]}  "
            # Print like this for the rest
            else:
                categoriesToPrint += f" {horizontal[i]} "
        categoriesToPrint += "\n"

    # Variable to return with the configured chart
    printable = graphicsTitle + graphics + divisoryLine + categoriesToPrint.rstrip("\n")

    return printable
    
    
food = Category("Food")
entertainment = Category("Entertainment")
business = Category("Business")

food.deposit(900, "deposit")

food.deposit(45.56)

food.deposit(900, "deposit")
food.withdraw(45.67, "milk, cereal, eggs, bacon, bread")

food.deposit(900, "deposit")
good_withdraw = food.withdraw(45.67)

food.deposit(900, "deposit")
food.withdraw(45.67, "milk, cereal, eggs, bacon, bread")

food.deposit(900, "deposit")
food.withdraw(45.67, "milk, cereal, eggs, bacon, bread")
transfer_amount = 20
print(food.get_balance())
entertainment_balance_before = entertainment.get_balance()
food.transfer(transfer_amount, entertainment)
print(food.get_balance())
print(entertainment.get_balance())

food.deposit(10, "deposit")

food.deposit(100, "deposit")
food.withdraw(100.10)

food.deposit(100, "deposit")
food.transfer(200, entertainment)

food.deposit(900, "deposit")
food.withdraw(45.67, "milk, cereal, eggs, bacon, bread")
food.transfer(20, entertainment)

food.deposit(900, "deposit")
entertainment.deposit(900, "deposit")
business.deposit(900, "deposit")
food.withdraw(105.55)
entertainment.withdraw(33.40)
business.withdraw(10.99)
print(food)
print(entertainment)
print(business)
print(create_spend_chart([business, food, entertainment]))


################################################################
# food = Category("Food")
# food.deposit(1000, "initial deposit")
# food.withdraw(10.15, "groceries")
# food.withdraw(15.89, "restaurant and more food for dessert")
# print(food.get_balance())
# clothing = Category("Clothing")
# food.transfer(50, clothing)
# clothing.withdraw(25.55)
# clothing.withdraw(100)
# auto = Category("Auto")
# auto.deposit(1000, "initial deposit")
# auto.withdraw(15)

# print(food)
# print(clothing)

# print(create_spend_chart([food, clothing, auto]))
