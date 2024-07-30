# THIS CODE IS WRONG, FIX IT AND ADD NEW CODE
name = None
board_size = None
number_of_mines = None
name = input("Hello, whats your name")
if len(name) <= 2:
    print("Your name is too short")
    name = None
else:
    board_size = int(input(f"{name}, please choose board size"))
    if board_size > 0 and board_size <=26 and isinstance(board_size,int):
        number_of_mines = int(input(f"{name}, for board size {board_size}, choose number of mines to allocate"))
    else:
        print(f"{name}, you have entered illegal board size")
        board_size = None
        number_of_mines = None
    if board_size//2 >= number_of_mines and number_of_mines >0 and isinstance(board_size,int):
        print(f"{name}, the board size is: {board_size}, number of mines is: {number_of_mines}")
    else:
        print(f"{name}, you have entered illegal number of mines")
        number_of_mines = None
#2