# Course: CSE210
# Assignment: Tic Tac Toe Game - Week 2
# Author: Eric Farley


VALID_INPUTS = [1, 2, 3, 4, 5, 6, 7, 8, 9]


def set_choices():
    pass


def check_game_status():
    pass


def validate_availability(option: int) -> bool:
    return True


def handle_user_input(user: str):
    try:
        user_input = int(input(f'{user}\'s turn to choose a square(1-9): '))

        if not user_input.isdigit():
            # Throw invalid input error.
            return False

        if user_input in VALID_INPUTS:
            # Validate that the option is not already taken
            validate_availability(user_input)
            return user_input
    except ValueError as error:
        print(error)


def main():
    pass


main()
