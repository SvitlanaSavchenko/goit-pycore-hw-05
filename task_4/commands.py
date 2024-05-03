from error_handling import input_error

@input_error
def add_contact(args, contacts):
    name, phone = args
    contacts[name] = phone
    return "Contact added."

@input_error
def change_contact(args, contacts):
    name, phone = args
    if name in contacts:
        contacts[name] = phone
        return "Contact updated."
    else:
        return "Contact not found."

@input_error
def show_phone(args, contacts):
    name = args[0]
    if name in contacts:
        return contacts[name]
    else:
        return "Contact not found."

@input_error
def show_all(contacts):
    if contacts:
        result = ""
        for name, phone in contacts.items():
            result += f"{name}: {phone}\n"
        return result
    else:
        return "No contacts available."
