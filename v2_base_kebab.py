import pandas
from datetime import date


# shows instructions
def show_instructions():
    print('''\n
***** Instructions ******


For each order, enter ...
- The person's name (cannot be blank)
- Age (between 12 and 120)


When you have entered all the users, press 'xxx' to quit.


The program will then display the kebab details
including the cost of each kebab, and the total cost.


This information will also be automatically written to
a text file.


**********************''')


# Show Menu
def show_menu():
    print('''\n
***** Menu ******




Size:                        REGULAR     LARGE    Number ID
Chicken Kebab                  $14        $24         1
Beef Kebab                     $16        $26         2
Lamb Kebab                     $16        $24         3
Veggie Kebab                   $17        $24         4
Paneer Tikka Kebab             $15        $23         5
Fish Kebab                     $13        $24         6


Gourmet kebabs    
Herb-Marinated Chicken Kebab   $27        $31         7
Grilled Lamb Kebab             $23        $32         8
Prawn Kebab                    $19        $31         9
Beef Tenderloin Kebab          $23        $32         10


Sides:              500ML    Number ID
Water                $6          1
Sprite               $6          2
Coca-Cola            $6          3
Fanta                $6          4
Mountain Dew         $6          5


**********************''')


# Function to check for valid responses based on options
def string_checker(question, num, valid_ans):
    while True:
        error = f"Enter a valid option from {valid_ans}"
        user_response = input(question).lower()
        for item in valid_ans:
            if item == user_response:
                return item
            elif user_response == item[:num]:
                return item
        print(error)
        print()


# Checks that user response is not blank
def not_blank(question):
    while True:
        response = input(question)
        if response == "":
            print("Sorry this can't be blank. Please try again")
        else:
            return response


# Yes or no function for a question
def yes_no(question):
    to_check = ["yes", "no"]
    valid = False
    while not valid:
        response = input(question).lower()
        for var_item in to_check:
            if response == var_item:
                return response
            elif response == var_item[0]:
                return var_item
        print("Please enter either yes or no...\n")


# Checks users enter an integer to a given question
def num_check(question, low, high):
    error = f"Enter a number between {low} and {high}"
    while True:
        try:
            response = int(input(question))
            if low <= response <= high:
                return response
            else:
                print(error)
        except ValueError:
            print(error)


# Currency formatting function
def currency(x):
    return "{:.2f}".format(x)


# Check which kebab is selected and assign the name
def kebab_id_checker(id, size):
    if id == 1 and size == "regular":
        kebab = "Chicken Kebab"
        price = 14
    elif id == 1 and size == "large":
        kebab = "Chicken Kebab"
        price = 24
    elif id == 2 and size == "regular":
        kebab = "Beef Kebab"
        price = 16
    elif id == 2 and size == "large":
        kebab = "Beef Kebab"
        price = 26
    elif id == 3 and size == "regular":
        kebab = "Lamb Kebab"
        price = 16
    elif id == 3 and size == "large":
        kebab = "Lamb Kebab"
        price = 24
    elif id == 4 and size == "regular":
        kebab = "Veggie Kebab"
        price = 17
    elif id == 4 and size == "large":
        kebab = "Veggie Kebab"
        price = 24
    elif id == 5 and size == "regular":
        kebab = "Paneer Tikka Kebab"
        price = 15
    elif id == 5 and size == "large":
        kebab = "Paneer Tikka Kebab"
        price = 23
    elif id == 6 and size == "regular":
        kebab = "Fish Kebab"
        price = 13
    elif id == 6 and size == "large":
        kebab = "Fish Kebab"
        price = 24
    elif id == 7 and size == "regular":
        kebab = "Herb-Marinated Chicken Kebab"
        price = 27
    elif id == 7 and size == "large":
        kebab = "Herb-Marinated Chicken Kebab"
        price = 31
    elif id == 8 and size == "regular":
        kebab = "Grilled Lamb Kebab"
        price = 23
    elif id == 8 and size == "large":
        kebab = "Grilled Lamb Kebab"
        price = 32
    elif id == 9 and size == "regular":
        kebab = "Prawn Kebab"
        price = 19
    elif id == 9 and size == "large":
        kebab = "Prawn Kebab"
        price = 31
    elif id == 10 and size == "regular":
        kebab = "Beef Tenderloin Kebab"
        price = 23
    else:
        kebab = "Beef Tenderloin Kebab"
        price = 32
    return kebab, price


