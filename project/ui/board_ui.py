def parse_cmd(command):
    command_parts = command.split(" ")
    command_name = command_parts[0]
    parameters = " ".join(command_parts[1:])
    return command_name, parameters
