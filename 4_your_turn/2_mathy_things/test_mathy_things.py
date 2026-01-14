import pytest
from mathy_things import fibonacci, factorial

class TestFibonacci(object):
    def test_fibonacci_positive(self):
        first_fibonacci = [1, 1, 2, 3, 5, 8, 13, 21, 34]
        for i in range(len(first_fibonacci)):
            assert fibonacci(i) == first_fibonacci[i]

    def test_fibonacci_negative(self):
        with pytest.raises(ValueError):
            fibonacci(-1)

    def test_fibonacci_non_integer_input(self):
        with pytest.raises(TypeError):
            fibonacci(1.6)

class TestFactorial(object):
    def test_factorial_positive(self):
        assert factorial(1) == 1
        assert factorial(2) == 2
        assert factorial(3) == 6
        assert factorial(4) == 24
        assert factorial(5) == 120

    def test_factorial_negative(self):
        with pytest.raises(ValueError):
            factorial(-1)

    def test_factorial_zero(self):
        assert factorial(0) == 1

    def test_factorial_non_integer_input(self):
        with pytest.raises(TypeError):
            factorial(2.6)
