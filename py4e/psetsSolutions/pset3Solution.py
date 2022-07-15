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

    # Method to register the withdrawals
    def withdraw(self, amount, description=""):
        # The nature of the withdrawal movements is to subtract, thus the amount is converted to a negative number
        amount = amount * -1
        # Verify if the withdrawal movement returns a positive balance, if not don't add it to ledger()
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
        
        # Append the withdrawal movement to values()
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
    # Dictionary to capture the category name and the percentage of withdrawals of each category
    percentageCategory = dict()
    # Variables to get the withdrawals percentage per category
    percentage = 0
    # List to sort the percentage and name of the category in reverse order
    percentagesReverse = list()

    # Get names and percentages of each category passed in as a parameter
    for cat in categories:
        # Get the names
        positive = list()
        negative = list()
        # Get the percentages
        for key in cat.ledger:
            # Use the values() method to get only the numeric values.
            for value in key.values():
                if type(value) == int or type(value) == float:
                    if value >= 0:
                        positive.append(value)
                    else:
                        value *= -1 # Convert the values into positive to get the correct percentage
                        negative.append(value)
        percentage = round((sum(negative) / sum(positive)) * 100)
        # Add each new key value pair to the percentageCategory dictionary
        percentageCategory[percentage] = cat.categoryName
    
    # Sort the list of tuples in reverse order
    for key, value in percentageCategory.items():
        percentagesReverse.append((key, value))
    percentagesReverse.sort(reverse=True)

    # Get the category with the name with the most characters and store the categories into a list
    # for later printing configuring
    charCount = 0
    categoryList = list()
    percentageList = list()
    space = ""
    for category in categories:
        if len(category.categoryName) > charCount:
            charCount = len(category.categoryName)

    for i in percentagesReverse:
        percentageList.append(i[0])
        categoryList.append(i[1])
    
    # Convert the value of the elements in percentageList into the number of 'o' to print in the graphic
    numberOfOs = 0
    whitespace = " "
    for i in percentageList:   
        numberOfOs = round(i/10)
        # Update the item in the corresponding index using index() funcition and passing the number of i
        # The blank spaces are necessary to add to print vertically correctly
        if numberOfOs == 0 or numberOfOs == 1:
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
        yAxis.append(f"{i:>3}|")
        
    # Put the 'o's into a string variable then convert the string into a list
    # with the 'o's and spaces in the proper order for later printing
    for i in range(11):
        for o in percentageList:
            meassurement += (f" {o[i]} ")
    
    # split the meassurement list every number of categories and append i to meassurementList
    length = len(categoryList)
    while meassurement:
        meassurementList.append(meassurement[:length * 3])
        meassurement = meassurement[length * 3:]

    # Use zip() to join the yAxis and meassurementList lists into one
    preGraphics = [x for y in zip(yAxis, meassurementList) for x in y]

    # Join each two pair of elements in preGraphics and concatenate them in the variable
    # to be passed as the first part of the graphics
    odd = ""
    even = ""

    for i in range(len(preGraphics)):
        if i % 2 != 0:
            odd = preGraphics[i]
            
        elif i % 2 == 0:
            even = preGraphics[i]
            if even == even:
                continue
        
        graphics += f"{even}{odd}\n"

    # Vertical categories
    for i in range(charCount):
        for vertical in categoryList: 
            # Print like this if the category is the first one
            if  vertical == categoryList[0]:
                categoriesToPrint += f"     {vertical[i]} "
            # Print like this for the rest
            else:
                categoriesToPrint += f" {vertical[i]} "
        categoriesToPrint += "\n"

    # Variable to return with the configured chart
    printable = graphicsTitle + graphics + divisoryLine + categoriesToPrint

    return printable
    
    
    
    
food = Category("Food")
food.deposit(1000, "initial deposit")
food.withdraw(10.15, "groceries")
food.withdraw(15.89, "restaurant and more food for dessert")
print(food.get_balance())
clothing = Category("Clothing")
food.transfer(50, clothing)
print(food.get_balance())
clothing.withdraw(25.55)
print(clothing.get_balance())
clothing.withdraw(100)
print(clothing.get_balance())
auto = Category("Auto")
auto.deposit(1000, "initial deposit")
auto.withdraw(15)

print(food)
print(clothing)

print(create_spend_chart([food, clothing, auto]))