import random

# EXIT_STORE determines if the user doesn't want ice cream
EXIT_STORE = False
NUMBER_OF_ICECREAMS_ORDERED = 0
USER_CHOICES = {}

def greeting():
    '''Welcomes the user to the shop and provides an overview of what they can order'''

    print("Welcome to the 9 Yum Yum Scoop Shop! \n")

    print("If you're into yummy ice cream you've come to the right place. \n")

    print("Before we can attend to your ice cream emergency, let me walk you through your options. \n")

    print("You can choose between a cup or a cone. You can pick your flavor or be surprised (picked by random!). You can choose a size and select any toppings you may like to add. You will be given the specific options soon. \n")


def get_icecream():
    '''Takes user input to enter the scoop shop or exit'''

    global EXIT_STORE
    while True: 
        proceed = input("Okay...are you ready? Enter Ready to proceed or Exit to quit. > \n").lower()
        if proceed == "ready":
            print("Alright, let's go! \n")
            EXIT_STORE = False
            return True

        elif proceed == "exit":
            print("Aw that's too bad! \n")
            EXIT_STORE = True
            return False

        else:
            print("Sorry, I didn't get that. Let's try this again! \n")


def flavor_choices():
    '''Provides ice cream options and sets USER_CHOICES with the selected options by the user'''

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
         
def cone_or_cup():
    '''Sets ice cream container and USER_CHOICES with the selected options by the user'''

    current_ice_cream_order = flavor_choices()

    if current_ice_cream_order:
        '''If current order exists, it proceeds'''
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

            else:
                print("Sorry we only have cups or cones. \n")

def icecream_scoops():
    '''Sets ice cream size and USER_CHOICES with the selected options by the user'''
    
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

def toppings():
    '''Sets toppings and USER_CHOICES with the selected options by the user'''
    
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

            else: 
                print(f"Sorry, I didn't get that. \n")
                continue

def more_icecream():
    '''Determines additional ice cream choices, if any'''

    while True: 
        additional_icecream_order = input("Would you like to order more ice cream? Enter Yes or No > ").lower()

        if additional_icecream_order == "yes":
            toppings()
            break
                
        elif additional_icecream_order == "no":
            break

def cost(size, container, toppings):
    '''Takes 3 parameters and calculates the cost of the ice cream the user previously ordered'''

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
    
def build_icecream():
    '''Calls greeting() and toppings()'''

    greeting()

    toppings()

    if EXIT_STORE == False:
        '''Sets total cost to 0 and prints summary'''

        total_cost = 0

        order_summary = "Your order of...\n"

        for key, value in USER_CHOICES.items():
            '''Splits keys and values of dictionary into an interable list'''

            current_ice_cream_cost = cost(value['size'], value['container'], value['toppings'])

            total_cost += current_ice_cream_cost
            
            if len(value['toppings']) > 0:
                all_toppings = "with " + (', ').join(value['toppings'])
            else:
                all_toppings = ""
            
            order_summary = order_summary + f"\n - {value['flavor']} in a {value['container']} " + all_toppings + "\n"



        return (f"\nAlright, your order total is {total_cost}. \n\n" + order_summary + "\n... is coming right up!")
    
    else: 
        return "I hope you come back another day!"

print(build_icecream())
