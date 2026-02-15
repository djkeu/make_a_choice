from random import randint
import sys


def display_welcome_message():
    """Greet the user with a friendly welcome message."""
    message = (
        "\nHaving trouble making the right choice? "
        "Let this program help you by making that dificult decision for you."
    )
    print(message)


def _get_number_of_options():
    """Prompt user for the number of options to choose from (2 to 5)."""
    err = "Please pick a number between 2 and 5."

    while True:
        num_options = input(
            "How many options do you want to compare? (max 5): "
        )
        if num_options == 's':
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
        elif option == '' and len(user_options) > 1:
            break
        elif option == '':
            print("Enter at least 2 options")
            continue

        user_options.append(option)
        i += 1

    return user_options


def display_user_options(options_list):
    """Display the list of options presented by the user."""
    print("\nDe door u gekozen opties zijn:")
    for item in options_list:
        print(f"{options_list.index(item) + 1} - {item}")


def throw_dice(options_list):
    """Throw 2 six-sided dices to determine the final choice."""
    throw = randint(2, 12)
    i = round((throw / 12) * (len(options_list) - 1))

    print(f"\nFinal verdict: {options_list[i]}")


def _quit_program():
    """Quit the program gracefully."""
    sys.exit("Laters!")


def restart():
    """In case the user wants to try again."""
    prompt = input("Nog een keer proberen? (j/n) ")

    if prompt == 'j':
        main()
    else:
        _quit_program()


def main():
    """Main function to run the program."""
    display_welcome_message()

    num_options = _get_number_of_options()
    user_options = _get_user_options(num_options)

    display_user_options(user_options)
    throw_dice(user_options)
    restart()


if __name__ == "__main__":
    main()
