import pytest
import make_a_choice as mc


# tests for display_welcome_message()
def test_display_welcome_message(capsys):
    """Verify the welcome message is printed correctly."""
    mc.display_welcome_message()
    captured = capsys.readouterr()
    assert (
        "Having trouble making the right choice? "
        "Let this program help you by making that dificult decision for you."
    ) in captured.out


# tests for get_number_of_options()
def test_get_number_of_options_valid(monkeypatch):
    """Verify the number of options can be between 2 and 5."""
    monkeypatch.setattr('builtins.input', lambda _: "2")
    assert mc._get_number_of_options() == 2

    monkeypatch.setattr('builtins.input', lambda _: "5")
    assert mc._get_number_of_options() == 5


def test_get_number_of_options_early_exit(monkeypatch):
    """Verify the program exits after input of 's'."""
    monkeypatch.setattr('builtins.input', lambda _: 's')

    with pytest.raises(SystemExit):
        mc._get_number_of_options()


def test_get_number_of_options_non_numerics(monkeypatch, capsys):
    """Verify only numbers are accepted as input."""
    inputs = iter(["abc", "u", "4"])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    result = mc._get_number_of_options()

    captured = capsys.readouterr()
    assert "Kies een getal tussen 2 en 5" in captured.out
    assert result == 4


def test_get_number_of_options_negative_numbers(monkeypatch, capsys):
    """Verify negative numbers are rejected as input."""
    inputs = iter(["-5", "-1", "2"])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    result = mc._get_number_of_options()

    captured = capsys.readouterr()
    assert "Kies een getal tussen 2 en 5" in captured.out
    assert result == 2


def test_get_number_of_options_too_small_numbers(monkeypatch, capsys):
    """Verify numbers smaller than 2 are rejected."""
    inputs = iter(["0", "1", "3"])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    result = mc._get_number_of_options()

    captured = capsys.readouterr()
    assert "Kies een getal tussen 2 en 5" in captured.out
    assert result == 3


def test_get_number_of_options_too_large_numbers(monkeypatch, capsys):
    """Verify numbers larger than 5 are rejected."""
    inputs = iter(["6", "10", "4"])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    result = mc._get_number_of_options()

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
    result = mc._get_user_options(2)
    assert result == ["Aap", "Noot"]


def test_get_user_options_four_numbers(monkeypatch):
    """Verify four numbers are collected and returned as a list of numbers."""
    inputs = iter(
        [1, 22, 3, 4]
    )
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    result = mc._get_user_options(4)
    assert result == [1, 22, 3, 4]


def test_get_user_options_strings_and_numbers(monkeypatch):
    """Verify numbers and strings are collected and returned as a list."""
    inputs = iter(
        [1, "noot", "mies", 44, "zus"]
    )
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    result = mc._get_user_options(5)
    assert result == [1, "noot", "mies", 44, "zus"]


def test_get_user_options_empty_first(monkeypatch, capsys):
    """Verify empty first input gets rejected."""
    inputs = iter(
        ["", "s"]
    )
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    with pytest.raises(SystemExit):
        mc._get_user_options(5)

    captured = capsys.readouterr()
    assert "Noem minstens " in captured.out


def test_get_user_options_empty_first_valid_later(monkeypatch, capsys):
    """Verify empty inputs are rejected."""
    inputs = iter(
        ["", "", "Aap", "Noot"]
    )
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    result = mc._get_user_options(2)
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
        mc._get_user_options(5)

    captured = capsys.readouterr()
    assert "Noem minstens twee opties" in captured.out


def test_get_user_options_empty_second_valid_later(monkeypatch, capsys):
    """Verify empty inputs get rejected."""
    inputs = iter(
        ["Aap", "", "", "Noot", "Mies"]
    )
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    result = mc._get_user_options(3)
    captured = capsys.readouterr()

    assert result == ["Aap", "Noot", "Mies"]
    assert "Noem minstens" in captured.out


def test_get_user_options_two_of_three(monkeypatch):
    """Verify function stops when 2 of 3 inputs exist."""
    inputs = iter(
        ["Aap", "Noot", ""]
    )
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    result = mc._get_user_options(3)
    assert result == ["Aap", "Noot"]


def test_get_user_options_two_of_five(monkeypatch):
    """Verify function stops after empty input when 2 of 5 options exist."""
    inputs = iter(
        ["Aap", "", "Mies", ""]
    )
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    result = mc._get_user_options(5)
    assert result == ["Aap", "Mies"]


def test_get_user_options_three_of_five(monkeypatch):
    """Verify function stops after empty input when 3 of 5 options exist."""
    inputs = iter(
        ["", "Aap", "", "", "Noot", "Mies", ""]
    )
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    result = mc._get_user_options(5)
    assert result == ["Aap", "Noot", "Mies"]


