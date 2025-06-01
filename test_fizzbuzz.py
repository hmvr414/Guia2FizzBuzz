import pytest
from fizzbuzz import fizzbuzz_imp

@pytest.fixture
def fizzbuzz():
    return fizzbuzz_imp()

def test_fizz_no(fizzbuzz):
    # Given
    number = 2

    # When
    output = fizzbuzz.check(number)

    # Then
    assert output == 2

def test_fizz_yes(fizzbuzz):
    # Given
    number = 3

    # When
    output = fizzbuzz.check(number)

    # Then
    assert output == "Fizz"

def test_buzz_no(fizzbuzz):
    # Given
    number = 4

    # When
    output = fizzbuzz.check(number)

    # Then
    assert output == 4

def test_buzz_yes(fizzbuzz):
    # Given
    number = 5

    # When
    output = fizzbuzz.check(number)

    # Then
    assert output == "Buzz"

def test_fizzbuzz_no(fizzbuzz):
    # Given
    number = 7

    # When
    output = fizzbuzz.check(number)

    # Then
    assert output == 7

def test_fizzbuzz_yes(fizzbuzz):
    # Given
    number = 15

    # When
    output = fizzbuzz.check(number)

    # Then
    assert output == "FizzBuzz"

def test_modulus_divisible(fizzbuzz):
    # Given
    dividend = 6
    divisor = 3

    # When
    result = fizzbuzz.modulus(dividend, divisor)

    # Then
    assert result == True

def test_modulus_not_divisible(fizzbuzz):
    # Given
    dividend = 7
    divisor = 3

    # When
    result = fizzbuzz.modulus(dividend, divisor)

    # Then
    assert result == False
