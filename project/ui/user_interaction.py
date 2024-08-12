# # THIS CODE IS WRONG, FIX IT AND ADD NEW CODE
# name = None
# board_size = None
# number_of_mines = None
#
# name = input("Hello, whats your name")
# if len(name) <= 2:
#     print("Your name is too short")
#     name = None
# else:
#     board_size_input = input(f"{name}, please choose board size")
#     if board_size_input.isdigit() or (board_size_input.startswith('-') and board_size_input[1:].isdigit()):
#         board_size = int(board_size_input)
#         if board_size > 0 and board_size <= 26:
#             number_of_mines_input = input(f"{name}, for board size {board_size}, choose number of mines to allocate")
#             if number_of_mines_input.isdigit() or (number_of_mines_input.startswith('-') and number_of_mines_input[1:].isdigit()):
#                 number_of_mines = int(number_of_mines_input)
#                 if number_of_mines > 0 and number_of_mines <= (board_size* board_size // 2) and number_of_mines is not None:
#                     print(f"{name}, the board size is: {board_size}, number of mines is: {number_of_mines}")
#                 else:
#                     print(f"{name}, you have entered illegal number of mines")
#                     number_of_mines = None
#             else:
#                 print("Please enter a valid number of mines")
#                 number_of_mines = None
#         else:
#             print(f"{name}, you have entered illegal board size")
#             board_size = None
#     else:
#         print("Please enter a valid number for board size")
#         board_size = None

def is_name_valid(name):
    return len(name) > 2

def is_board_size_valid(board_size):
    return board_size > 0 and board_size <= 26

def is_number_of_mines_valid(board_size, number_of_mines):
    return number_of_mines > 0 and number_of_mines <= (board_size * board_size // 2)

def register_user():
    name = input("Hello, whats your name")
    if not is_name_valid(name):
        print("Your name is too short")
        return None, None, None

    board_size_input = input(f"{name}, please choose board size")
    if board_size_input.isdigit() or (board_size_input.startswith('-') and board_size_input[1:].isdigit()):
        board_size = int(board_size_input)
        if is_board_size_valid(board_size):
            number_of_mines_input = input(f"{name}, for board size {board_size}, choose number of mines to allocate")
            if number_of_mines_input.isdigit() or (number_of_mines_input.startswith('-') and number_of_mines_input[1:].isdigit()):
                number_of_mines = int(number_of_mines_input)
                if is_number_of_mines_valid(board_size, number_of_mines):
                    print(f"{name}, the board size is: {board_size}, number of mines is: {number_of_mines}")
                    return name, board_size, number_of_mines
                else:
                    print(f"{name}, you have entered illegal number of mines")
                    return None, None, None
            else:
                print("Please enter a valid number of mines")
                return None, None, None
        else:
            print(f"{name}, you have entered illegal board size")
            return None, None, None
    else:
        print("Please enter a valid number for board size")
        return None, None, None