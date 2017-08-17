# test_raise_exception.py
from nose.tools import raises
from nose.plugins.skip import SkipTest

from raise_exception import function_raises_exception

@raises(RuntimeError)
def test_function_raises_expection():
    function_raises_exception()

def test_that_has_not_been_written():
    raise SkipTest
