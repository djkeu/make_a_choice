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


def test_get_user_options_two_of_three(monkeypatch):
    """Verify function stops when 2 of 3 inputs exist."""
    inputs = iter(
        ["Aap", "Noot", ""]
    )
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    result = make_a_choice.get_user_options(3)
    assert result == ["Aap", "Noot"]


def test_get_user_options_two_of_five(monkeypatch):
    """Verify function stops after empty input when 2 of 5 options exist."""
    inputs = iter(
        ["Aap", "", "Mies", ""]
    )
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    result = make_a_choice.get_user_options(5)
    assert result == ["Aap", "Mies"]


def test_get_user_options_three_of_five(monkeypatch):
    """Verify function stops after empty input when 3 of 5 options exist."""
    inputs = iter(
        ["", "Aap", "", "", "Noot", "Mies", ""]
    )
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    result = make_a_choice.get_user_options(5)
    assert result == ["Aap", "Noot", "Mies"]


def test_get_user_options_early_quit_first_input(monkeypatch, capsys):
    """Verify program stops when first input is 's'."""
    monkeypatch.setattr('builtins.input', lambda _: "s")

    with pytest.raises(SystemExit):
        make_a_choice.get_user_options(5)

    # Note: no assertion! that's done in test_quit_program()


def test_get_user_options_early_quit_third_input(monkeypatch, capsys):
    """Verify program stops when third input is 's'."""
    inputs = iter(
        ["Aap", "Noot", "s"]
    )
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    with pytest.raises(SystemExit):
        make_a_choice.get_user_options(5)


def test_get_user_options_early_quit_fifth_input(monkeypatch, capsys):
    """Verify program stops when fifth input is 's'."""
    inputs = iter(
        ["Aap", "", "Noot", "Mies", "Wim", "s"]
    )
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    with pytest.raises(SystemExit):
        make_a_choice.get_user_options(5)


# tests for display_user_options
def test_display_user_options_strings(capsys):
    """Verify a list of strings is displayed correctly."""
    options = ["Aap", "Noot", "Mies"]
    make_a_choice.display_user_options(options)

    captured = capsys.readouterr()
    assert "De door u" in captured.out
    assert "1 - Aap" in captured.out
    assert "3 - Mies" in captured.out


def test_display_user_options_numbers(capsys):
    """Verify a list of numbers is displayed correctly."""
    options = [10, 20, 30]
    make_a_choice.display_user_options(options)

    captured = capsys.readouterr()
    assert "\nDe door u gekozen opties zijn:" in captured.out
    assert "1 - 10" in captured.out
    assert "3 - 30" in captured.out


def test_display_user_options_mixed(capsys):
    """Verify a list of strings and numbers is displayed correctly."""
    options = ["Aap", 20, "Mies", 40, "Zus"]
    make_a_choice.display_user_options(options)

    captured = capsys.readouterr()
    assert "\nDe door u gekozen opties zijn:" in captured.out
    assert "1 - Aap" in captured.out
    assert "2 - 20" in captured.out
    assert "3 - Mies" in captured.out
    assert "4 - 40" in captured.out
    assert "5 - Zus" in captured.out


# tests for throw_dice
def test_throw_dice_heading(capsys):
    """Verify heading is displayed."""
    options = ["Aap", "Noot"]
    make_a_choice.throw_dice(options)

    captured = capsys.readouterr()
    assert "\nHet wordt: " in captured.out


def test_throw_dice_two_strings(capsys):
    """Verify one random option of two strings is displayed."""
    options = ["Aap", "Noot"]
    make_a_choice.throw_dice(options)

    captured = capsys.readouterr()
    assert (
        options[0] in captured.out or
        options[1] in captured.out    
    )
    assert not (
        options[0] in captured.out and
        options[1] in captured.out    
    )
    assert (
        "Aap" in captured.out or
        "Noot" in captured.out
    )
    assert not (
        "Aap" in captured.out and
        "Noot" in captured.out
    )

    # FixMe: use itertools?

    # FixMe:
    # result = make_a_choice.throw_dice(options)
    # print(result)  # "\nHet wordt: Aap"
    # FixMe:
    # assert len(result) == 1

    # FixMe:
    # assert sum(options[0] in captured.out, options[1] in captured.out) == 1

    # FixMe: use sum(conditions) == 1 to check only one condition is true


"""
ToDo: tests throw_dice
    - ToDo: "\nHet wordt: "
    - ToDo: list[0] or list[1] or list[x]
"""


# Functions to test in make_a_choice.py:
"""
- display_welcome_message
- get_number_of_options
- get_user_options
- display_user_options
- ToDo: throw_dice
- ToDo: quit_program
- ToDo: restart
- ToDo: main
"""
