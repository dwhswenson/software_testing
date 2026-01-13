# test_raise_exception.py
import pytest

from raise_exception import function_raises_exception

def test_function_raises_exception():
    with pytest.raises(RuntimeError):
        function_raises_exception()

def test_function_raises_exception_message():
    with pytest.raises(RuntimeError, match="This function is in a bad mood"):
        function_raises_exception()
