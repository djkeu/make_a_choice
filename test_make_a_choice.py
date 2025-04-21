import pytest
import make_a_choice


# tests for display_welcome_message()
def test_display_welcome_message(capsys):
    """Verify the welcome message is printed correctly."""
    make_a_choice.display_welcome_message()
    captured = capsys.readouterr()
    assert (
        "Kun je weer niet kiezen? "
        "Laat dit programma die moeilijke keuze voor je maken."
    ) in captured.out


# tests for get_number_of_options()
def test_get_number_of_options_valid(monkeypatch):
    """Verify the number of options can be between 2 and 5."""
    monkeypatch.setattr('builtins.input', lambda _: "2")
    assert make_a_choice.get_number_of_options() == 2

    monkeypatch.setattr('builtins.input', lambda _: "3")
    assert make_a_choice.get_number_of_options() == 3

    monkeypatch.setattr('builtins.input', lambda _: "4")
    assert make_a_choice.get_number_of_options() == 4

    monkeypatch.setattr('builtins.input', lambda _: "5")
    assert make_a_choice.get_number_of_options() == 5


def test_get_number_of_options_non_numerics(monkeypatch, capsys):
    """Verify only numbers are accepted as input."""
    inputs = iter(["abc", "u", "4"])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    result = make_a_choice.get_number_of_options()

    captured = capsys.readouterr()
    assert "Kies een getal tussen 2 en 5" in captured.out
    assert result == 4


def test_get_number_of_options_negative_numbers(monkeypatch, capsys):
    """Verify negative numbers are rejected as input."""
    inputs = iter(["-5", "-1", "2"])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    result = make_a_choice.get_number_of_options()

    captured = capsys.readouterr()
    assert "Kies een getal tussen 2 en 5" in captured.out
    assert result == 2


def test_get_number_of_options_too_small_numbers(monkeypatch, capsys):
    """Verify numbers smaller than 2 are rejected."""
    inputs = iter(["0", "1", "3"])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    result = make_a_choice.get_number_of_options()

    captured = capsys.readouterr()
    assert "Kies een getal tussen 2 en 5" in captured.out
    assert result == 3


def test_get_number_of_options_too_large_numbers(monkeypatch, capsys):
    """Verify numbers larger than 5 are rejected."""
    inputs = iter(["6", "10", "4"])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    result = make_a_choice.get_number_of_options()

    captured = capsys.readouterr()
    assert "Kies een getal tussen 2 en 5" in captured.out
    assert result == 4


# tests for get_user_options()
def test_get_user_options_two_strings(monkeypatch):
    """Verify two strings are collected and returned as a list of strings."""
    inputs = iter(
        ["Aap", "Noot"]
    )
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    result = make_a_choice.get_user_options(2)
    assert result == ["Aap", "Noot"]


def test_get_user_options_four_numbers(monkeypatch):
    """Verify four numbers are collected and returned as a list of numbers."""
    inputs = iter(
        [1, 2, 3, 4]
    )
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    result = make_a_choice.get_user_options(4)
    assert result == [1, 2, 3, 4]


def test_get_user_options_strings_and_numbers(monkeypatch):
    """Verify numbers and strings are collected and returned as a list."""
    inputs = iter(
        [1, "noot", "mies", 4, "zus"]
    )
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    result = make_a_choice.get_user_options(5)
    assert result == [1, "noot", "mies", 4, "zus"]


def test_get_user_options_empty_first(monkeypatch, capsys):
    """Verify empty first input gets rejected."""
    inputs = iter(
        ["", "s"]
    )
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    with pytest.raises(SystemExit):
        make_a_choice.get_user_options(5)

    captured = capsys.readouterr()
    assert "Noem minstens " in captured.out


def test_get_user_options_empty_first_valid_later(monkeypatch, capsys):
    """Verify empty inputs are rejected."""
    inputs = iter(
        ["", "", "Aap", "Noot"]
    )
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    result = make_a_choice.get_user_options(2)
    captured = capsys.readouterr()

    assert "Noem minstens twee opties" in captured.out
    assert result == ["Aap", "Noot"]


def test_get_user_options_empty_second(monkeypatch, capsys):
    """Verify empty second input gets rejected."""
    inputs = iter(
        ["4", "", "s"]
    )
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    with pytest.raises(SystemExit):
        make_a_choice.get_user_options(5)

    captured = capsys.readouterr()
    assert "Noem minstens twee opties" in captured.out


def test_get_user_options_empty_second_valid_later(monkeypatch, capsys):
    """Verify empty inputs get rejected."""
    inputs = iter(
        ["Aap", "", "", "Noot", "Mies"]
    )
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    result = make_a_choice.get_user_options(3)
    captured = capsys.readouterr()

    assert result == ["Aap", "Noot", "Mies"]
    assert "Noem minstens" in captured.out


def test_get_user_options_two_of_three(monkeypatch, capsys):
    """Verify fewer inputs are accepted."""
    inputs = iter(
        ["Aap", "Noot", ""]
    )
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    result = make_a_choice.get_user_options(3)
    assert result == ["Aap", "Noot"]


"""
ToDo: tests get_user_options
    - Done: valid number of options
    - Done: first empty option
    - Done: second empty option
    - ToDo: less than entered options (2 of 3, 2 of 5, 3 of 5)
    - ToDo: early quit (option: 's')
    - Abandoned: too many options given: not possible
"""


# Functions make_a_choice.py:
"""
- display_welcome_message
- get_number_of_options
- ToDo: test_get_user_options
- ToDo: test_display_user_options
- ToDo: test_determine_choice
- ToDo: test_quit_program
- ToDo: test_restart
- ToDo: test_main
"""
