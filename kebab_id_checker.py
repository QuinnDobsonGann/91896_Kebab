def kebab_id_checker(id):
    all_name = ["Chicken Kebab", "Beef Kebab", "Lamb Kebab", "Veggie Kebab", "Paneer Tikka Kebab", "Fish Kebab",
                "Herb-Marinated Chicken Kebab", "Grilled Lamb Kebab", "Prawn Kebab", "Beef Tenderloin Kebab"]
    
    return all_name.get(id, "Unknown kebab")


def num_check(question, min_value=None, max_value=None):
    while True:
        try:
            response = int(input(question))
            if (min_value is not None and response < min_value) or (max_value is not None and response > max_value):
                print(f"Please enter a number between {min_value} and {max_value}.")
            else:
                return response
        except ValueError:
            print("Please enter an integer.")


# Main Routine

user_order_id = num_check("Please enter the number of the kebab you want to order (1-10): ", min_value=1, max_value=10)
user_order_name = kebab_id_checker(user_order_id)

print(f"You have selected {user_order_name}")