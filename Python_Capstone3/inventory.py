# this program keeps stock of different shoes and gives the user a few options to manage the inventory, it uses OOP

# importing math to use the min and ceil methods
import math

# definign the Shoe class which will contain the inventory data about each type of shoe
class Shoe():
# defining the constructor which will take a country, code, description, cost per item and quantity available    
    def __init__(self, country, code, product, cost, quantity):
        self.country = country
        self.code = code
        self.product = product
        self.cost = cost
        self.quantity = quantity

# definign a method to get the cost of a shoe    
    def get_cost(self):
        return self.cost

# defining a method to get the quantity of a shoe available    
    def get_quanty(self):
        return self.quantity

# definign a method which will print out the inventory data as part of a table    
    def __str__(self):
        print(f"| {self.country :<15}", f"| {self.code :<10}", f"| {self.product :<20}", f"| {self.cost :<6}", f"| {self.quantity :<10}|")

# initiating an empty list to store Shoe objects in
shoes = []

# definign a function to import the shoe data from "inventory.txt"
def read_shoes_data():
# try to read "inventory.txt" and populate shoes    
    try:
        with open("inventory.txt", "r") as inventory:
# skip the header and read in all of the shoe data            
            lines = inventory.readlines()[1:]
            for line in lines:
# split the string into a list at every ","                
                pair = str(line).split(",")
# initiate a new Shoe object for each line of the inventory data
# try to cast the last 2 atributes to int                
                try:
                    shoes.append(Shoe(pair[0], pair[1], pair[2], int(pair[3]), int(pair[4])))
# if it fails, continue reading but print an error informing the user that that shoe failed                
                except ValueError:
                    print(f"**ERROR** either the \"cost\" or \"quantity\" value for the shoe {pair[2]}, code: {pair[1]} are not of type int")
               
# if inventory.txt is not found, give the user the option to create a blank inventory file
    except FileNotFoundError:
        while True:
            not_found_menu = input("The file \"inventory.txt\" was not found. Do you want to create a blank one?\nyes/no: ")
# if the user decides to do this, create "inventory.txt"            
            if not_found_menu == "yes":
                with open("inventory.txt", "w") as inventory:
# write the header                    
                    inventory.write("Country,Code,Product,Cost,Quantity")
# prompt the user to add a shoe to "inventory.txt"
                capture_shoes()
                break
# if the user does not want to create a new file, end the program            
            elif not_found_menu == "no":
                quit()
# if the user enters anything else, print an error and reprompt            
            else:
                print("Sorry, that is not a valid option")

# defining a function to add a new type of shoe to the inventory
def capture_shoes():
# prompt for a country    
    country = input("In which country is the shoe produced?\n:")
    
# create an empty list that will contain the current codes in the inventory    
    shoe_codes = []
    while True:
# prompt the user for a code        
        code = input("Please create a stock code for the shoe.\n:")
# populate the list of all of the codes currently in the inventory        
        for pair in shoes:
            shoe_codes.append(pair.code)
# if the user code is already in the list print an error        
        if code in shoe_codes:
            print("Sorry, a shoe with that code already exists")
# else except the code and continue        
        else:
            break

# prompt for a name     
    product = input("What is the name of the shoe?\n:")
    
# prompt for cost and quantity as ints, if the user does not input an int, displan an error and reprompt    
    while True:
        try:
            cost = int(input("What is the retail price of the shoe?\n:"))
            quantity = int(input("How many of the shoe is in storage?\n:"))
            break
        except ValueError:
            print("Sorry, either the \"cost\" or \"quantity\" value for the shoe is not of type int.")
# write the shoe data to "inventory.txt" and call "read_shoe_data" to refresh data
    with open("inventory.txt", "a") as inventory:
                    inventory.write(f"\n{str(country)},{str(code)},{str(product)},{str(cost)},{str(quantity)}")
    read_shoes_data()

# defingina function to view all of the shoes in inventory
def view_all():
# print a table header    
    print(f"\n  {'Country' :<15}", f"  {'Code' :<10}", f"  {'Product' :<20}", f"  {'Cost' :<6}", f"  {'Quantity' :<10}")
# for each Shoe object call the "__str__" method to display it's data in a table format    
    for pair in shoes:
        pair.__str__()

# definign a function to add stock to the shoe with the lowest quantity
def re_stock():
# create a new list from the list "shoes" this time sorted by the quantity atribute    
    re_stock_list = sorted(shoes, key=lambda x:x.quantity)
# print a message giving the user data about the shoe and ask them to enter a number if they want to resupply it    
    print(f"{re_stock_list[0].code}:{re_stock_list[0].product} is the shoe with the least stock.\n"\
        f"Only {re_stock_list[0].quantity} pair available.")
    add_stock = input("If you would like to add stock please enter the number of pairs to add, else press ENTER\n:")
# if the user enters nothing end the function    
    if add_stock =="":
        return
# if the user inputs something try and cast the input to an int and add it to the quantity
    else:
        try:
            re_stock_list[0].quantity += int(add_stock)
            print("Stock added!")
# if the user enters a non-int print an error        
        except ValueError:
            print("Please enter a value or press ENTER to continue")
    
