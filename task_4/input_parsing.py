def parse_input(user_input):
    tokens = user_input.strip().split(maxsplit=2)
    command = tokens[0].lower()
    args = tokens[1:] if len(tokens) > 1 else []
    return command, args
