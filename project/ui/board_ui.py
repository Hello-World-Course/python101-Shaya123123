def parse_cmd(command):
    command_parts = command.split(" ")
    command_name = command_parts[0]
    if len(command_parts) > 1:
        parameters = [int(digit) for part in command_parts[1:] for digit in part if digit.isdigit()]
    else:
        parameters = []
    return [command_name, parameters]