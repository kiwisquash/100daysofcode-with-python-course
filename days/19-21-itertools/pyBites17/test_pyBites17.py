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
    if expected:
        assert test_input in teams
    else:
        assert test_input not in teams
