from pyBites17 import friends_teams
import pytest

friend_list = "Ted Jedi Glork Starp Cheese".split()


import pytest
@pytest.mark.parametrize("test_input,expected", [
    (("Ted", "Jedi"), True),
    (("Ted", "Cheese"), True),
    (("Glork", "Starp"), True),
    (("Jedi", "Jedi"), False),
    (("Jedi", "Ted"), False),
])

def test_two_friends_teams_no_order(test_input,expected):
    teams = friends_teams(friend_list)
    assert len(teams) == 10
    for team in teams:
        assert len(team) == 2
    if expected:
        assert test_input in teams
    else:
        assert test_input not in teams

@pytest.mark.parametrize("test_input,expected", [
    (("Ted", "Jedi"), True),
    (("Ted", "Cheese"), True),
    (("Cheese", "Ted"), True),
    (("Glork", "Starp"), True),
    (("Jedi", "Jedi"), False),
    (("Jedi", "Ted"), True),
])
def test_two_friends_teams_yes_order(test_input,expected):
    teams = friends_teams(friend_list,order_does_matter=True)
    assert len(teams) == 20
    for team in teams:
        assert len(team) == 2
    if expected:
        assert test_input in teams
    else:
        assert test_input not in teams

@pytest.mark.parametrize("test_input,expected", [
    (("Ted", "Jedi", "Glork"), True),
    (("Ted", "Glork", "Cheese"), True),
    (("Cheese", "Ted", "Glork"), False),
    (("Glork", "Starp", "Cheese"), True),
    (("Jedi", "Jedi", "Glork"), False),
])

def test_three_friends_teams_no_order(test_input,expected):
    teams = friends_teams(friend_list,3)
    assert len(teams) == 10
    for team in teams:
        assert len(team) == 3
    if expected:
        assert test_input in teams
    else:
        assert test_input not in teams

@pytest.mark.parametrize("test_input,expected", [
    (("Ted", "Jedi", "Glork"), True),
    (("Ted", "Glork", "Cheese"), True),
    (("Cheese", "Ted", "Glork"), True),
    (("Glork", "Starp", "Cheese"), True),
    (("Jedi", "Jedi", "Glork"), False),
])

def test_three_friends_teams_yes_order(test_input,expected):
    teams = friends_teams(friend_list,3,True)
    assert len(teams) == 60
    for team in teams:
        assert len(team) == 3
    if expected:
        assert test_input in teams
    else:
        assert test_input not in teams


