from commands import add_contact, change_contact, show_phone, show_all
from input_parsing import parse_input

def main():
    contacts = {}
    print("Welcome to the assistant bot!")
    print("You can use some of these commands:\n add [name] [phone number] \n change [name] [new phone number] \n phone [name] \n all \n close or exit. \n Let's go!")
    while True:
        user_input = input("Enter a command: ")
        command, args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Goodbye!")
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
