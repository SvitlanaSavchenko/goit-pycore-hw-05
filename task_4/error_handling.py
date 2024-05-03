def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except KeyError:
            return "Contact not found."
        except ValueError:
            return "Invalid input format. Please provide name and phone number."
        except IndexError:
            return "Insufficient arguments. Please provide both name and phone number."

    return inner
