### ---------------------------------------------------- ###
### Course: CSE210
### Assignment: W02 Prove: Developer - Tic Tac Toe Game
### Author: Eric Farley
### ---------------------------------------------------- ###


import sys

# All available turns in the game.
USER_TURNS = ['x', 'o', 'x', 'o', 'x', 'o', 'x', 'o', 'x']

VALID_INPUTS = [1, 2, 3, 4, 5, 6, 7, 8, 9]

POSSIBLE_WINS = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [1, 4, 7], [2, 5, 8], [3, 6, 9], [1, 5, 9], [3, 5, 7]]

# Initially, all the squares are empty.
taken_squares = [1, 2, 3, 4, 5, 6, 7, 8, 9]


def print_grid(values: list):
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
    user_squares = []
    for i, square in enumerate(taken_squares, 1):
        if square == user:
            user_squares.append(i)
    
    for wins in POSSIBLE_WINS:
        # First iterate through the possible win spots and assign them in 'item'
        # Then find out if they exist in the options the user selected already inside 'user_squares'
        if all(item in user_squares for item in wins):
            print(f'"{user}" won the game. Congrats!')
            return True

    if not any(item in taken_squares for item in VALID_INPUTS):
        print('Game ended in a draw. Well played!')

def is_option_available(option: int) -> bool:
    return True if option in taken_squares else False


def handle_user_input(user: str) -> int:
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
