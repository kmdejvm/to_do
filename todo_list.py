"""This is a Terminal-based program that allows a user to create and edit a to-do list.

The stub of each function has been provided. Read the docstrings for what each 
function should do and complete the body of the functions below.

You can run the script in your Terminal at any time using the command:

    >>> python todo_list.py

"""

def add_to_list(my_list):
    """Takes user input and adds it as a new item to the end of the list."""
    prompt = "\n What would you like to add to the list?\n>>>"

    new_item = raw_input(prompt)
    my_list.append(new_item)
    new_item[0]

def view_list(my_list):
    for item in my_list:
        print item

def delete_item_from_list(my_list):
    """Deletes an item from the beginning of list"""
    prompt = "\n What would you like to delete from the list?\n>>>"
    new_item = raw_input(prompt)
    my_list.remove(new_item)
        


def display_main_menu(my_list):
    """Displays main options, takes in user input, and calls view or add function."""

    user_options = """
    \nWould you like to:
    A. Add a new item
    B. View list
    C. Delete Item From List
    D. Quit the program
    >>> """

    while True:
        # Collect input and include your if/elif/else statements here.
        user_choice = raw_input(user_options)
        if user_choice == 'A':
            add_to_list(my_list)
        elif user_choice == 'B':
            view_list(my_list) # print list
        elif user_choice == 'C':
            delete_item_from_list(my_list)
        elif user_choice == 'D':    
            break
        else:
            print "sorry that is not an option"
            print "please pick 'A', 'B', or 'C' "

#-------------------------------------------------

my_list = []
display_main_menu(my_list)

