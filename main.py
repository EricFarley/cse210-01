### ---------------------------------------------------- ###
### Course: CSE210
### Assignment: W02 Prove: Developer - Tic Tac Toe Game
### Author: Eric Farley
### ---------------------------------------------------- ###


import sys

USER_TURNS = ['x', 'o', 'x', 'o', 'x', 'o', 'x', 'o', 'x']
""" All available turns in the game. """

VALID_INPUTS = [1, 2, 3, 4, 5, 6, 7, 8, 9]

POSSIBLE_WINS = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [1, 4, 7], [2, 5, 8], [3, 6, 9], [1, 5, 9], [3, 5, 7]]

taken_squares = [1, 2, 3, 4, 5, 6, 7, 8, 9]
""" Initially, all the squares are empty. """


def print_grid(values: list):
    """
    Prints the grid with the values in it.
    """
    print()
    print(f'{values[0]} | {values[1]} | {values[2]}')
    print('--+---+--')
    print(f'{values[3]} | {values[4]} | {values[5]}')
    print('--+---+--')
    print(f'{values[6]} | {values[7]} | {values[8]}')
    print()


def set_choice(option: int, user: str):
    for i, square in enumerate(taken_squares):
        if option == square:
            taken_squares[i] = user


def is_game_over(user: str):
    """
    Checks if the game should end, based on the possible winning options.\n
    If none of the options are met, the game ends in a draw.
    """
    user_squares = []
    for i, square in enumerate(taken_squares, 1):
        if square == user:
            user_squares.append(i)
    
    for wins in POSSIBLE_WINS:
        # First iterate through the possible win spots and assign them in 'item' variable
        # Then, find out if ALL of the options the user selected are inside the winning options.
        if all(item in user_squares for item in wins):
            print(f'"{user}" won the game. Congrats!')
            return True

    if not any(item in taken_squares for item in VALID_INPUTS):
        print('Game ended in a draw. Well played!')


def is_option_available(option: int) -> bool:
    """
    Checks if option the user entered is still available.
    Return: Boolean
    """
    return True if option in taken_squares else False


def handle_user_input(user: str) -> int:
    """
    Handles user interaction with the game.\n
    Makes sure that the input is valid, according to the rules.\n
    Return: the number selected by the user.
    """
    user_input_validated: bool = False
    while user_input_validated == False:
        try:
            user_input = input(f'{user}\'s turn to choose a square(1-9): ')

            if not user_input.isdigit() or int(user_input) not in VALID_INPUTS:
                # Throw invalid input error.
                raise ValueError(
                    f'Invalid input "{user_input}". Only numbers between 1 and 9 are allowed.')

            # Because we know this is an int, convert it.
            user_input = int(user_input)

            if user_input in VALID_INPUTS:
                # Validate that the option is not already taken
                if not is_option_available(user_input):
                    raise ValueError(f'Option "{user_input}" already taken.')

                user_input_validated = True
                return user_input

        except ValueError as value_error:
            print(value_error)

        # If an unexpected error occurred, print it.
        except Exception as exception:
            print(exception)


def main():
    try:
        for user in USER_TURNS:
            user_option = handle_user_input(user)
            set_choice(user_option, user)    
            print_grid(taken_squares)
            if is_game_over(user):
                break    
    except KeyboardInterrupt:
        print()
        print('Program interrupted. Try again.')
        sys.exit(0)

if __name__ == '__main__':
    main()
