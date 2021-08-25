# exercises
# 1) Build a Shopping Cart
# Should have the following capabilities:
# 
# 1) Takes in input
# 2) Stores user input into a list
# 3) User can add or delete items
# 4) User can see current shopping list
# 5) Loops until user 'quits'
# 6) Upon quiting the program, print out all items in the user's list
# add
# remove
# show
# instructions
# application logic (how the application flows)
# add
# remove
# show
# instructions
# application logic (how the application flows)

def show_instructions():
    print("""
Type 'add' to add new item's to your cart.
Type 'remove' to remoce item's from your cart.
Type 'show' to list all items in your cart. 
Type 'checkout' to exit the program. """)
    
    info = []

    def cart():
        input('Welcome to your cart! Press any key to continue ')
    while True:
        choice = input('Would you like to add anything into your cart? ')
    
        if choice == 'add':
            item = input("Type in name of item ").title()
            
            item_dict = {'bananas': bananas,
                         'eggs': eggs,
                         'water': water,
                         'cereal': cereal,
                         'milk': milk
                        }
            
            info.append(item_dict)
        
        elif choice == 'show':
            for items in info:
                print(items)
            input('Press any key continue')
            
    done = False
    while not done:
            
        elif choice == 'checkout':
            confirm = input('Are are you sure you want to checkput? Y/N? ').lower()
            if confirm == 'y':
                done = True
            elif confirm == 'n':
                continue
    
cart()


# 2) Create a Module in Visual Studio Code and Import It
# Module should have the following capabilities:
# 
# 1) Has a function to calculate the square footage of a room
# 2) Has a function to calculate the circumference of a circle
# 
# Program in Jupyter Notebook should take in user input and use imported functions to calculate a circle's circumference or a houses square footage
# 
# **Note: When using functions in Python, arguments are passed in by reference, NOT

def area_circumference():
    print(""""Welcome! Would you like to find the area of a room or circumference of a circle? """)
    while True:    
        shape = input("""Type 'room' to find area 
Type 'circle' to find circumference
Type 'quit' to exit the program | """)

        if shape == 'room':
            x = float(input("What is the length in feet? | "))
            y = float(input("What is the width in feet? | "))
            print(x * y, 'ft.^2' )
            
        elif shape == 'circle':
            r = float(input("What is the length of the radius in feet? | "))
            print(r * 2 * 3.14, 'ft.' )
        elif shape == 'quit':
            return
        else:
            input('That was an invalid option. Please try again. Press any key to continue. | ')
            continue
        
        done = False
        while not done:
            confirm = input('Would you like to continue? Y/N | ').lower()

            if confirm == 'n':
                return
            elif confirm == 'y':
                break
            else:
                input('That was an invalid option. Please try again. Press any key to continue. | ')
                

measurement = area_circumference()