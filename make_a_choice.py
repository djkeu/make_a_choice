from random import randint
import sys


def display_welcome_message():
    """Greet the user with a friendly welcome message."""
    message = (
        "\nHaving trouble making the right choice? "
        "Let this program help you by making that difficult decision for you."
    )
    print(message)


def _get_number_of_options():
    """Prompt user for the number of options to choose from (2 to 5)."""
    err = "Please pick a number between 2 and 5."

    while True:
        num_options = input(
            "How many options do you want to compare? (max 5): "
        )
        if num_options == 'q':
            _quit_program()
        try:
            num_options = int(num_options)

            if 1 < num_options <= 5:
                return num_options
            else:
                print(err)

        except ValueError:
            print(err)


def _get_user_options(num_options):
    """Make a list of the options presented by the user."""
    user_options = []
    i = 1
    
    while len(user_options) < num_options:
        if i == 1:
            option = input(f"Option {i} ('q' to quit): ")
        else:
            option = input(f"Option {i}: ")

        if option == 'q':
            _quit_program()
        
        if option == '':
            if len(user_options) < 2:
                print("Enter at least 2 options")
                continue
            else:
                break
        
        user_options.append(option)
        i += 1

    return user_options


def display_user_options(options_list):
    """Display the list of options presented by the user."""
    print("\nYou have chosen:")
    for item in options_list:
        print(f"{options_list.index(item) + 1} - {item}")


def get_random_index(options_list):
    """Create a random index to choose a random option."""
    i = randint(0, len(options_list) - 1)
    print(f"\nFinal verdict: {options_list[i]}")


def _quit_program():
    """Quit the program gracefully."""
    sys.exit("Later!")


def restart():
    """In case the user wants to try again."""
    prompt = input("Try again? (y/n) ")

    if prompt != 'y':
        _quit_program()


def main():
    """Main function to run the program."""
    while True:
        display_welcome_message()

        option_count = _get_number_of_options()
        chosen_options = _get_user_options(option_count)

        display_user_options(chosen_options)
        get_random_index(chosen_options)

        restart()


if __name__ == "__main__":
    main()