# Uses drink id to identify 500ml drinks
def drink_id_checker(id):
    if id == 1:
        drink = "Sprite"
        price = 6
    elif id == 2:
        drink = "Coca-Cola"
        price = 6
    elif id == 3:
        drink = "Fanta"
        price = 6
    elif id == 4:
        drink = "Mountain Dew"
        price = 6
    elif id == 5:
        drink = "Water"
        price = 6
    return drink, price


# Print Function to pizzeria
print("Welcome to Feta Pizzeria")

# Set maximum number of kebabs below
MAX_KEBAB = 5

yes_no_list = ["yes", "no"]
deliv_option = ["delivery", "pickup"]
all_regular = ["regular", "large"]
drink_options = ["sprite", "coca-cola", "fanta", "mountain dew", "water"]
address = ""
# List to hold kebab details
all_name = ["Chicken Kebab", "Beef Kebab", "Lamb Kebab", "Veggie Kebab", "Paneer Tikka Kebab", "Fish Kebab",
            "Herb-Marinated Chicken Kebab", "Grilled Lamb Kebab", "Prawn Kebab", "Beef Tenderloin Kebab"]

all_drinks = ["Sprite", "Coca-Cola", "Fanta", "Mountain Dew", "Water"]

drink_cost = ["$6", "$6", "$6", "$6", "$6"]
all_regular_size = ["$14", "$16", "$16", "$17", "$15", "$13", "$27", "$23", "$19", "$23"]
all_large_size = ["$24", "$26", "$24", "$24", "$23", "$24", "$31", "$32", "$31", "$32"]
all_kebab_cost = []
payment_list = ["cash", "credit"]

# **** Get current date for heading and filename ****
# get today's date
today = date.today()

# Get day, month and year as individual strings
day = today.strftime("%d")
month = today.strftime("%m")
year = today.strftime("%Y")

heading = "---- Kebab House Data ({}/{}/{}) ----\n".format(day, month, year)
filename = "MMF_{}_{}_{}".format(year, month, day)

# kebab order
user_order_kebab = []
user_order_kebab_size = []
user_order_cost = []

# drink order
user_order_drinks = []
user_order_drink_cost = []

kebab_order = []

total_price = 0
delivery_surcharge = 0
payment_surcharge = 0

# Dictionary used to display kebab menu
kebab_dict = {
    "Name": all_name,
    "Large": all_large_size,
    "Regular": all_regular_size
}

# Dictionary used to store kebab orders
order_dict_kebab = {
    "kebab": user_order_kebab,
    "Size": user_order_kebab_size,
    "Price": user_order_cost
}

# Dictionary used to store drinks
order_dict_drink = {
    "Drink": user_order_drinks,
    "Price": user_order_drink_cost
}

# Would you like to read instructions
want_instructions = string_checker("Do you want to read the instructions/menu (y/n) : ", 1, yes_no_list)

if want_instructions == "yes":
    show_instructions()

# After pickup or delivery show menu
print("Here is the menu:")
show_menu()

# Name user enters to order
# Age check for users to order
name = not_blank("Enter your name: ")
age = num_check("Enter your age: ", 12, 120)

# Pick up/Delivery Function
delivery = string_checker("Do you want pickup or delivery? (or 'xxx' to quit) ", 1, deliv_option)

if delivery == 'xxx':
    quit()
elif delivery == "delivery":
    print("There is a $6 delivery surcharge")
    address = not_blank("Enter your address: ")
    phone_number = num_check("Enter your phone number: ", 0, 999999999)

    delivery_surcharge = 6
    total_price += delivery_surcharge
else:
    phone_number = num_check("Enter your phone number: ", 0, 999999999)

# Ordering from selection
keep_going = "yes"
count = 0

