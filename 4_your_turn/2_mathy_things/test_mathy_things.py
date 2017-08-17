from nose.tools import assert_equal, raises
from mathy_things import fibonacci, factorial

class TestFibonacci(object):
    def test_fibonacci_positive(self):
        first_fibonacci = [1, 1, 2, 3, 5, 8, 13, 21, 34]
        for i in range(len(first_fibonacci)):
            assert_equal(fibonacci(i), first_fibonacci[i])

    @raises(ValueError)
    def test_fibonacci_negative(self):
        fibonacci(-1)

    @raises(TypeError)
    def test_fibonacci_non_integer_input(self):
        fibonacci(1.6)

class TestFactorial(object):
    def test_factorial_positive(self):
        assert_equal(factorial(1), 1)
        assert_equal(factorial(2), 2)
        assert_equal(factorial(3), 6)
        assert_equal(factorial(4), 24)
        assert_equal(factorial(5), 120)

    @raises(ValueError)
    def test_factorial_negative(self):
        factorial(-1)

    def test_factorial_zero(self):
        assert_equal(factorial(0), 1)

    @raises(TypeError)
    def test_factorial_non_integer_input(self):
        factorial(2.6)
