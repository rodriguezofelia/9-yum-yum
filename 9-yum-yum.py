import random

# EXIT_STORE store is used to determine if a customer doesn't want ice cream
EXIT_STORE = False
# NUMBER_OF_ICECREAMS_ORDERED keeps track of how many ice creams have been ordered
NUMBER_OF_ICECREAMS_ORDERED = 0
# USER_CHOICES keeps track of all the choices the customer makes
USER_CHOICES = {}

# greeting() welcomes the user to the shop and gives them an overview of what they can do through print statements
def greeting():
    print("Welcome to the 9 Yum Yum Scoop Shop! \n")

    print("If you're into yummy ice cream you've come to the right place. \n")

    print("Before we can attend to your ice cream emergency, let me walk you through your options. \n")

    print("You can choose between a cup or a cone. You can pick your flavor or be surprised (picked by random!). You can choose a size and select any toppings you may like to add. You will be given the specific options soon. \n")

# get_icecream() allows the user to enter the scoop shop or exit 
def get_icecream():
    global EXIT_STORE
    while True: 
        proceed = input("Okay...are you ready? Enter Ready to proceed or Exit to quit. > \n").lower()
        if proceed == "ready":
            print("Alright, let's go! \n")
            EXIT_STORE = False
            return True

        elif proceed == "exit":
            print("Aw that's too bad! Come back soon. \n")
            EXIT_STORE = True
            return False

        else:
            print("Sorry, I didn't get that. Let's try this again! \n")

# flavor_choices() gives the customer the ice cream options and sets USER_CHOICES with the selected options by the customer
def flavor_choices():

    global NUMBER_OF_ICECREAMS_ORDERED

    if get_icecream(): 

        icecream_flavors_available = ['vanilla', 'chocolate', 'mint chocolate chip', 'bunny tracks', 'birthday cake', 'creamsicle', ]

        while True: 

            icecream_flavors = input("Enter Yum to see what the ice cream options are available? > \n").lower()

            if icecream_flavors == "yum":
                print(icecream_flavors_available)
            
                icecream_choice = input("Which of the available flavors would you like? If you'd like to be surprised, enter surprise. > \n").lower()

                if icecream_choice not in icecream_flavors_available and icecream_choice != "surprise" : 
                    print("Hmm..it doesn't look that flavor is available. Try again.  \n")
                
                elif icecream_choice == "surprise":
                    surprise_icecream = random.choice(icecream_flavors_available)
                    print(f"Looks like you got {surprise_icecream}! \n")
                    
                    NUMBER_OF_ICECREAMS_ORDERED += 1
                    
                    current_ice_cream_order = surprise_icecream + str(NUMBER_OF_ICECREAMS_ORDERED)

                    USER_CHOICES[current_ice_cream_order] = {
                        'flavor': surprise_icecream,
                        'size': '',
                        'toppings': [],
                        'container': ''
                    }
                    return current_ice_cream_order
                
                else: 
                    print("Excellent choice! Let me scoop that up for you. \n")
                    
                    NUMBER_OF_ICECREAMS_ORDERED += 1

                    current_ice_cream_order = icecream_choice + str(NUMBER_OF_ICECREAMS_ORDERED)

                    USER_CHOICES[current_ice_cream_order] = {
                        'flavor': icecream_choice,
                        'size': '',
                        'toppings': [],
                        'container': ''
                    }
                    return current_ice_cream_order

            else: 
                print("Sorry, I didn't get that. Did you mean to spell yum? \n")
                continue
         
# cone_or_cup() allows the user to determine what type of container they want for their ice cream and sets USER_CHOICES with the selected options by the customer
def cone_or_cup():
    current_ice_cream_order = flavor_choices()

    # If current order exists
    if current_ice_cream_order:
        while True: 
            icecream_holder = input("Would you like a cup or a cone? > ").lower()

            if icecream_holder == "cup":
                print("Sounds good, a cup it is! \n")
                USER_CHOICES[current_ice_cream_order]['container'] = icecream_holder
                return current_ice_cream_order
            
            elif icecream_holder == "cone": 
                kind_of_cone = input("Woud you like a sugar or buttermilk cone? > \n").lower()

                if kind_of_cone == "sugar":
                    print("Sugar it is! ")
                    USER_CHOICES[current_ice_cream_order]['container'] = kind_of_cone + " cone"
                    return current_ice_cream_order
                
                elif kind_of_cone == "buttermilk":
                    print("That's my favorite! \n")
                    USER_CHOICES[current_ice_cream_order]['container'] = kind_of_cone + " cone"
                    return current_ice_cream_order
                
                else:
                    print("Sorry that's not an option. \n")
                    continue

                    #THIS IF YOU MISPELL SUGAR OR BUTTERMILK IT SHOULD ASK kind_of_cone AGAIN ---- FIX THIS !!!

            else:
                print("Sorry we only have cups or cones. \n")

