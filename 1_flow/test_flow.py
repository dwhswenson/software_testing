
def setup():
    print "Module-level setup"

def teardown():
    print "Module-level teardown"

class TestClassA(object):
    def setup(self):
        print "  Class-level setup (A)"

    def teardown(self):
        print "  Class-level teardown (A)"

    def test_this(self):
        print "    Running test (A1)"

    def test_that(self):
        print "    Running test (A2)"

class TestClassB(object):
    def setup(self):
        print "  Class-level setup (B)"

    def teardown(self):
        print "  Class-level teardown(B)"

    def test_this(self):
        print "    Running test"
