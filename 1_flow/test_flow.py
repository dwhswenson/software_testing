
def setup_module():
    print("Module-level setup")

def teardown_module():
    print("Module-level teardown")

class TestClassA(object):
    def setup_method(self):
        print("  Class-level setup (A)")

    def teardown_method(self):
        print("  Class-level teardown (A)")

    def test_this(self):
        print("    Running test (A1)")

    def test_that(self):
        print("    Running test (A2)")

class TestClassB(object):
    def setup_method(self):
        print("  Class-level setup (B)")

    def teardown_method(self):
        print("  Class-level teardown(B)")

    def test_this(self):
        print("    Running test")