while keep_going == "yes":
    # Create data frame from dictionary to organize information
    kebab_selection_frame = pandas.DataFrame(kebab_dict)
    kebab_selection_frame.index += 1

    print(kebab_selection_frame)

    user_order_id = num_check("What kebab would you like to order?(Use the number ID next to the kebab)", 1, 10)

    user_order_size = string_checker("What size kebab would you like?(Regular or Large) ", 1, all_regular)

    user_order_kebab_size.append(user_order_size)

    user_order_name, kebab_price = kebab_id_checker(user_order_id, user_order_size)

    user_order_kebab.append(user_order_name)
    user_order_cost.append(kebab_price)
    all_kebab_cost.append(kebab_price)

    # Add the kebab price to the total price
    total_price += kebab_price

    print(f"You have chosen a {user_order_size}, {user_order_name} ${user_order_cost[count]}")

    count += 1

    keep_going = yes_no("Enter 'yes' to order another kebab, or type 'no' to finish ")

# Option to order drinks
while True:
    # Display drink menu
    print("\n----- Drink Menu -----")
    for i, drink in enumerate(all_drinks, 1):
        print(f"{i}. {drink} - {drink_cost[i - 1]}")

    # Ask user if they want to order a drink
    order_drink = string_checker("Would you like to order a drink? (yes/no): ", 1, yes_no_list)

    if order_drink == "no":
        break

    # Get drink ID from user
    drink_id = num_check("Enter the drink ID: ", 1, 5)
    drink_name, drink_price = drink_id_checker(drink_id)

    user_order_drinks.append(drink_name)
    user_order_drink_cost.append(drink_price)

    # Add the drink price to the total price
    total_price += drink_price

    print(f"You have chosen a {drink_name} for ${drink_price}")

# Update order dictionaries with drinks
order_dict_kebab.update({"Drink": user_order_drinks, "Drink Price": user_order_drink_cost})

# Create DataFrames for kebabs and drinks


kebab_order_frame = pandas.DataFrame({
    "kebab": user_order_kebab,
    "Size": user_order_kebab_size,
    "Price": user_order_cost
})
kebab_order_frame.index += 1
drink_order_frame = pandas.DataFrame({
    "Drink": user_order_drinks,
    "Price": user_order_drink_cost
})
drink_order_frame.index += 1

# Combine the DataFrames
combined_order_frame = pandas.concat([kebab_order_frame, drink_order_frame], axis=1)

# Calculate total including surcharge
total_price_with_surcharge = total_price + payment_surcharge

# List holding content to print/write to file
# List holding content to print/write to file
to_write = [
    heading,
    "\n----- Order Details -----",
    "Name: {}.".format(name.capitalize()),
    "Phone Number: {}".format(phone_number),
    "Address: {}".format(address) if delivery == "delivery" else "",
    "",  # Blank line for whitespace
    "",  # Another blank line for additional whitespace
    "Kebab Names: {}".format(', '.join(user_order_kebab)),
    "Kebab Sizes: {}".format(', '.join(user_order_kebab_size)),
    "Kebab Costs: ${}".format(', '.join(map(str, user_order_cost))),
    "Drink Names: {}".format(', '.join(user_order_drinks)),
    "Drink Costs: ${}".format(', '.join(map(str, user_order_drink_cost))),
    "Delivery Surcharge: ${}".format(currency(delivery_surcharge)),
    "Total Kebab/Drink Costs (May Include Delivery Cost): ${}".format(currency(total_price)),
]


print("\n".join(to_write))

# Change frame to a string so that we can export it to file
combined_order_string = pandas.DataFrame.to_string(combined_order_frame)

# Create file to hold data (add .txt extension)
write_to = "{}.txt".format(filename)
with open(write_to, "w") as text_file:
    text_file.write("\n".join(to_write))
    text_file.write("\n\n")
    text_file.write(combined_order_string)

    # Get payment method
    pay_method = string_checker("Choose a payment method (cash / credit): ", 2, payment_list)

    if pay_method == "cash":
        payment_surcharge = 0
    else:
        # Calculate 5% surcharge if users are paying by credit card
        payment_surcharge = total_price * 0.05
        total_price += payment_surcharge
        print(f"Surcharge is {currency(payment_surcharge)}, the total cost will be ${total_price} ")

    # Confirm the order, prevent accidental purchase
    confirm_order = string_checker("Do you want to confirm this order?(y/n) ", 1, yes_no_list)

    if confirm_order == "yes":
        print("Order confirmed. Thank you for your purchase!")
    else:
        print("Order canceled.")

print("Program has finished")
