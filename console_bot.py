def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args


def add_contact(args, contacts):
    name, phone = args
    contacts[name] = phone
    return "Contact added."


def change_contact(args, contacts):
    name, phone = args
    if name not in contacts:
        return f"No name {name} in contact list"

    contacts[name] = phone
    return "Contact updated."


def show_phone(args, contacts):
    name = args[0]
    if name not in contacts:
        return f"No name {name} in contact list"
    return contacts[name]


def show_all(contacts):
    contacts_str = ""
    for name, phone in contacts.items():
        contacts_str += f"{name}: {phone}\n"
    return contacts_str.rstrip()


def main():
    contacts = {}
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break
        elif command == "hello":
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


# TODO сделать обработку ошибок если после команды не было введено аргументов
# TODO сделать загрузку контактов из файла
# TODO при запуске программы и сохранение при выходе
# TODO протестировать и добавить обработку других возможных ошибок