# icecream_scoops allows the user to select a size and sets USER_CHOICES with the selected options by the customer
def icecream_scoops():
    
    current_ice_cream_order = cone_or_cup() 

    if current_ice_cream_order:

        while True: 
            size = input("What size would you like? You can choose between a single scoop, double scoops or triple scoops. > \n").lower()

            if size == "single":
                print(f"One scoop of {USER_CHOICES[current_ice_cream_order]['flavor']} coming right up! \n")
                USER_CHOICES[current_ice_cream_order]['size'] = size
                return current_ice_cream_order

                
            elif size == "double": 
                print(f"Two scoops of {USER_CHOICES[current_ice_cream_order]['flavor']} coming right up! \n")
                USER_CHOICES[current_ice_cream_order]['size'] = size
                return current_ice_cream_order

                
            elif size == "triple":
                print(f"Three scoops of {USER_CHOICES[current_ice_cream_order]['flavor']} coming right up! \n")
                USER_CHOICES[current_ice_cream_order]['size'] = size
                return current_ice_cream_order
                
            else: 
                print("Sorry, it doesn't look like we have that size. Please try again.  \n")           

# toppings() allows the user to add as many toppings as they'd like and sets USER_CHOICES with the selected options by the customer
def toppings():
    current_ice_cream_order = icecream_scoops()

    if current_ice_cream_order:

        while True: 

            toppings = ['sprinkles', 'chocolate sauce', 'whipped cream', 'strawberry sauce']

            want_toppings = input("We have the following toppings available: sprinkles, chocolate sauce, whipped cream, and strawberry sauce. Enter yes to add toppings or exit for no toppings. \n")

            if want_toppings == "yes":
                which_topping = input("Perfect, which topping would you like to add? Enter one at a time. > \n").lower()
                
                if which_topping in toppings:
                    print(f" Great choice, adding {which_topping}! ")
                    USER_CHOICES[current_ice_cream_order]['toppings'].append(which_topping)

                    add_another_topping = input("Would you like to add more toppings? Enter Yes or No. > \n")

                    if add_another_topping == "yes":
                        continue
                    elif add_another_topping == "no":
                        more_icecream()
                        break

                else: 
                    print("Sorry, I didn't get that. \n")
                    continue
            
            elif want_toppings == "exit":
                print(f"Okay, your {USER_CHOICES[current_ice_cream_order]['flavor']} ice cream is coming right up with no toppings. \n")
                more_icecream()
                break
                #IF USER SAYS THEY WANT TO EXIT AFTER THEY SAID YES TO ADDING ANOTHER TOPPING, IT WILL PRINT THIS STATEMENT ABOVE. THEN IT WILL CALL THE MORE ICE CREAM FUNCTION TO ASK IF THEY WANT TO ADD MORE TO THEIR ORDER

            else: 
                print(f"Sorry, I didn't get that. \n")
                continue

# more_icecream() asks the user if they'd like any additional ice cream. If they say yes, they'll get pushed back to toppings()
def more_icecream():

    while True: 
        additional_icecream_order = input("Would you like to order more ice cream? Enter Yes or No > ").lower()

        if additional_icecream_order == "yes":
            toppings()
            break
                
        elif additional_icecream_order == "no":
            break

# cost() takes 3 parameters and calculates the cost of the ice cream the user previously ordered
def cost(size, container, toppings):

        tax = 0.083

        size_pricing = {
            "single": 3.50, 
            "double": 4.50, 
            "triple": 5.50
        }

        container_pricing = {
            "cup": 0, 
            "sugar cone": 1.00, 
            "buttermilk cone": 1.50,  
        }

        toppings_pricing = {
            "sprinkles": 1.00, 
            "chocolate sauce": 1.25, 
            "whipped cream": 1.00,
            "strawberry sauce": 1.25
        }

        cost_of_topping = 0

        for topping in toppings:
            cost_of_topping += toppings_pricing[topping]

        price = size_pricing[size] + container_pricing[container] + cost_of_topping

        total_cost = price + (tax * price)

        return round(total_cost,2)
    
# build_icecream() calls greeting() and toppings()
def build_icecream():

    greeting()

    toppings()

    # If customer orders and ice cream this will print set total cost to 0 and print a statement 
    if EXIT_STORE == False:

        total_cost = 0

        print_statement = "Okay your order of: \n"

        # print("The user choices dictionary is equal to:")
        # print(USER_CHOICES)
        # print('\n \n')
        # print("The user choices dictionary in .items() form is equal to:")
        # print(USER_CHOICES.items())
        # print('\n \n')

        # items split keys and values of a dictionary into an iterable list
        for key, value in USER_CHOICES.items():
            # print("The key variable is equal to: ")
            # print(key)
            # print('\n \n')
            # print("The value variable is equal to: ")
            # print(value)

            current_ice_cream_cost = cost(value['size'], value['container'], value['toppings'])

            total_cost += current_ice_cream_cost
            
            if len(value['toppings']) > 0:
                all_toppings = "with the following toppings: " + (', ').join(value['toppings'])
            else:
                all_toppings = ""
            
            print_statement = print_statement + f"{value['flavor']} in a {value['container']} " + all_toppings + " is coming right up! \n"



        return (f"Okay, your order total is {total_cost}. \n" + print_statement)
    
    else: 
        return "I hope you come back another day! \n"

print(build_icecream())





