from math_series import __version__


def test_version():
    assert __version__ == '0.1.0'


    from series import fibonacci, lucas, sum_series

# Fibonacci tests"
# Expected Outcome

def test_zero():
    expected = 0
    actual = fibonacci(0)
    assert actual == expected

def test_one():
    expected = 1
    actual = fibonacci(1)
    assert actual == expected

def test_15n():
    expected = 610
    actual = fibonacci(15)
    assert actual == expected


# Edge Case

def test_negative():
    expected = 0
    actual = fibonacci(-4)
    assert actual == expected

# Expected Failure

def test_letter():
    expected = "Input should be a one integer"
    actual = fibonacci("a")
    assert actual == expected


def test_float():
    expected = "Input should be a one integer"
    actual = fibonacci(1.354)
    assert actual == expected


# LUCAS TESTS
# Expected Outcome
def test_zero_lucas():
    expected = 2
    actual = lucas(0)
    assert actual == expected

def test_one_lucas():
    expected = 1
    actual = lucas(1)
    assert actual == expected

def test_three_lucas():
    expected = 4
    actual = lucas(3)
    assert actual == expected

def test_four_lucas():
    expected = 7
    actual = lucas(4)
    assert actual == expected

def test_15n_lucas():
    expected = 1364
    actual = lucas(15)
    assert actual == expected

# Edge case
def test_negative_lucas():
    expected = 2
    actual = lucas(-4)
    assert actual == expected


# expected failure
def test_15n_lucas():
    expected = "Input should be a one integer"
    actual = lucas("a")
    assert actual == expected


# SUM_SERIES TESTS
# Expected Outcome
def test_zero_sum_series_fibonacci():
    expected = 0
    actual = sum_series(0)
    assert actual == expected

def test_zero_sum_series_fibonacci_params():
    expected = 0
    actual = sum_series(0, 0, 1)
    assert actual == expected


def test_zero_sum_series_lucas():
    expected = 2
    actual = sum_series(0, 2, 1)
    assert actual == expected

def test_sum_series_new_sequence():
    expected = 123
    actual = sum_series(8, 3, 4)
    assert actual == expected

# Edge Cases
def test_sum_series_new_sequence_negative():
    expected = 3
    actual = sum_series(-4, 3, 4)
    assert actual == expected

def test_sum_series_new_sequence_negative_params():
    expected = 6
    actual = sum_series(4, -3, 4)
    assert actual == expected


# expected failure
def test_sum_series_letters():
    expected = "Input allows only integers"
    actual = sum_series('a', 3, 4)
    assert actual == expected

def test_sum_series_letters_in_params():
    expected = "Input allows only integers"
    actual = sum_series(5, 'a', 4)
    assert actual == expected
