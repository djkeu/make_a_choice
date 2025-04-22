# Make A Choice


## Description
Originally intended as a small Python program to help decide between various options. Gradually became more of an exercise in testing with Pytest.


## ToDo Section
- Abandoned: translate prompts and prints into English
- Abandoned: restart(): get messages from text file


## Pytest
Pytest test file: test_make_a_choice.py


### All tests
```
$ pytest --collect-only -q

test_make_a_choice.py::test_display_welcome_message

test_make_a_choice.py::test_get_number_of_options_valid
test_make_a_choice.py::test_get_number_of_options_early_exit
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
test_make_a_choice.py::test_display_user_options_strings_and_numbers

test_make_a_choice.py::test_throw_dice_lead
test_make_a_choice.py::test_throw_dice_options_strings_and_numbers

test_make_a_choice.py::test_quit_program

test_make_a_choice.py::test_restart_yes
test_make_a_choice.py::test_no_restart_char
test_make_a_choice.py::test_no_restart_string
test_make_a_choice.py::test_no_restart_number

test_make_a_choice.py::test_main_happy_path
test_make_a_choice.py::test_main_early_exit

32 tests collected in 0.01s

```
