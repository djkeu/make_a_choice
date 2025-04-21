# Make A Choice


## Description
Python program to help decide between various options presented by the user.\
Also serves as an exercise in writing pytest tests.


## ToDo Section
- ToDo: readme.md
- ToDo: translate prompts and prints into English

- ToDo: explanatory docstrings (explain why, not what)
    - Done: make_a_choice.py
    - ToDo: test_make_a_choice.py
        - Done: test_display_welcome_message
        - Done: test_get_number_of_options
        - Done: test_get_user_options
        - Done: test_display_user_options

        - ToDo: test_throw_dice
        - ToDo: test_quit_program
        - ToDo: test_restart
        - ToDo: test_main


## Pytest
test_make_a_choice.py:

```
$ pytest --lf --collect-only -q

test_make_a_choice.py::test_display_welcome_message

test_make_a_choice.py::test_get_number_of_options_valid
test_make_a_choice.py::test_get_number_of_options_non_numerics
test_make_a_choice.py::test_get_number_of_options_negative_numbers
test_make_a_choice.py::test_get_number_of_options_too_small_numbers
test_make_a_choice.py::test_get_number_of_options_too_large_numbers

test_make_a_choice.py::test_get_user_options_two_strings
test_make_a_choice.py::test_get_user_options_four_numbers
test_make_a_choice.py::test_get_user_options_strings_and_numbers

test_make_a_choice.py::test_get_user_options_empty_first
test_make_a_choice.py::test_get_user_options_empty_first_valid_later
test_make_a_choice.py::test_get_user_options_empty_second
test_make_a_choice.py::test_get_user_options_empty_second_valid_later

test_make_a_choice.py::test_get_user_options_two_of_three
test_make_a_choice.py::test_get_user_options_two_of_five
test_make_a_choice.py::test_get_user_options_three_of_five

test_make_a_choice.py::test_get_user_options_early_quit_first_input
test_make_a_choice.py::test_get_user_options_early_quit_third_input
test_make_a_choice.py::test_get_user_options_early_quit_fifth_input

test_make_a_choice.py::test_display_user_options_strings
test_make_a_choice.py::test_display_user_options_numbers
test_make_a_choice.py::test_display_user_options_mixed
```


## Make a choice
make_a_choice.py:

- ToDo: restart():
    - ToDo: get messages from text file
