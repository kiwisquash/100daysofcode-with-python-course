from fizzbuzz import fizzBuzz
import pytest

def test_fizzBuzz():
    assert fizzBuzz(5) == "Buzz"
    assert fizzBuzz("3") == "Fizz"
    assert fizzBuzz(15) == "Fizz Buzz"
    assert fizzBuzz("-99") == "Fizz"
    assert fizzBuzz(0.0) == "Fizz Buzz"
    assert fizzBuzz(1) == 1 
    with pytest.raises(ValueError):
        fizzBuzz(1.1)
    with pytest.raises(ValueError):
        fizzBuzz("fishcake")
    with pytest.raises(ValueError):
        fizzBuzz('13.5')
