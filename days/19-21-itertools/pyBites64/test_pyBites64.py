from pyBites64 import names, locations, confirmed
from pyBites64 import get_attendees

def test_get_attendees(capfd):
    get_attendees()
    output = capfd.readouterr()[0].strip().split("\n")

    assert len(output) == 8
    assert output[0] == "('Tim', 'DE', False)"
    assert output[5] == "('Mike', 'US', '-')"
    assert output[6] == "('Kim', '-', '-')"