# write the updated inventory to "inventory.txt"    
    with open("inventory.txt", "w") as inventory:
        inventory.write("Country,Code,Product,Cost,Quantity\n")
        for shoe in re_stock_list:
            inventory.write(f"{shoe.country},{shoe.code},{shoe.product},{shoe.cost},{shoe.quantity}\n")

# defining a function to search for a shoe by it's code
def search_shoe(code):
# create a list of codes currently in inventory    
    shoe_codes = []
    for pair in shoes:
        shoe_codes.append(pair.code)
# if the user code is in the list of current codes, print the shoie data in a table    
    if code in shoe_codes:
        print(f"  {'Country' :<15}", f"  {'Code' :<10}", f"  {'Product' :<20}", f"  {'Cost' :<6}", f"  {'Quantity' :<10}")
        for pair in shoes:
            if pair.code == code:
                pair.__str__()
# otherwise print an error    
    else:
        print("Sorry, there is no shoe with that code")

# definign a function to get the total value of stock for each shoe
def value_per_item():
    print(f"  {'Country' :<15}", f"  {'Code' :<10}", f"  {'Product' :<20}", f"  {'Value' :<10}")
    for pair in shoes:
# print out the inventory data but combine cost and quantity into value with value = cost * quantity        
        print(f"| {pair.country :<15}", f"| {pair.code :<10}", f"| {pair.product :<20}", f"| {pair.cost * pair.quantity :<10}|")

# defining a function to put the shoe with most stock on sale
def highest_qty():
# create a list sorterd by quantity from high to low    
    sale_list = sorted(shoes, key = lambda x:x.quantity, reverse = True)
# return data on the highest stocked shoe and ask the user if they want to start a sale    
    print(f"{sale_list[0].code}:{sale_list[0].product} is the shoe with the most stock"\
        f"There are {sale_list[0].quantity} pairs available. Do you want to start a sale?")
    
    while True:
        start_sale = input("yes/no: ")
# if the user selects yes reduce the cost of the shoe by 50%        
        if start_sale == "yes":
            sale_list[0].cost = math.ceil(sale_list[0].cost * 0.5)
# write the new inventory data to "inventory.txt"            
            with open("inventory.txt", "w") as inventory:
                inventory.write("Country,Code,Product,Cost,Quantity\n")
                for shoe in sale_list:
                    inventory.write(f"{shoe.country},{shoe.code},{shoe.product},{shoe.cost},{shoe.quantity}\n")
# tell the user the shoe is on sale            
            print("The shoe is now in sale!")
            break
# if the user selects no, take them back to the main menu        
        elif start_sale == "no":
            break
# if the user enters anything else, print an error        
        else:
            print("Sorry, that is not a valid option.")

# print a welcome message
print("\033[1mWelcome to the OOP shoe inventory program!\033[0m")

# present the user with the main menu
while True:
    main_menu = input(
        "\n\t\t\033[1mwhat would you like to do?\033[0m\n"\
        f"{'import' :<12} - read in shoe data from \"inventory.txt\"\n"\
        f"{'capture' :<12} - capture data for a new shoe not in inventory\n"\
        f"{'view all' :<12} - view inventory data on all shoes\n"\
        f"{'buy' :<12} - get more stock of the shoe with the least amount of pairs left\n"\
        f"{'search' :<12} - retrieve the inventory data of a shoe by searching the code\n"\
        f"{'valuation' :<12} - return the stock value of all of the shoes in inventory\n"\
        f"{'sale' :<12} - put the shoe with the highest quantity on 50% sale\n"\
        f"{'quit' :<12} - exit the program\n: "
        )
    
# if the list "shoes" contains any shoes all of the menu items are available
    if len(shoes) > 0:
        
# if the user selects "import" call the "read_shoes_data" function        
        if main_menu == "import":
            read_shoes_data()
            print("Data imported!")
        
# if the user selects "capture" call the "capture_shoes" function
        elif main_menu == "capture":
            capture_shoes()
            print("Shoe data added!")
        
# if the user selects "view all" call the "view_all" function
        elif main_menu == "view all":
            view_all()
        
# if the user selects "buy" call the "re_stock" function        
        elif main_menu == "buy":
            re_stock()
        
# if the user selects "search" ask for a code and call the "search_shoe" function passing the user code
        elif main_menu == "search":
            search_code = input("What is the code?\n:")
            search_shoe(search_code)
        
# if the user selects "valuation" call the "value_per_item" function
        elif main_menu == "valuation":
            value_per_item()
        
# if the user selects "sale" call the "highest_qty" function
        elif main_menu == "sale":
            highest_qty()
        
# if the user selects "quit" end the program
        elif main_menu == "quit":
            quit()
        else:
            print("Sorry, that's not a valid option")
    
# if the user selects "quit" end the program even if no data has been imported
    elif main_menu == "quit":
        quit()

# if the user selects "import" call the "read_shoes_data" function    
    elif main_menu == "import":
        read_shoes_data()
        print("Data imported!")
    
# if there are no shoes in the "shoes" list and the user selects anything except "import" or "quit", display an error    
    else:
        print("Sorry, please import data first")