
#creating list of products using nested dictionary 
products = {
    'Sandwich': {
        'D1': ('chicken', 3),
        'D2': ('tuna', 3.50),
        'D3': ('vegtable', 2),
        'D4': ('cheese',2)
    },
    'Chips': {
        'A1': ('sohar', 2.50),
        'A2': ('ruffles', 4),
        'A3': ('salad', 1),
        'A4': ('pringles',4.50)
    },
    'Biscuits': {
        'E1': ('oreo', 2.50),
        'E2': ('biscoff', 3),
        'E3': ('parle g', 1.50),
        'E4': ('cookie monsta',1.75)
    },
    'Chocolates': {
        'B1': ('minstrels', 4),
        'B2': ('m&m',3.50),
        'B3': ('kitkat', 1.50),
        'B4': ('flakes', 2)
    },
    'Drinks': {
        'C1': ('cola', 2.50),
        'C2': ('pepsi', 2.50),
        'C3': ('dew', 2.50),
        'C4': ('water', 1)
    },
}

print('\n WELCOME TO THE VENDING MACHINE!') #prints welcome message for the user

#creating a function named display to show the products
def display(): 
    print('\n Available items: ')
    print('--------------------------------------------------')
    print(f'{"code":<6} {"category":<15} {"item":<20} {"cost":<15}')
    print('--------------------------------------------------')
    for key, value in products.items():
         for value_num, (value_name, value_cost) in value.items():
             print(f'{value_num:<6} {key:<15} {value_name:<20} {value_cost:<15.2f}')
        
# creating a function named question to ask the user for input
def question():
    total_cost= 0 #tuple for total cost created to add total cost
    order_list= [] #empty list created to add which all items user chose
    while True:
        user = input('\n Enter the product number of your choosing: ').strip().upper() #askin user for input
        for key, value in products.items():
            if user in value: #checking if user is available in value
                value_name, value_cost = value[user]
                print(f"\n You have selected {user} - {value_name} for the cost ${value_cost:.2f}") #prints chosen item and its details 
                total_cost += value_cost # adding the user asked product's cost to total cost
                order_list.append(value_name) # adding the user asked product's name to order list
                return total_cost, order_list #returning total cost and order list 
        print('\n Invalid code, try again')   # prints error if user inputs other than whats in the list

#creating a function to ask user if user needs any more items         
def new_question():
        while True: #loop to ask user any more items till user decides to exit
            user = input('\n Do u want anything else? (press: 1 for yes, 2 for no): ').strip().lower() # asking input from user if they need any more item 
            if user == '1': 
                return True # if user chooses YES
            elif user == '2':
                return False #if user chooses NO
            print('\n Invalid code, try again') #prints error if user types anything other than 1 or 2
        

#creating money function for the money proccesing 
def money(total_cost,order_list):
        while True: # loop created so it will repeat until the user enters correct or more amount of money
            try:
                print(f'\n the total cost is ${total_cost:.2f}') #prints the total cost of all chosen item by user
                user = float(input('\n Input your money: ') ) #asking user to input the cash
                if user>= total_cost: #only works if user input is greater than or equal to total cost
                    balance= user - total_cost
                    print(f'\n The total cost is ${total_cost:.2f}, you have inputted ${user:.2f}, you have a balance of ${balance:.2f}')# prints the total cost, the user input money and balance
                    print(f'\n The following products have been dispensed: {order_list} ') #prints what all product have been dispensed
                    print('\n THANKYOU FOR PURCHASING WITH US!! \n') #prints thankyou message for the user
                    break #will stop here if the user enterred greater or equal to total cash
                else:# only works if user input is smaller than total cost
                    balance= total_cost - user
                    print(f'\n you have only inputted ${user}, the amount is insufficient to cover the total cost')#prints that the user needs enough to cover the total cost
            except ValueError: 
                print('\n Invalid input, please enter a valid number') #prints error if user enters anything other than number

#calling display function
display()

total_cost = 0
order_list = []  
while True:
    prices, orders = question() # calling the question function and assigning the output to prices & orders
    total_cost += prices # adding all the user asked products cost together
    order_list.extend(orders)  # adding all the user aked products name together
    if not new_question(): #looping new_question until user exits
        break # breaks if the user chooses not to have any more items

#calling money function with its variable
money(total_cost, order_list)
     