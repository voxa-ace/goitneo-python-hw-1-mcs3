"""
This is a simple command-line assistant bot for managing contacts.
"""

def parse_input(user_input):
    """
    Parse the user input and extract the command and its arguments.

    Args:
        user_input (str): The user's input string.

    Returns:
        tuple: A tuple containing the command (str)
        and its arguments (list of str).
    """
    cmd, *args = user_input.strip().lower().split()
    cmd = cmd.strip().lower()
    return cmd, *args

def add_contact(args, contacts):
    """
    Add a new contact to the contacts dictionary.

    Args:
        args (list): A list containing the name and 
        phone number of the contact.
        contacts (dict): The dictionary of contacts.

    Returns:
        str: A confirmation message.
    """
    name, phone = args
    contacts[name] = phone
    return "Contact added."

def change_contact(args, contacts):
    """
    Change the phone number of an existing contact.

    Args:
        args (list): A list containing the name and the new phone number.
        contacts (dict): The dictionary of contacts.

    Returns:
        str: A confirmation message or an error message
        if the contact doesn't exist.
    """
    name, new_phone = args
    if name not in contacts:
        return f"No name {name} in contact list"
    contacts[name] = new_phone
    return "Contact updated."

def show_phone(args, contacts):
    """
    Show the phone number of an existing contact.

    Args:
        args (list): A list containing the name of the contact.
        contacts (dict): The dictionary of contacts.

    Returns:
        str: The phone number of the contact or an error
        message if the contact doesn't exist.
    """
    name = args[0]
    if name not in contacts:
        return f"No name {name} in contact list"
    return contacts[name]

def show_all(contacts):
    """
    Display all contacts and their phone numbers.

    Args:
        contacts (dict): The dictionary of contacts.

    Returns:
        str: A formatted string containing all 
        contacts and their phone numbers.
    """
    contacts_str = ""
    for name, phone in contacts.items():
        contacts_str += f"{name}: {phone}\n"
    return contacts_str.rstrip()

def main():
    """
    Main function to run the contact management bot.
    """
    contacts = {}
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break
        if command == "hello":
            print("How can I help you?")
        elif command == "add":
            print(add_contact(args, contacts))
        elif command == "change":
            print(change_contact(args, contacts))
        elif command == "phone":
            print(show_phone(args, contacts))
        elif command == "all":
            print(show_all(contacts))
        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()
