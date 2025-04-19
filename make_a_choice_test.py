import make_a_choice


# display_welcome_message
def test_display_welcome_message(capsys):
    """Make sure the welcome message is printed correctly."""
    make_a_choice.display_welcome_message()
    captured = capsys.readouterr()
    assert (
        "Kun je weer niet kiezen? "
        "Laat dit programma die moeilijke keuze voor je maken."
    ) in captured.out


# get_number_of_options
def test_get_number_of_options_valid(monkeypatch):
    """Make sure the number of options can be between 2 and 5."""
    monkeypatch.setattr('builtins.input', lambda _: "2")
    assert make_a_choice.get_number_of_options() == 2

    monkeypatch.setattr('builtins.input', lambda _: "3")
    assert make_a_choice.get_number_of_options() == 3

    monkeypatch.setattr('builtins.input', lambda _: "4")
    assert make_a_choice.get_number_of_options() == 4

    monkeypatch.setattr('builtins.input', lambda _: "5")
    assert make_a_choice.get_number_of_options() == 5

def test_get_number_of_options_non_numerics(monkeypatch, capsys):
    inputs = iter(["abc", "u", "4"])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    result = make_a_choice.get_number_of_options()

    captured = capsys.readouterr()
    assert "Kies een getal tussen 2 en 5" in captured.out
    assert result == 4

def test_get_number_of_options_negative_numbers(monkeypatch, capsys):
    inputs = iter(["-5", "-1", "2"])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    result = make_a_choice.get_number_of_options()

    captured = capsys.readouterr()
    assert "Kies een getal tussen 2 en 5" in captured.out
    assert result == 2

def test_get_number_of_options_too_small_numbers(monkeypatch, capsys):
    inputs = iter(["0", "1", "3"])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    result = make_a_choice.get_number_of_options()

    captured = capsys.readouterr()
    assert "Kies een getal tussen 2 en 5" in captured.out
    assert result == 3

def test_get_number_of_options_too_large_numbers(monkeypatch, capsys):
    inputs = iter(["6", "10", "4"])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    result = make_a_choice.get_number_of_options()

    captured = capsys.readouterr()
    assert "Kies een getal tussen 2 en 5" in captured.out
    assert result == 4


# get_user_options
def test_get_user_options():
    ...


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
