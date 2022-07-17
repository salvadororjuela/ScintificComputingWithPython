#                       --> Constructor <--
class Category:   
    
    def __init__(self, name): # Create the attributes
        
        self.name = name
        self.ledger = list()
        self.balance = 0
        
    
    def deposit (self, amount, description=''): #Put a number and sum to the amount
        self.ledger.append({"amount": amount, "description": description})
        self.balance += amount
        

    def withdraw(self, amount, description=''): # Check if possible and subtract the amount
        if (self.check_funds(amount)):
            self.ledger.append({"amount": -amount, "description": description})
            self.balance -= amount
            return True
        else:
            return False
        
        
    def wd_count(self): #Count the withdraw
        count = 0
        for entry in self.ledger:
            if entry["amount"] < 0:
                count += entry["amount"]
        return count


    def get_balance(self): # print the balance (ez)
        return self.balance


    def transfer(self, amount, category): 
        if (self.check_funds(amount)):
            self.withdraw(amount, 'Transfer to ' + category.name)
            category.deposit(amount, 'Transfer from ' + self.name)
            return True
        else:
            return False
    
    
    def check_funds(self, amount):
    
        if amount > self.balance:
            return False
        else:
            return True
        
    #                   --> String constructor <--    
    def __str__(self): 
            first = f'{self.name:*^30}' + '\n'
            items = ""
            for item in self.ledger: #Slicing the description and printing with .2f precision the num.
                items += f"{item['description'][0:23]:23}" + f"{item['amount']:>7.2f}" + '\n'
                         
            return first + items + 'Total: ' + str(self.balance)
        
    
def create_spend_chart(categories): #Expenses chart 
    title = 'Percentage spent by category'+ '\n'
    total = 0 #total of expenses
    counts = {} #dict of category (key) with related expense (value)
    percentage = {} #percent of each category
    name_length = 0   
   

    for category in categories:
        countkey = category.wd_count() #Grabbing the int value
        counts[category.name] = countkey #Giving a value to each category
        total += countkey #Calculating a total of expenses for each category


    for name, count in counts.items(): #Get the percent and adding to key
        percent = count / total * 100
        percentage[name] = percent
 
    #                   --> Y axis <--
    x = 100 
    for number in range(11):
        row = f"{x}".rjust(3) + "| "
        for name, percent in percentage.items(): #add the values to the chart
            if percent >= (x):
                row += "o  "
            else:
                row += "   "
        title += row + '\n'
        x -= 10
   
    #                   --> X  axis <--
    x_axis = "    -" 
    for category in categories:
        x_axis += ("---")
    title += x_axis + "\n"


    for category in categories: # determines the longest category name length
        if len(category.name) > name_length:
            name_length = len(category.name)
 
    
    y = 0
    while y <= name_length:
        rows = "     "
        for key, value in percentage.items(): # add the category names for x axis values
            category_name = key
            try:    
                rows +=  category_name[y] + "    "
            except: 
                rows += "   "
        
        if y <= name_length -1:
            title += rows + '\n' 
        else:
            title += rows.strip(" ")
           
        y = y + 1
    title = title.rstrip("\n")
    return title


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
