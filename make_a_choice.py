from random import randint
import sys


def display_welcome_message():
    """Greet the user with a friendly welcome message."""
    message = (
        "\nKun je weer niet kiezen? "
        "Laat dit programma die moeilijke keuze voor je maken."
    )
    print(message)


def get_number_of_options():
    """Prompt user for the number of options to choose from."""
    err = "Kies een getal tussen 2 en 5."

    while True:
        try:
            num_options = int(input(
                "Hoeveel opties wil je vergelijken? (max 5): "
            ))

            if 1 < num_options <= 5:
                return num_options
            else:
                print(err)

        except ValueError:
            print(err)


def get_user_options(num_options):
    """Make a list of the options presented by the user."""
    user_options = []

    i = 1
    while len(user_options) < num_options:
        if i == 1:
            option = input(f"Optie {i} ('s' om te stoppen): ")
        else:
            option = input(f"Optie {i}: ")

        if option == 's':
            quit_program()
        elif option == '' and len(user_options) > 1:
            break
        elif option == '':
            print("Noem minstens twee opties")
            continue

        user_options.append(option)
        i += 1

    return user_options


def display_user_options(options_list):
    """Display a list of the options presented by the user."""
    print("\nDe door u gekozen opties zijn:")
    for item in options_list:
        print(f"{options_list.index(item) + 1} - {item}")


def determine_choice(options_list):
    """Present the user with the final choice."""
    throw = randint(2, 12)
    i = round((throw / 12) * (len(options_list) - 1))

    print(f"\nHet wordt: {options_list[i]}")


def quit_program():
    """Quit the program gracefully."""
    sys.exit("Laters!")


def restart():
    """In case the user wants to try again."""
    prompt = input("Nog een keer proberen? (j/n) ")

    if prompt == 'j':
        main()
    else:
        quit_program()


def main():
    """Main function to run the program."""
    display_welcome_message()

    num_options = get_number_of_options()
    user_options = get_user_options(num_options)

    display_user_options(user_options)
    determine_choice(user_options)
    restart()


if __name__ == "__main__":
    main()
