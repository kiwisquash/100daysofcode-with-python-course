# Importing unittest.mock to mock the random module 
from unittest.mock import patch
import random
from guess import get_random_number, Game
import pytest

@patch.object(random, 'randint') #random.randint is being mocked here
def test_get_random_number(m):
    m.return_value = 17 # random.randint will return 17
    assert get_random_number() == 17

# The guess method in the Game class requires a user input.
# patch can be used to define a sequence of fake user inputs

@patch("builtins.input", side_effect=[11,'12','Bpb',12,5,-1,21,7,None])
def test_guess(inp):
    game = Game()
    # These work
    assert game.guess() == 11
    assert game.guess() == 12
    # Must enter a number
    with pytest.raises(ValueError):
        game.guess()
    # Cannot repeat a number
    with pytest.raises(ValueError):
        game.guess()
    # This works
    assert game.guess() == 5
    # Number is not in the range
    with pytest.raises(ValueError):
        game.guess()
    with pytest.raises(ValueError):
        game.guess()
    # This works
    assert game.guess() == 7
    # Must be a number
    with pytest.raises(ValueError):
        game.guess()

# To test the method _validate_guess, we need to capture the standard output
# capfd does exactly that.
def test_validate_guess(capfd):
    game = Game()
    game._answer = 4

    assert not game._validate_guess(2)
    out, _ = capfd.readouterr()
    assert out.rstrip() == "2 is too low"

    assert not game._validate_guess(8)
    out, _ = capfd.readouterr()
    assert out.rstrip() == "8 is too high"

    assert game._validate_guess(4)
    out, _ = capfd.readouterr()
    assert out.rstrip() == "4 is correct!"

@patch("builtins.input", side_effect=[10, 5, 15, 1, 2])
def test_game_win(inp, capfd):
    game = Game()
    game._answer = 2
    
    game()
    
    assert game._win
    out, _ = capfd.readouterr()
    output = [line.strip() for line in out.split("\n") if line.strip()]
    expected = [ "10 is too high",
                 "5 is too high",
                 "15 is too high",
                 "1 is too low",
                 "2 is correct!",
               ]
    for outputLine, expectedLine in zip(output,expected):
        assert outputLine == expectedLine

@patch("builtins.input", side_effect=[10, 5, 15, 1, -1, 5, 3, 4])
def test_game_lose(inp, capfd):
    game = Game()
    game._answer = 2
    
    game()
    
    assert not game._win
    out, _ = capfd.readouterr()
    output = [line.strip() for line in out.split("\n") if line.strip()]
    expected = [ "10 is too high",
                 "5 is too high",
                 "15 is too high",
                 "1 is too low",
                 "Number not in range",
                 "Already guessed",
                 "3 is too high",
                 "Guessed 5 times, answer was 2",
               ]
    for outputLine, expectedLine in zip(output,expected):
        assert outputLine == expectedLine