def test_get_user_options_early_quit_first_input(monkeypatch):
    """Verify program stops when first input is 's'."""
    monkeypatch.setattr('builtins.input', lambda _: "s")

    with pytest.raises(SystemExit) as e:
        mc._get_user_options(5)

    assert "Laters" in str(e.value)


def test_get_user_options_early_quit_third_input(monkeypatch):
    """Verify program stops when third input is 's'."""
    inputs = iter(
        ["Aap", "Noot", "s"]
    )
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    with pytest.raises(SystemExit):
        mc._get_user_options(5)


def test_get_user_options_early_quit_fifth_input(monkeypatch):
    """Verify program stops when fifth input is 's'."""
    inputs = iter(
        ["Aap", "", "Noot", "Mies", "Wim", "s"]
    )
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    with pytest.raises(SystemExit):
        mc._get_user_options(5)


# tests for display_user_options()
def test_display_user_options_strings(capsys):
    """Verify a list of strings is displayed correctly."""
    options = ["Aap", "Noot", "Mies"]
    mc.display_user_options(options)

    captured = capsys.readouterr()
    assert "De door u" in captured.out
    assert "1 - Aap" in captured.out
    assert "3 - Mies" in captured.out


def test_display_user_options_numbers(capsys):
    """Verify a list of numbers is displayed correctly."""
    options = [10, 20, 30]
    mc.display_user_options(options)

    captured = capsys.readouterr()
    assert "\nDe door u gekozen opties zijn:" in captured.out
    assert "1 - 10" in captured.out
    assert "3 - 30" in captured.out


def test_display_user_options_strings_and_numbers(capsys):
    """Verify a list of strings and numbers is displayed correctly."""
    options = ["Aap", 20, "Mies", 40, "Zus"]
    mc.display_user_options(options)

    captured = capsys.readouterr()
    assert "\nDe door u gekozen opties zijn:" in captured.out
    assert "1 - Aap" in captured.out
    assert "2 - 20" in captured.out
    assert "3 - Mies" in captured.out
    assert "4 - 40" in captured.out
    assert "5 - Zus" in captured.out


# tests for throw_dice()
def test_throw_dice_leading_text(capsys):
    """Verify leading text is displayed."""
    options = ["Aap", 2, "Mies"]
    mc.throw_dice(options)

    captured = capsys.readouterr()
    assert "\nHet wordt: " in captured.out


def test_throw_dice_options_strings_and_numbers(capsys):
    """Verify one random option of 5 options is displayed."""
    options = ["Aap", 2, "Mies", 44, "Zus"]
    mc.throw_dice(options)

    captured = capsys.readouterr()

    counter = 0
    for option in options:
        if str(option) in captured.out:
            counter += 1
    assert counter == 1


# tests for quit_program()
def test_quit_program():
    """Verify the program exits with a friendly message."""
    with pytest.raises(SystemExit) as e:
        mc._quit_program()

    assert "Laters!" in str(e.value)


# tests for restart()
def test_restart_yes(monkeypatch, capsys):
    """Verify the program is restarted after input of 'j'."""
    inputs = iter(
        ['j', 's']
    )
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    with pytest.raises(SystemExit):
        mc.restart()

    captured = capsys.readouterr()
    assert "Having trouble making the right choice?" in captured.out


def test_no_restart_char(monkeypatch):
    """Verify the program exits after input is a char not 'j'."""
    monkeypatch.setattr('builtins.input', lambda _: 'x')
    with pytest.raises(SystemExit):
        mc.restart()

    monkeypatch.setattr('builtins.input', lambda _: 'n')
    with pytest.raises(SystemExit):
        mc.restart()


def test_no_restart_string(monkeypatch):
    """Verify the program exits after input of string."""
    monkeypatch.setattr('builtins.input', lambda _: 'nee')
    with pytest.raises(SystemExit):
        mc.restart()


def test_no_restart_number(monkeypatch):
    """Verify the program exits after input of number."""
    monkeypatch.setattr('builtins.input', lambda _: 3)
    with pytest.raises(SystemExit):
        mc.restart()


# tests for main()
def test_main_happy_path(capsys, monkeypatch):
    """Verify main() runs the full workflow with expected output."""
    inputs = iter(
        ["2", "Aap", "Noot", "n"]
    )
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    with pytest.raises(SystemExit):
        mc.main()

    captured = capsys.readouterr()
    output = captured.out

    assert "Having trouble" in output
    assert "1 - " in output and "2 - " in output
    assert "Het wordt: " in output


def test_main_early_exit(monkeypatch):
    """Verify main() exits when 's' is entered."""
    monkeypatch.setattr('builtins.input', lambda _: "s")
    with pytest.raises(SystemExit) as e:
        mc.main()
    assert "Laters!" in str(e.value)
