# THIS CODE IS WRONG, FIX IT AND ADD NEW CODE
name = None
board_size = None
number_of_mines = None

name = input("Hello, whats your name")
if len(name) <= 2:
    print("Your name is too short")
    name = None
else:
    board_size_input = input(f"{name}, please choose board size")
    if board_size_input.isdigit():
        board_size = int(board_size_input)
        if board_size > 0 and board_size <= 26:
            number_of_mines_input = input(f"{name}, for board size {board_size}, choose number of mines to allocate")
            if number_of_mines_input.isdigit():
                number_of_mines = int(number_of_mines_input)
                if number_of_mines > 0 and number_of_mines <= (board_size // 2):
                    print(f"{name}, the board size is: {board_size}, number of mines is: {number_of_mines}")
                else:
                    print(f"{name}, you have entered illegal number of mines")
            else:
                print("Please enter a valid number of mines")
        else:
            print(f"{name}, you have entered illegal board size")
    else:
        print("Please enter a valid number for board size")
#