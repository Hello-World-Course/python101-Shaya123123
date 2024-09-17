def parse_cmd(command):
    command_parts = command.split(" ")
    command_name = command_parts[0]
    if len(command_parts) > 1:
        parameters = " ".join(command_parts[1:])
    else:
        parameters = None
    return command_name, parameters